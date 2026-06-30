# 01 — Visão geral do conceito

## Ideia central

O sistema é dividido em duas partes:

1. **Unidade externa:** bobina de indução e, opcionalmente, matriz de transdutores/campos direcionais.
2. **Microrrobô:** corpo biocompatível com microbobina receptora, retificação, armazenamento temporário, controle, atuadores ultrassônicos, reservatório de carga terapêutica e sensores conceituais.

O objetivo computacional é simular:

- movimento para frente/trás;
- movimento lateral;
- rotação yaw/pitch/roll simplificada;
- arrasto em fluido viscoso;
- fluxo semelhante a vaso sanguíneo;
- liberação local de medicamento;
- controle por enxame.

## Arquitetura conceitual

```text
Bobina externa -> campo alternado -> microbobina receptora -> retificação -> barramento DC
                                                      -> controlador -> drivers -> atuadores ultrassônicos
                                                      -> sensores -> feedback -> controle de trajetória
                                                      -> reservatório -> liberação de medicamento
```

## Grau de liberdade

- X: frente/trás;
- Y: esquerda/direita;
- Z: cima/baixo;
- yaw: rotação horizontal;
- pitch: inclinação;
- roll: rolagem.

Na simulação HTML5 usamos 2D por clareza visual. Nos códigos Python, o modelo permite vetores 2D ou 3D.

## Parâmetros iniciais usados nas simulações

| Parâmetro | Valor base | Observação |
|---|---:|---|
| Comprimento | 300 µm | Escala conceitual de microrrobô, não nanorrobô real |
| Diâmetro | 120 µm | Corpo tipo cápsula |
| Viscosidade do fluido | 3,5 mPa·s | Ordem de grandeza do sangue |
| Densidade do fluido | 1060 kg/m³ | Ordem de grandeza do sangue |
| Velocidade de fluxo | 0–5 mm/s | Simulação de vaso pequeno/lento |
| Controle | PID/pure pursuit + enxame | Conceitual |

## Premissa importante

Quanto menor o robô, mais difícil é colocar dentro dele: fonte de energia, retificador, controlador, sensores, reservatório e atuadores. Por isso este projeto trabalha em escala **micrométrica** e não afirma viabilidade de um nanorrobô autônomo completo.
