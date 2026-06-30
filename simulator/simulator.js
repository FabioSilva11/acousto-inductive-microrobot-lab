const canvas = document.getElementById('sim');
const ctx = canvas.getContext('2d');
const controls = ['robots','viscosity','flow','acoustic','release'];
const state = { robots: [], target: {x: 880, y: 310}, t: 0 };

function $(id){ return document.getElementById(id); }
function val(id){ return parseFloat($(id).value); }
function updateLabels(){
  $('robotsV').textContent = $('robots').value;
  $('viscosityV').textContent = $('viscosity').value;
  $('flowV').textContent = $('flow').value;
  $('acousticV').textContent = $('acoustic').value;
  $('releaseV').textContent = $('release').value;
}
controls.forEach(id => $(id).addEventListener('input', updateLabels));
$('reset').addEventListener('click', reset);

function reset(){
  updateLabels();
  state.robots = [];
  const n = parseInt($('robots').value, 10);
  for(let i=0;i<n;i++){
    state.robots.push({
      x: 150 + Math.random()*120,
      y: 250 + Math.random()*120,
      vx: 0, vy: 0,
      payload: 1,
      trail: []
    });
  }
}

function limit(vx, vy, max){
  const n = Math.hypot(vx, vy);
  if(n > max && n > 0) return [vx/n*max, vy/n*max];
  return [vx, vy];
}

function step(){
  const viscosity = val('viscosity');
  const flow = val('flow');
  const acoustic = val('acoustic');
  const release = val('release');
  const useSwarm = $('swarm').checked;
  const vesselTop = 120, vesselBottom = 500, center = (vesselTop+vesselBottom)/2, radius=(vesselBottom-vesselTop)/2;

  for(let i=0;i<state.robots.length;i++){
    const r = state.robots[i];
    let ax = 0, ay = 0;
    const dx = state.target.x - r.x, dy = state.target.y - r.y;
    const d = Math.hypot(dx, dy) || 1;
    ax += dx/d * acoustic * 0.018;
    ay += dy/d * acoustic * 0.018;

    // Swarm: separation + small cohesion
    if(useSwarm){
      let cx=0, cy=0, count=0, sx=0, sy=0;
      for(let j=0;j<state.robots.length;j++){
        if(i===j) continue;
        const o = state.robots[j];
        const ox = o.x-r.x, oy=o.y-r.y;
        const od = Math.hypot(ox,oy) || 1;
        if(od < 120){ cx += o.x; cy += o.y; count++; }
        if(od < 38){ sx -= ox/(od*od); sy -= oy/(od*od); }
      }
      if(count>0){ ax += ((cx/count)-r.x)*0.00008; ay += ((cy/count)-r.y)*0.00008; }
      ax += sx*12; ay += sy*12;
    }

    // Parabolic flow to the right
    const yy = Math.abs(r.y-center);
    const flowPx = flow * (1 - Math.min(1, (yy/radius)**2)) * 0.055;
    ax += flowPx;

    // viscosity damping
    r.vx = (r.vx + ax) * (1 - Math.min(0.22, viscosity*0.018));
    r.vy = (r.vy + ay) * (1 - Math.min(0.22, viscosity*0.018));
    [r.vx, r.vy] = limit(r.vx, r.vy, 2.2);
    r.x += r.vx; r.y += r.vy;

    // wall bounce
    if(r.y < vesselTop+10){ r.y = vesselTop+10; r.vy *= -0.25; }
    if(r.y > vesselBottom-10){ r.y = vesselBottom-10; r.vy *= -0.25; }
    if(r.x > canvas.width+20){ r.x = -20; }

    if(Math.hypot(state.target.x-r.x, state.target.y-r.y) < 90){
      r.payload = Math.max(0, r.payload - release*0.003);
    }
    r.trail.push({x:r.x,y:r.y});
    if(r.trail.length>50) r.trail.shift();
  }
  state.t += 1;
}

