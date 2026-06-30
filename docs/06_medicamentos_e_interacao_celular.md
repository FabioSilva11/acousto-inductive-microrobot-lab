# 06 — Medicamentos e interação celular

## Entrega de medicamento

O modelo usa um reservatório genérico com liberação de primeira ordem. Ele não contém dose real, nome de fármaco ou protocolo de tratamento.

Variáveis simuladas:

- `payload_mass_ug`: massa inicial genérica;
- `release_rate`: taxa abstrata de liberação;
- `duty_cycle`: fração de tempo em modo de liberação;
- `diffusion_radius`: raio abstrato da nuvem local.

## Interação celular

A simulação de célula-alvo usa três camadas:

1. proximidade do robô ao alvo;
2. liberação de medicamento;
3. índice mecânico abstrato ligado a ultrassom.

```text
cell_effect_score = proximity * (drug_score + acoustic_interaction_score)
```

Esse resultado não representa morte celular real. Ele serve para comparar estratégias de navegação e entrega localizada.

## Mecanismos reais que precisariam ser pesquisados

- sonoporação;
- microbolhas e cavitação controlada;
- hipertermia localizada;
- liberação por pH;
- ligantes para células-alvo;
- drug delivery por PLGA/lipossomas/hidrogéis;
- terapia fototérmica ou magnetotérmica, quando aplicável.

## Controle de segurança em projeto real

Qualquer sistema real teria que monitorar:

- temperatura;
- pressão acústica;
- cavitação não desejada;
- dose acumulada;
- posição em tempo real;
- coagulação/agregação;
- resposta imune.
