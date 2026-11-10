# Código-fonte do portfólio

Esta pasta gera o site de https://leonvrdof.vercel.app. Os arquivos da pasta `site/` são o resultado: não edite aqueles `.html` à mão, porque a próxima geração apaga a mudança.

## Como gerar o site

1. `python3 build.py` monta tudo num arquivo só, em `saida/portfolio-leonardo.html`.
2. `python3 site.py` transforma esse arquivo no site, na pasta `../site`. Para gerar em outra pasta: `python3 site.py caminho/da/pasta`.
3. Publicar: enviar para o repositório `leonvrdof/portfolio` no GitHub. A Vercel publica sozinha a cada envio.

No repositório do GitHub, o site pronto fica na raiz, e não numa pasta `site/`. Lá o passo 2 é `python3 fonte/site.py .`. As pastas `fonte/` e `assets/` ficam no repositório, mas não são publicadas no site (arquivo `.vercelignore`).

Precisa de Python 3 com `pip install markdown pillow`.

## O que é cada arquivo

| Arquivo | O que tem |
|---|---|
| `template.html` | A página: visual (CSS), navegação (JS), início, Sobre mim e a moldura dos cases |
| `../assets/textos-cases/*.md` | Os textos originais dos cases. Lia, Tom e Drogaria são lidos daqui |
| `corpos/` | Petgram e Assaí já em HTML |
| `visuais.py` | Blocos visuais dos cases: persona, mapas, jornada, telas com mapa de calor |
| `resumos.py` | Resumo no topo de cada case, visuais do Tom e o convite no fim |
| `reescritas.py` | Trocas de frase aplicadas na geração. Os textos originais não mudam |
| `imgs/` | Telas do Petgram e do Assaí |
| `certificados/` | Certificados que abrem na janela do Sobre mim |
| `curriculo.pdf` | O currículo publicado em `/curriculo.pdf`. Para atualizar, troque este arquivo |
| `og/` | Imagem que aparece ao compartilhar o link (LinkedIn, WhatsApp) |
| `testes/` | Testes automáticos |

## Testes

Precisam de Node com `npm install playwright axe-core` nesta pasta.

- `node testes/qa.js` abre as 7 páginas em 3 larguras e 2 temas. Confere acessibilidade (WCAG A e AA), erros, imagens quebradas, rolagem lateral e a navegação.
- `node testes/regr.js pasta` fotografa todas as telas. Rode antes e depois de uma mudança e compare as duas pastas.

## Regras do projeto

- Nome: Leonardo Fernandes, nunca "Léo".
- Acessibilidade conduz as palavras: "Acessar" no lugar de "ver", "Selecione" no lugar de "Toque" ou "Clique".
- Os textos originais dos cases não são reescritos. Mudanças de frase vão em `reescritas.py`.
- Sem menção a Dawntech nem a Google AI Studio.