function draw(){
  ctx.clearRect(0,0,canvas.width,canvas.height);
  const vesselTop=120, vesselBottom=500, center=(vesselTop+vesselBottom)/2;

  // vessel
  const grad = ctx.createLinearGradient(0,vesselTop,0,vesselBottom);
  grad.addColorStop(0,'#ffd4d4'); grad.addColorStop(0.5,'#fff5f5'); grad.addColorStop(1,'#ffd4d4');
  ctx.fillStyle = grad; ctx.fillRect(40,vesselTop,1020,vesselBottom-vesselTop);
  ctx.strokeStyle = '#a94442'; ctx.lineWidth=5;
  ctx.strokeRect(40,vesselTop,1020,vesselBottom-vesselTop);

  // flow arrows
  ctx.strokeStyle='rgba(160,40,40,.35)'; ctx.fillStyle='rgba(160,40,40,.35)';
  for(let y=160;y<480;y+=48){
    ctx.beginPath(); ctx.moveTo(80,y); ctx.lineTo(190,y); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(190,y); ctx.lineTo(180,y-5); ctx.lineTo(180,y+5); ctx.fill();
  }

  // target cell cluster
  ctx.fillStyle='rgba(130,50,160,.85)';
  for(let i=0;i<10;i++){
    const a=i*0.9, rr=18+(i%3)*9;
    ctx.beginPath(); ctx.arc(state.target.x+Math.cos(a)*rr, state.target.y+Math.sin(a)*rr, 22,0,Math.PI*2); ctx.fill();
  }
  ctx.fillStyle='#4b165f'; ctx.font='bold 15px Arial'; ctx.fillText('região-alvo simulada', state.target.x-60, state.target.y-55);

  // medicine cloud
  const release = val('release');
  const acoustic = val('acoustic');
  const cloudR = 50 + release*90;
  const g = ctx.createRadialGradient(state.target.x,state.target.y,5,state.target.x,state.target.y,cloudR);
  g.addColorStop(0,`rgba(30,180,100,${0.28*release})`); g.addColorStop(1,'rgba(30,180,100,0)');
  ctx.fillStyle=g; ctx.beginPath(); ctx.arc(state.target.x,state.target.y,cloudR,0,Math.PI*2); ctx.fill();

  // abstract interaction ring
  ctx.strokeStyle=`rgba(220,30,30,${Math.min(.7, acoustic*release*.09)})`;
  ctx.lineWidth=3; ctx.beginPath(); ctx.arc(state.target.x,state.target.y,cloudR*0.72,0,Math.PI*2); ctx.stroke();

  // robots
  for(const r of state.robots){
    ctx.strokeStyle='rgba(0,75,145,.25)'; ctx.beginPath();
    r.trail.forEach((p,k)=>{ if(k===0) ctx.moveTo(p.x,p.y); else ctx.lineTo(p.x,p.y); }); ctx.stroke();
    ctx.save(); ctx.translate(r.x,r.y); ctx.rotate(Math.atan2(r.vy,r.vx));
    ctx.fillStyle='#0b74c9'; ctx.strokeStyle='#063b69'; ctx.lineWidth=2;
    ctx.beginPath(); ctx.ellipse(0,0,16,7,0,0,Math.PI*2); ctx.fill(); ctx.stroke();
    ctx.fillStyle='#91d5ff'; ctx.beginPath(); ctx.arc(8,0,4,0,Math.PI*2); ctx.fill();
    ctx.restore();
  }

  ctx.fillStyle='#14213d'; ctx.font='14px Arial';
  ctx.fillText(`Robôs: ${state.robots.length} | Viscosidade: ${val('viscosity')} mPa·s | Fluxo: ${val('flow')} mm/s | Intensidade acústica simulada: ${val('acoustic')}`, 50, 40);
  ctx.fillText('Índice visual vermelho = interação celular simulada, não dose real', 50, 64);
}

function loop(){ step(); draw(); requestAnimationFrame(loop); }
reset(); loop();
