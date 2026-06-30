# 07 — Custos e viabilidade

## Custos aproximados por protótipo experimental

Estes valores são apenas estimativas de ordem de grandeza, variando muito por país, laboratório, escala e processo.

| Item | Protótipo acadêmico | Escala industrial |
|---|---:|---:|
| Máscaras/litografia MEMS | alto | diluído por lote |
| Wafer/processamento | alto | médio por unidade |
| Piezo/PMUT/CMUT | alto | médio |
| Encapsulamento biocompatível | médio/alto | médio |
| Microbobina/metalização | médio | baixo/médio |
| Teste e metrologia | alto | médio |
| Validação biomédica | muito alto | muito alto |

## Estimativa simbólica por unidade

No simulador usamos um modelo simples:

```text
custo_unidade = custo_fixo_lote / quantidade + custo_material + custo_teste + custo_perdas
```

Exemplo puramente ilustrativo:

- lote de pesquisa pequeno: caro por unidade;
- lote industrial grande: custo unitário cai, mas validação continua cara.

## Viabilidade por subsistema

| Subsistema | Viabilidade hoje | Comentário |
|---|---|---|
| Propulsão acústica externa | média/alta em pesquisa | Já existe literatura de microrrobôs acústicos |
| Microbobina receptora | média | Depende de escala e alinhamento |
| Controle interno completo | baixa/média | Difícil em 100–300 µm |
| Enxame controlado | média em simulação, difícil in vivo | Exige feedback robusto |
| Terapia seletiva | baixa/média | Precisa validação biológica forte |
| Uso clínico | muito distante | Regulatório e segurança são grandes barreiras |

## Caminho mais realista de pesquisa

1. Simulação 2D/3D.
2. Microcanal com fluido viscoso artificial.
3. Micropartículas passivas acionadas externamente.
4. Medição de movimento com microscópio.
5. Teste de liberação de corante inerte.
6. Só depois pensar em modelos biológicos aprovados.
