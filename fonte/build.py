# Monta o portfólio num arquivo só (saida/portfolio-leonardo.html), com as imagens embutidas.
# Uso: python3 build.py   (precisa de: pip install markdown)
import re, markdown, html
from pathlib import Path
AQUI = Path(__file__).resolve().parent
from visuais import *
import reescritas

SRC = str(AQUI.parent / 'assets' / 'textos-cases') + '/'   # os textos originais dos cases
OUT = AQUI / 'saida' / 'portfolio-leonardo.html'
TPL = AQUI / 'template.html'

LEGENDAS = {
    '01-lia-assistente-de-viagens.md': ['Imagem do case: síntese da entrevista', 'Imagem do case: canais do chatbot', 'Imagem do case: fluxo feliz'],
    '03-drogaria-popular.md': ['Imagem do case: Double Diamond', 'Imagem do case: mapa mental do fluxo'],
    '04-petgram.md': ['Capa: telas do Petgram no celular', 'Naming, logotipo e símbolo', 'Matriz CSD: certezas, suposições e dúvidas', 'Diagrama de afinidades das entrevistas', 'Mapa de empatia da Juliana, com dores e ganhos', 'Persona: Juliana e a Mel', 'Canvas de proposta de valor', 'Wireframes das telas', 'Style guide: logo, cores, tipografia e componentes', 'Mapas de calor do teste no Maze'],
    '05-redesign-assai.md': ['Avaliações negativas na Play Store', 'Ranking ABRAS', 'Gráficos do mercado de compras online', 'Design atual com as heurísticas de Nielsen', 'Objetivos do redesign', 'Heurísticas antes e depois do redesign', 'Matriz CSD', 'Proto-persona', 'Benchmark de apps parecidos', 'User flow da compra', 'Wireframes de baixa fidelidade', 'UI Design: telas finais'],
}

CUSTOM = {
    ('01-lia-assistente-de-viagens.md', 1): LIA_EMPATIA,
    ('01-lia-assistente-de-viagens.md', 2): '',
    ('01-lia-assistente-de-viagens.md', 3): '',
    ('03-drogaria-popular.md', 1): DRO_DIAMANTE,
    ('03-drogaria-popular.md', 2): DRO_MAPA,
}

def troca(b, velho, novo):
    assert b.count(velho) == 1, velho[:60]
    return b.replace(velho, novo)

def case_html(fname):
    s = open(SRC + fname, encoding='utf-8').read()
    s = re.sub(r'<!--.*?-->', '', s, flags=re.S)
    s = s.split('\n---\n')[0]
    titulo = re.search(r'^# (.+)$', s, re.M).group(1)
    s = re.sub(r'^# .+$', '', s, count=1, flags=re.M)
    s = re.sub(r'^Resumo do card na home:.*$', '', s, flags=re.M)
    s = s.replace(' {#prototipo}', '')
    legendas = LEGENDAS.get(fname, [])
    def img(m):
        i = int(m.group(1)) - 1
        cap = legendas[i] if i < len(legendas) else 'Imagem do case'
        bloco = CUSTOM.get((fname, i + 1))
        if bloco is not None:
            return '\n' + bloco + '\n'
        return f'\n<figure class="ph"><div>{cap}</div><figcaption>A imagem original entra aqui na versão final do site.</figcaption></figure>\n'
    s = re.sub(r'\[IMAGEM (\d+)\]', img, s)
    body = markdown.markdown(s, extensions=['sane_lists'])
    body = body.replace('<h2>', '<h2 class="ch">').replace('<a href="http', '<a target="_blank" rel="noopener" href="http')
    body = body.replace('href="#prototipo"', 'href="#lia-prototipo" data-scroll="1"')
    return titulo, body

lia_t, lia_b = case_html('01-lia-assistente-de-viagens.md')
lia_b = troca(lia_b, '<ul>\n<li>BlipChat</li>\n<li>WhatsApp</li>\n</ul>', LIA_CANAIS)
lia_b = re.sub(r'(planejar uma viagem com autonomia e confiança\.</p>)', lambda m: m.group(1) + LIA_PERSONA, lia_b, count=1)
lia_b = re.sub(r'<ol>\n<li>Escolher o destino ideal</li>[\s\S]*?</ol>', LIA_FLUXO_FELIZ, lia_b, count=1)
lia_b = re.sub(r'<ul>\n<li>Etapa 1:[\s\S]*?</ul>', LIA_JORNADA, lia_b, count=1)
tom_t, tom_b = case_html('02-tom-clinica-veterinaria.md')
dro_t, dro_b = case_html('03-drogaria-popular.md')
dro_b = troca(dro_b, '<p>Onboarding ➔ Validação Cadastral ➔ FAQ ➔ Finalização</p>', DRO_FLUXO)
pet_t, _ = case_html('04-petgram.md')
pet_b = open(AQUI / 'corpos' / 'petgram-body.html', encoding='utf-8').read()
pet_b, n = re.subn(r'<ul class="pg-chips pg-chips-claros largo">[\s\S]*?<figure class="ph"><div>Diagrama de afinidades completo</div>[\s\S]*?</figure>', lambda m: pet_afinidades(), pet_b); assert n == 1
pet_b = troca(pet_b, '<figure class="ph"><div>Mapa de empatia da Juliana, com dores e ganhos</div><figcaption>A imagem original entra aqui na versão final do site.</figcaption></figure>', pet_empatia())
pet_b, n = re.subn(r'<ol class="pg-tarefas largo">[\s\S]*?</ol>\n<figure class="ph"><div>Mapas de calor do teste no Maze</div>[\s\S]*?</figure>', lambda m: pet_maze(), pet_b); assert n == 1
ass_t, _ = case_html('05-redesign-assai.md')
ass_b = open(AQUI / 'corpos' / 'assai-body.html', encoding='utf-8').read()
ass_b = troca(ass_b, '<figure class="ph"><div>Telas finais do app</div><figcaption>A imagem original entra aqui na versão final do site.</figcaption></figure>', assai_ui())

