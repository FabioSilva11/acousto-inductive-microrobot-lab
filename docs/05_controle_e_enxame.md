# 05 — Controle e tecnologia de enxame

## Controle individual

O microrrobô simulado usa controle por direção desejada:

1. calcula vetor até o alvo;
2. calcula erro entre direção atual e direção desejada;
3. converte o erro em comando de atuadores;
4. soma correção contra fluxo;
5. limita aceleração/velocidade.

## Controle 3D conceitual

Para movimento em 3D, o robô teria atuadores em múltiplas faces:

- atuador frontal/traseiro: frente e ré;
- atuadores laterais: esquerda/direita;
- atuadores dorsais/ventrais: cima/baixo;
- pares diferenciais: yaw, pitch e roll.

## Enxame

O módulo de enxame usa três regras clássicas:

1. **Separação:** evitar colisões entre robôs.
2. **Coesão:** manter o grupo unido.
3. **Alinhamento:** seguir direção média local.

Além disso, existe atração ao alvo terapêutico e repulsão da parede do vaso.

## Por que enxame ajuda

Um microrrobô isolado pode carregar pouca energia e pouco medicamento. Um enxame permite:

- distribuir carga terapêutica;
- compensar perdas individuais;
- cobrir área maior;
- reduzir dependência de um único robô;
- usar comportamento coletivo para manter posição contra fluxo.

## Riscos do enxame

- agregação indesejada;
- bloqueio de microvasos;
- dificuldade de recuperação;
- controle individual limitado;
- interferência entre microbobinas e atuadores.

O simulador inclui repulsão entre robôs justamente para visualizar esse risco.
