# 02 — Materiais conceituais

A tabela abaixo é uma proposta conceitual de materiais, não uma receita de fabricação validada.

| Subsistema | Materiais candidatos | Por quê |
|---|---|---|
| Corpo estrutural | SiO₂, TiO₂, polímeros biocompatíveis, SU-8 experimental | Estrutura, microfabricação, encapsulamento |
| Revestimento | PEG, parylene-C, hidrogel, PLGA | Redução de aderência, compatibilidade e liberação controlada |
| Microbobina | cobre, ouro, alumínio microfabricado | Condutividade elétrica |
| Eletrônica | silício CMOS/ASIC, diodos Schottky, capacitores MIM | Retificação, controle e armazenamento temporário |
| Atuador ultrassônico | AlN, PZT, PVDF, LiNbO₃ experimental | Transdução piezoelétrica ou MEMS ultrassônico |
| Reservatório | PLGA, hidrogel, lipossomas acoplados | Liberação controlada de fármaco |
| Direcionamento | nanopartículas magnéticas/óxidos de ferro em baixa carga | Potencial orientação/feedback magnético |
| Sensores | pH, temperatura, pressão, impedância, contraste acústico | Feedback conceitual |

## Observações de biocompatibilidade

- Materiais como PEG, PLGA e parylene-C são muito usados em contextos biomédicos, mas cada uso precisa de validação específica.
- Materiais piezoelétricos como PZT podem envolver chumbo; em um projeto real isso exigiria encapsulamento rigoroso ou escolha de alternativas.
- Grafeno/óxidos e nanopartículas exigem avaliação toxicológica específica.

## Escolha mais conservadora para simulação

Para o simulador, adote:

```text
corpo: polímero biocompatível simplificado
revestimento: PEG/PLGA
atuador: PMUT conceitual baseado em AlN ou PVDF
energia: indução externa com armazenamento capacitivo
medicamento: carga genérica sem dose real
```