for velho, novo in reescritas.LIA: lia_b = troca(lia_b, velho, novo)
for velho, novo in reescritas.PET: pet_b = troca(pet_b, velho, novo)
for velho, novo in reescritas.ASS: ass_b = troca(ass_b, velho, novo)

# resumo no topo dos cases (o conteúdo original continua inteiro) e frase do desafio da Drogaria
import resumos
lia_b = resumos.LIA + lia_b
# Tom: resumo em caixa (mesmo conteúdo) e visuais com o que o case já diz
_m = re.search(r'<h2 class="ch">Resumo</h2>[\s\S]*?Testar o MVP do Tom[\s\S]*?</p>\n', tom_b); assert _m, 'resumo tom'
tom_b = tom_b.replace(_m.group(0), resumos.TOM, 1)
_p = 'Opinion Box, junho de 2025'
_i = tom_b.find(_p); assert _i > 0; _f = tom_b.find('</p>', _i) + len('</p>\n')
tom_b = tom_b[:_f] + resumos.TOM_DADOS + tom_b[_f:]
_i = tom_b.find('e eu decidia o que entrava.</p>'); assert _i > 0; _f = _i + len('e eu decidia o que entrava.</p>\n')
tom_b = tom_b[:_f] + resumos.TOM_DOC + tom_b[_f:]
_m = re.search(r'<ul>\s*<li>Pedir o mínimo de dados\.[\s\S]*?</ul>\n', tom_b); assert _m, 'decisoes tom'
tom_b = tom_b.replace(_m.group(0), resumos.TOM_DECISOES, 1)
_m = re.search(r'<p>V1: “Toque[\s\S]*?</p>\n<p>V2: “Como posso[\s\S]*?</p>\n', tom_b); assert _m, 'v1v2 tom'
tom_b = tom_b.replace(_m.group(0), '<p>A mesma mensagem de boas-vindas, antes e depois das regras:</p>\n' + resumos.TOM_V1V2, 1)
dro_b = resumos.DRO + troca(dro_b, *resumos.DRO_DESAFIO)
_m = re.search(r'<section class="pg-abre largo">\s*<dl class="pg-ficha">[\s\S]*?</dl>\s*</section>\s*', pet_b); assert _m, 'ficha petgram'
pet_b = pet_b.replace(_m.group(0), resumos.PET + '\n', 1)
_m = re.search(r'<section class="largo">\s*<dl class="pg-ficha">[\s\S]*?</dl>\s*</section>\s*', ass_b); assert _m, 'ficha assai'
ass_b = ass_b.replace(_m.group(0), resumos.ASS + '\n', 1)
t = open(TPL, encoding='utf-8').read()
t = t.replace('{{LIA_T}}', html.escape(lia_t)).replace('{{LIA_B}}', lia_b)
t = t.replace('{{TOM_T}}', html.escape(tom_t)).replace('{{TOM_B}}', tom_b)
t = t.replace('{{DRO_T}}', html.escape(dro_t)).replace('{{DRO_B}}', dro_b)
t = t.replace('{{PET_T}}', html.escape(pet_t)).replace('{{PET_B}}', pet_b)
t = t.replace('{{ASS_T}}', html.escape(ass_t)).replace('{{ASS_B}}', ass_b)

# acessibilidade: setas decorativas escondidas do leitor de tela e aviso de nova aba
def acessivel(html_txt):
    partes = re.split(r'(<script[\s\S]*?</script>|<style[\s\S]*?</style>|<[^>]+>)', html_txt)
    for k, p in enumerate(partes):
        if p and not p.startswith('<'):
            partes[k] = re.sub(r'\s*[→←↗⇄]', lambda m: '<span aria-hidden="true">' + m.group(0) + '</span>', p)
    html_txt = ''.join(partes)
    html_txt = re.sub(r'(<a\b[^>]*target="_blank"[^>]*>)([\s\S]*?)(</a>)', lambda m: m.group(1) + m.group(2) + ('' if 'abre em nova aba' in m.group(2) else '<span class="sr"> (abre em nova aba)</span>') + m.group(3), html_txt)
    return html_txt
# convite para conversar no fim de cada case, antes de "Próximo projeto"
assert t.count('  <nav class="proximo"') == 5
t = t.replace('  <nav class="proximo"', resumos.CONVITE + '  <nav class="proximo"')
assert t.count('/* imagens dos cases */') == 1
t = t.replace('/* imagens dos cases */', resumos.CSS + resumos.CSS_TOM + '/* imagens dos cases */')
assert t.count('<section class="converse"><div class="wrap">') == 1
t = t.replace('<section class="converse"><div class="wrap">', '<section class="converse" id="tom-prototipo" style="scroll-margin-top:80px"><div class="wrap">')
t = t.replace('{{IMG_PET_CAPA}}', b64('pg-home1.jpg')).replace('{{IMG_ASS_CAPA}}', b64('as-inicio.jpg'))
t = acessivel(t)
OUT.parent.mkdir(exist_ok=True)
open(OUT, 'w', encoding='utf-8').write(t)
assert 'class="ph"' not in t, 'sobrou placeholder'
print('ok', len(t))
