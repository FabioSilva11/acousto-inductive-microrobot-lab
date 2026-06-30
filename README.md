# Acousto-Inductive Microrobot Lab

> **Status:** pesquisa conceitual, documentação e simulação. Não é um dispositivo médico, não é protocolo clínico e não deve ser usado em pessoas, animais ou células reais sem projeto formal, revisão ética, ensaios regulamentados e equipe especializada.

Este repositório organiza a ideia de um **microrrobô biomédico conceitual** com:

- energia externa por **indução eletromagnética**;
- atuação por **microatuadores ultrassônicos**;
- navegação em fluido viscoso parecido com sangue;
- controle de movimento 2D/3D;
- modelo de enxame;
- simulação de entrega de medicamento;
- simulação segura de **índice de interação celular**, sem fornecer receita real para destruir células.

## Nome sugerido do repositório

`acousto-inductive-microrobot-lab`

## O que está incluído

```text
.
├── README.md
├── SAFETY.md
├── requirements.txt
├── docs/
│   ├── 01_visao_geral.md
│   ├── 02_materiais.md
│   ├── 03_fabricacao_conceitual.md
│   ├── 04_modelos_matematicos.md
│   ├── 05_controle_e_enxame.md
│   ├── 06_medicamentos_e_interacao_celular.md
│   ├── 07_custos_e_viabilidade.md
│   └── referencias.md
├── src/microrobot_lab/
│   ├── constants.py
│   ├── physics.py
│   ├── induction_power.py
│   ├── drug_release.py
│   ├── cell_interaction.py
│   ├── motion_sim.py
│   └── swarm_control.py
├── examples/
│   ├── run_motion_demo.py
│   ├── run_swarm_demo.py
│   └── run_therapy_safety_demo.py
├── simulator/
│   ├── index.html
│   ├── style.css
│   └── simulator.js
└── assets/images/
```

## Como rodar a simulação Python

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python examples/run_motion_demo.py
python examples/run_swarm_demo.py
python examples/run_therapy_safety_demo.py
```

Os resultados aparecem em `outputs/`.

## Como abrir o simulador HTML5

Abra o arquivo:

```text
simulator/index.html
```

Ele funciona offline no navegador, com controles para viscosidade, intensidade acústica simulada, fluxo do vaso, quantidade de robôs, liberação de medicamento e enxame.

## Limites honestos do projeto

A ideia é plausível **como linha de pesquisa**, mas a versão apresentada aqui não é um projeto fabricável pronto. Os maiores obstáculos são:

1. miniaturização real de bobina, retificador, controle e atuadores;
2. aquecimento e segurança tecidual;
3. imageamento/feedback em tempo real;
4. biocompatibilidade e degradação controlada;
5. seletividade contra célula-alvo;
6. controle robusto em fluxo pulsátil e geometrias reais de vasos;
7. fabricação MEMS/NEMS com alto rendimento.

## Referências principais

Consulte [`docs/referencias.md`](docs/referencias.md). O projeto se apoia em revisões sobre microrrobôs acionados por ultrassom, atuação magneto-acústica híbrida, transferência de energia sem fio para implantes e interação ultrassom-membrana celular.
