# Como criar o repositório no GitHub

A ferramenta disponível nesta conversa consegue mexer em repositórios existentes, mas não expôs uma ação para criar um repositório novo do zero. Por isso o pacote foi montado pronto para subir manualmente.

## Opção 1 — pelo site do GitHub

1. Entre no GitHub.
2. Clique em **New repository**.
3. Nome sugerido: `acousto-inductive-microrobot-lab`.
4. Crie vazio, sem README automático.
5. Faça upload dos arquivos deste pacote.

## Opção 2 — pelo terminal

```bash
git init
git add .
git commit -m "Initial educational microrobot simulator"
git branch -M main
git remote add origin https://github.com/FabioSilva11/acousto-inductive-microrobot-lab.git
git push -u origin main
```
