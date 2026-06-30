# 04 — Modelos matemáticos usados

Os modelos são aproximações de primeira ordem para simulação.

## 1. Arrasto viscoso

Para uma partícula pequena em regime laminar, usamos uma aproximação tipo Stokes:

```text
F_drag = 6π μ r_eff (v_robot - v_flow)
```

Onde:

- `μ`: viscosidade dinâmica;
- `r_eff`: raio efetivo;
- `v_robot`: velocidade do microrrobô;
- `v_flow`: velocidade do fluido local.

## 2. Número de Reynolds

```text
Re = ρ v L / μ
```

Para `Re << 1`, a inércia é pequena e a viscosidade domina. Isso é comum em microrrobôs.

## 3. Pressão de radiação acústica simplificada

```text
P_rad ≈ 2I / c
F_acoustic ≈ η A P_rad
```

Onde:

- `I`: intensidade acústica simulada;
- `c`: velocidade do som no fluido;
- `A`: área efetiva do atuador;
- `η`: eficiência abstrata do acoplamento.

Isso não substitui simulação acústica real por elementos finitos.

## 4. Potência por indução

A tensão induzida ideal em uma bobina simplificada:

```text
V_rms ≈ N A ω B / sqrt(2)
P_available ≈ η_transfer V_rms² / R_load
```

Onde:

- `N`: número de espiras;
- `A`: área da bobina;
- `ω`: frequência angular;
- `B`: campo magnético alternado;
- `R_load`: carga equivalente;
- `η_transfer`: eficiência aproximada.

## 5. Liberação de medicamento

Modelo de primeira ordem:

```text
dm/dt = -k_release * duty * m
```

A concentração local é estimada de forma simplificada por um volume de difusão:

```text
C_local ≈ m_released / V_diffusion
```

## 6. Índice abstrato de interação celular

Para manter o projeto seguro, não usamos “dose de destruição”. Usamos um escore de interação:

```text
MI = P_neg_MPa / sqrt(f_MHz)
interaction_score = sigmoid((MI - MI_ref) / width) * exposure_factor
```

Esse escore serve para visualizar regiões de maior interação mecânica simulada, não para orientar tratamento real.
