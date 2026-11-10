# Monta o site publicável a partir do resultado do build.py: uma página por endereço, imagens em WebP,
# sitemap, robots, 404 e configuração da Vercel.
# Uso: python3 site.py [pasta de saída]   (padrão: ../site; precisa de: pip install pillow)
import sys
from pathlib import Path
AQUI = Path(__file__).resolve().parent
SITE = str(Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else AQUI.parent / 'site')
Path(SITE).mkdir(parents=True, exist_ok=True)
src = open(AQUI / 'saida' / 'portfolio-leonardo.html', encoding='utf-8').read()
src = src.replace('<title>Leonardo Fernandes — Designer Conversacional</title>\n', '').replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '')
i = src.find('<style>'); j = src.find('</style>') + len('</style>')
head_extra, corpo = src[:j], src[j:]
desc = 'Portfólio de Leonardo Fernandes, designer conversacional e UX Writer em São Paulo. Cases de chatbots no WhatsApp e de product design.'
html = f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Leonardo Fernandes — Designer Conversacional</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="Leonardo Fernandes — Designer Conversacional">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://leonvrdof.vercel.app/">
<meta property="og:image" content="https://leonvrdof.vercel.app/capa.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="627">
<meta property="og:image:alt" content="Leonardo Fernandes, Designer Conversacional e UX Writer. Ao lado, um celular com a conversa da Lia, assistente de viagens no WhatsApp.">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#F7F7F5">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{head_extra}
</head>
<body>
{corpo}
</body>
</html>
'''
open(SITE + '/index.html', 'w', encoding='utf-8').write(html)
open(SITE + '/favicon.svg', 'w').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><path d="M32 4 56 28 32 60 8 28Z" fill="#141414"/><path d="M32 4 56 28H8Z" fill="#C8102E"/><path d="M32 4V60" stroke="#F7F7F5" stroke-width="2"/></svg>')
import json as _json
_vj = {"cleanUrls": True, "headers": [
  {"source": "/(.*)", "headers": [{"key": "X-Content-Type-Options", "value": "nosniff"}, {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"}]},
  # currículo abre no navegador e, ao salvar, vem com o nome dele
  {"source": "/curriculo.pdf", "headers": [{"key": "Content-Disposition", "value": "inline; filename=\"Leonardo-Fernandes-Curriculo.pdf\""}, {"key": "Cache-Control", "value": "public, max-age=0, must-revalidate"}]}]}
open(SITE + '/vercel.json', 'w').write(_json.dumps(_vj, indent=2, ensure_ascii=False) + '\n')
open(SITE + '/README.md', 'w', encoding='utf-8').write('# Portfólio · Leonardo Fernandes\n\nSite estático publicado na Vercel: https://leonvrdof.vercel.app\n\nCada página tem endereço próprio (`/lia`, `/tom`, `/drogaria`, `/petgram`, `/assai`, `/sobre`). São cópias do mesmo site, cada uma com título e descrição próprios, e a Vercel serve `lia.html` em `/lia` (`cleanUrls`). Links antigos com `#` (`/#lia`) são levados ao endereço novo.\n\nOs protótipos da Lia e do Tom rodam dentro dos celulares dos cases, pelo modo vitrine (`?modo=vitrine`) dos sites deles.\n\nEstes arquivos são gerados. O código-fonte fica na pasta `fonte/` do projeto (`build.py` e depois `site.py`); não edite os `.html` daqui à mão.\n')
print('ok')

# imagens em arquivos WebP separados (página mais leve, carregamento sob demanda)
import re, base64, hashlib, io, os, shutil
from PIL import Image
d = SITE + '/img'
shutil.rmtree(d, ignore_errors=True); os.makedirs(d)
h = open(SITE + '/index.html', encoding='utf-8').read()
def troca(m):
    raw = base64.b64decode(m.group(2)); nome = hashlib.sha1(raw).hexdigest()[:10] + '.webp'
    caminho = os.path.join(d, nome)
    if not os.path.exists(caminho):
        im = Image.open(io.BytesIO(raw)); im = im.convert('RGBA' if im.mode in ('RGBA', 'LA', 'P') else 'RGB'); im.save(caminho, 'WEBP', quality=82, method=6)
    return '/img/' + nome
h = re.sub(r'data:image/(jpeg|png|webp);base64,([A-Za-z0-9+/=]+)', troca, h)
def dim(m):
    tag = m.group(0)
    if 'width=' in tag: return tag
    src = re.search(r'src="(/img/[^"]+)"', tag)
    if not src: return tag
    w, hh = Image.open(SITE + src.group(1)).size
    return tag.replace('<img ', f'<img width="{w}" height="{hh}" ', 1)
h = re.sub(r'<img [^>]*>', dim, h)
open(SITE + '/index.html', 'w', encoding='utf-8').write(h)
print('imagens', len(os.listdir(d)), 'html', len(h))
shutil.copy(AQUI / 'og' / 'og-1x.png', SITE + '/og.png')
# mesmo arquivo com outro nome: o endereço novo faz WhatsApp e LinkedIn buscarem a imagem de novo
shutil.copy(AQUI / 'og' / 'og-1x.png', SITE + '/capa.png')
shutil.copy(AQUI / 'curriculo.pdf', SITE + '/curriculo.pdf')

# páginas com endereço próprio: /lia, /tom, /sobre... (a Vercel serve lia.html em /lia por causa do cleanUrls)
B = 'https://leonvrdof.vercel.app'
h = open(SITE + '/index.html', encoding='utf-8').read()
h = h.replace('<head>\n', '<head>\n<script>window.ROTAS_LIMPAS=true</script>\n', 1)
# ficha para o Google (dados estruturados): quem é o dono do site, ligada ao LinkedIn
import json as _j
_foto = re.search(r'<img src="(/img/[0-9a-f]+\.webp)"[^>]*alt="Leonardo Fernandes sentado', h)
_ficha = {"@context": "https://schema.org", "@graph": [
  {"@type": "Person", "@id": "https://leonvrdof.vercel.app/#leonardo", "name": "Leonardo Fernandes",
   "alternateName": "Leonardo Fernandes de Almeida", "jobTitle": "Designer Conversacional e UX Writer",
   "description": "Designer conversacional e UX Writer. Desenha conversas de chatbots e assistentes no WhatsApp.",
   "url": "https://leonvrdof.vercel.app/", **({"image": "https://leonvrdof.vercel.app" + _foto.group(1)} if _foto else {}),
   "sameAs": ["https://www.linkedin.com/in/leonvrdof", "https://github.com/leonvrdof"],
   "address": {"@type": "PostalAddress", "addressLocality": "São Paulo", "addressRegion": "SP", "addressCountry": "BR"},
   "alumniOf": [{"@type": "CollegeOrUniversity", "name": "Universidade Anhembi Morumbi"}, {"@type": "CollegeOrUniversity", "name": "Universidade Cruzeiro do Sul"}],
   "knowsAbout": ["Design conversacional", "UX Writing", "Chatbots", "WhatsApp", "Content Design", "UX Design", "Acessibilidade"],
   "knowsLanguage": ["pt-BR", "es", "en"]},
  {"@type": "WebSite", "@id": "https://leonvrdof.vercel.app/#site", "url": "https://leonvrdof.vercel.app/", "name": "Leonardo Fernandes — Designer Conversacional", "inLanguage": "pt-BR", "author": {"@id": "https://leonvrdof.vercel.app/#leonardo"}}]}
assert _foto, 'foto do sobre'
h = h.replace('</head>', '<script type="application/ld+json">' + _j.dumps(_ficha, ensure_ascii=False) + '</script>\n</head>', 1)
# Google Search Console: confirma que o site é do Leonardo (não remover)
h = h.replace('<head>\n', '<head>\n<meta name="google-site-verification" content="z2XPxKjB1APv3-MzLcT5TTWi-wAIZYrJHr1w3sVIA0Q">\n', 1)
# Vercel Web Analytics: conta visitas e páginas, sem cookies; acompanha as trocas de página (/lia, /tom...) sozinho
h = h.replace('</head>', '<script>window.va = window.va || function () { (window.vaq = window.vaq || []).push(arguments); };</script>\n<script defer src="/_vercel/insights/script.js"></script>\n</head>', 1)
h = re.sub(r'href="#inicio"( data-ir="inicio")', r'href="/"\1', h)
h = re.sub(r'href="#(\w+)"( data-ir="\1")', r'href="/\1"\2', h)
assert 'href="#lia"' not in h and 'data-ir="sobre"' in h
PAG = {
 'index': ('Leonardo Fernandes — Designer Conversacional', desc, '/'),
 'sobre': ('Sobre mim — Leonardo Fernandes', 'Trajetória de Leonardo Fernandes: formação, experiência e o caminho até o design conversacional e o UX Writing.', '/sobre'),
 'lia': ('Lia, assistente de viagens — Leonardo Fernandes', 'Assistente no WhatsApp que ajuda pessoas com 50 anos ou mais a escolher o destino da viagem, uma pergunta de cada vez. Com protótipo para testar.', '/lia'),
 'tom': ('Tom, da Clínica Veterinária Vila Matilde — Leonardo Fernandes', 'Assistente no WhatsApp da clínica: agenda consultas, envia a receita digital e tira dúvidas sobre o cuidado com o pet. Com protótipo para testar.', '/tom'),
 'drogaria': ('Drogaria Popular — Leonardo Fernandes', 'Fluxo sem IA para o WhatsApp da farmácia: confere o cadastro pelo CPF e responde às dúvidas frequentes.', '/drogaria'),
 'petgram': ('Petgram — Leonardo Fernandes', 'App para tutores trocarem histórias e dicas de cuidado com cães e gatos. Projeto em grupo, da pesquisa ao teste de usabilidade.', '/petgram'),
 'assai': ('Redesign Assaí Atacadista — Leonardo Fernandes', 'Redesign do app para a compra acontecer dentro dele, com retirada na loja, sem depender do iFood e do Rappi.', '/assai'),
}
def pagina(tit, ds, url):
    p = h
    p = p.replace('<title>Leonardo Fernandes — Designer Conversacional</title>', f'<title>{tit}</title>\n<link rel="canonical" href="{B}{url}">', 1)
    p = p.replace(f'<meta name="description" content="{desc}">', f'<meta name="description" content="{ds}">', 1)
    p = p.replace('<meta property="og:title" content="Leonardo Fernandes — Designer Conversacional">', f'<meta property="og:title" content="{tit}">', 1)
    p = p.replace(f'<meta property="og:description" content="{desc}">', f'<meta property="og:description" content="{ds}">', 1)
    p = p.replace(f'<meta property="og:url" content="{B}/">', f'<meta property="og:url" content="{B}{url}">', 1)
    assert p.count(f'<title>{tit}</title>') == 1 and f'og:url" content="{B}{url}"' in p
    return p
for arq, (tit, ds, url) in PAG.items():
    open(f'{SITE}/{arq}.html', 'w', encoding='utf-8').write(pagina(tit, ds, url))
open(SITE + '/404.html', 'w', encoding='utf-8').write(pagina(*PAG['index']).replace('<head>\n', '<head>\n<meta name="robots" content="noindex">\n<script>window.E404=true</script>\n', 1).replace('<title>Leonardo Fernandes — Designer Conversacional</title>', '<title>Página não encontrada — Leonardo Fernandes</title>', 1))
open(SITE + '/sitemap.xml', 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{B}{u}</loc></url>\n' for _, _, u in PAG.values()) + '</urlset>\n')
open(SITE + '/robots.txt', 'w').write(f'User-agent: *\nAllow: /\nSitemap: {B}/sitemap.xml\n')
print('paginas', len(PAG))

# certificados (abrem na janela por cima do portfólio)
shutil.rmtree(SITE + '/certificados', ignore_errors=True)
shutil.copytree(AQUI / 'certificados', SITE + '/certificados')
