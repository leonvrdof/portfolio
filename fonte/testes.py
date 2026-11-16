# Resultados dos testes de usabilidade (rodada de 10 a 27/11/2026), com os números de 10 a 15/11.
# Fonte: relatórios "Lia: resultados do primeiro teste de usabilidade" e "Tom: resultados do primeiro teste
# de usabilidade" (docs de 15/11/2026), mais o MVP 1.1 da Lia (10/11). O teste segue aberto: ao atualizar,
# troque os números aqui e em RODADA.

RODADA = 'De 10 a 15/11/2026'


def _metas(linhas, rotulo):
    corpo = ''.join(
        f'<tr><th scope="row">{m}</th><td>{meta}</td><td>{res}</td><td><span class="sit {cls}">{sit}</span></td></tr>'
        for m, meta, res, sit, cls in linhas)
    return (f'<div class="metas largo" role="region" aria-label="{rotulo}" tabindex="0"><table>'
            f'<caption>{rotulo}</caption>'
            '<thead><tr><th scope="col">Métrica</th><th scope="col">Meta</th><th scope="col">Resultado</th><th scope="col">Situação</th></tr></thead>'
            f'<tbody>{corpo}</tbody></table></div>\n')


def _metas2(linhas, rotulo):
    corpo = ''.join(
        f'<tr><th scope="row">{m}</th><td>{meta}</td><td>{todos}</td><td>{mais50}</td><td><span class="sit ok">{sit}</span></td></tr>'
        for m, meta, todos, mais50, sit in linhas)
    return (f'<div class="metas largo" role="region" aria-label="{rotulo}" tabindex="0"><table>'
            f'<caption>{rotulo}</caption>'
            '<thead><tr><th scope="col">Métrica</th><th scope="col">Meta</th><th scope="col">Todos (8)</th>'
            '<th scope="col">50 anos ou mais (3)</th><th scope="col">Situação</th></tr></thead>'
            f'<tbody>{corpo}</tbody></table></div>\n')


def _mudancas(itens):
    li = ''.join(
        f'<li><strong>{titulo}</strong>'
        f'<p><b>Por quê:</b> {porque}</p><p><b>O que mudou:</b> {mudou}</p><p><b>Resultado:</b> {res}</p></li>'
        for data, titulo, porque, mudou, res in itens)
    return f'<ol class="mudancas largo">{li}</ol>\n'


def _dados(itens, rotulo):
    li = ''.join(('<li class="alerta">' if alerta else '<li>') + f'<strong>{n}</strong><span>{t}</span></li>' for n, t, alerta in itens)
    return f'<ul class="dados largo" aria-label="{rotulo}">{li}</ul>\n'


BATIDA, NAO, BASE = ('Batida', 'ok'), ('Não batida', 'nao'), ('Linha de base', 'base')

LIA = (
    '<h2 class="ch">Teste de usabilidade</h2>\n'
    '<p>8 pessoas testaram o MVP com uma tarefa: escolher o destino de uma viagem com a ajuda da Lia. '
    'O teste continua aberto, e estes números são atualizados até o fim da rodada.</p>\n'
    '<p>A Lia é aberta a todo mundo, mas foi desenhada pensando em quem tem 50 anos ou mais. Por isso, além do resultado geral, '
    'separei o das 3 pessoas desse grupo.</p>\n'
    + _dados([
        ('87,5%', 'escolheram o destino que queriam (7 de 8; meta de 80%)', False),
        ('5,0', 'de facilidade média, de 1 a 5 (7 notas; meta de 4)', False),
        ('3 de 3', 'pessoas com 50 anos ou mais escolheram o destino que queriam, todas com nota 5', False),
    ], 'Principais números do teste da Lia')
    + '<h3>Métricas e metas</h3>\n'
    + _metas2([
        ('Escolheram o destino que queriam', '80% ou mais', '87,5% (7 de 8)', '100% (3 de 3)', 'Batida nos dois'),
        ('Facilidade média (1 a 5)', '4 ou mais', '5,0 (7 notas)', '5,0 (3 notas)', 'Batida nos dois'),
        ('Notas 4 e 5 de facilidade', '80% ou mais', '100% (7 de 7)', '100% (3 de 3)', 'Batida nos dois'),
    ], 'Métricas do teste da Lia contra as metas, para todos e para quem tem 50 anos ou mais')
    + '<p>Duas métricas viraram linha de base para os próximos testes: 8 mensagens não entendidas no total (1 por sessão) '
    'e mediana de 5 min 25 s até confirmar a viagem.</p>\n'
    + '<p>As 3 pessoas com 50 anos ou mais conseguiram usar a Lia sozinhas. Uma delas escreveu “4 adultos e 1 criança”, '
    'a Lia entendeu 4, e ela corrigiu pelo botão “Corrigir informações”. Outra mandou uma foto e tocou num botão antigo, '
    'e a Lia trouxe a conversa de volta. Com 3 pessoas, é um bom sinal, mas ainda não é uma conclusão.</p>\n'
    + '<p>As 8 conversas terminaram com a viagem confirmada, mas uma conta como falha: a pessoa pediu sugestões '
    '“para o Natal e Ano Novo” e a Lia entendeu a cidade de Natal.</p>\n'
    + '<h3>O que mudei, e por quê</h3>\n'
    + '<p>Corrigi cada problema assim que ele apareceu, com o teste rodando.</p>\n'
    + _mudancas([
        ('10/11', 'Dicas de passeios no fim da conversa',
         'um designer conversacional confirmou a viagem para Natal, respondeu “Sim” em “Posso te ajudar com mais alguma coisa?” '
         'esperando sugestões para essa viagem, e a Lia voltou para a escolha do destino.',
         'o Sim e o Não viraram três opções: “Dicas de passeios”, “Planejar nova viagem” e “Não, obrigado”. É o MVP 1.1.',
         'quem quer outra viagem diz isso com um botão, e quem quer sugestões recebe passeios do destino escolhido.'),
        ('12/11', 'Cidade no lugar do país',
         'uma pessoa digitou “Bolívia”, e a Lia respondeu que não encontrou o destino.',
         'a pergunta pede a cidade, com um exemplo, e quem digita um país recebe as cidades daquele país para escolher.',
         'nenhum participante depois digitou só o país.'),
        ('12/11', 'Soma de pessoas',
         'uma participante escreveu “4 adultos e 1 criança”, a Lia entendeu 4, e ela precisou corrigir.',
         'a Lia soma os grupos (“4 adultos e 1 criança” vira 5) e ignora idades, como em “filho de 8 anos”.',
         'passou nos 23 casos de teste, e ninguém depois precisou corrigir o número de pessoas.'),
    ])
    + '<p>Com poucas sessões depois das correções, não dá para falar em melhora estatística. O que o teste mostra é o ciclo: '
    'um problema visto numa conversa real, a correção logo em seguida e as conversas seguintes sem ele.</p>\n'
    + '<h3>O que ainda falta</h3>\n'
    + '<ul>'
    '<li>Reconhecer o pedido antes de ler um dado: “Quero sugestões” digitado na pergunta da cidade e o feriado de Natal lido como a cidade.</li>'
    '<li>Não encerrar a conversa por um “não” no meio de uma frase longa.</li>'
    '<li>Testar com mais pessoas de 50 anos ou mais, para o resultado desse grupo ganhar peso.</li>'
    '</ul>\n'
)

TOM = (
    '<p>Coloquei o Tom em teste de usabilidade com 8 pessoas e uma tarefa: agendar uma consulta para o pet '
    'pelo WhatsApp, sem ligar para a clínica. O teste continua aberto, e estes números são atualizados até o fim da rodada.</p>\n'
    + _dados([
        ('8 de 8', 'agendaram a consulta sozinhas (meta de 80%)', False),
        ('0%', 'precisaram da equipe (meta de 20% ou menos)', False),
        ('100%', 'de notas 4 e 5 na satisfação (6 notas; meta de 80%)', False),
        ('2:47', 'minutos da primeira mensagem até a consulta confirmada (mediana)', False),
    ], 'Principais números do teste do Tom')
    + '<h3>Métricas e metas</h3>\n'
    + _metas([
        ('Agendaram sem ajuda', '80% ou mais', '100% (8 de 8)', *BATIDA),
        ('Satisfação: notas 4 e 5 (CSAT)', '80% ou mais', '100% (6 de 6)', *BATIDA),
        ('Precisaram da equipe', '20% ou menos', '0% (0 de 8)', *BATIDA),
        ('Mensagens não entendidas', 'Medir', '8 no total, em 3 sessões', *BASE),
        ('Tempo de uso', 'Medir', 'Mediana de 3 min 15 s', *BASE),
    ], 'Métricas do teste do Tom contra as metas')
    + '<h3>O que mudei, e por quê</h3>\n'
    + '<p>O primeiro teste já mudou o fluxo. As mudanças entraram antes dos outros 7 participantes.</p>\n'
    + _mudancas([
        ('12/11', 'Minhas consultas',
         'um designer conversacional agendou, voltou para agendar de novo, e o Tom começou outro agendamento sem mostrar a consulta marcada.',
         'ao agendar, o Tom mostra a consulta já marcada, com Reagendar, Cancelar consulta e Nova consulta. Também virou item do menu.',
         'resolve o caso do primeiro teste. Ainda falta alguém que volte para remarcar.'),
        ('12/11', 'Trocar pet e Outro pet',
         'no mesmo teste, faltava um jeito de agendar para outro pet sem recomeçar a conversa.',
         'o resumo da consulta ganhou Trocar pet, e a escolha do pet sempre mostra Outro pet, mesmo com um pet cadastrado.',
         'os 7 participantes seguintes escolheram o pet sem erro. O custo foi um toque a mais.'),
    ])
    + '<h3>O que ainda falta</h3>\n'
    + '<ul>'
    '<li>Reconhecer pedidos escritos, como “gostaria de agendar uma consulta para meu pet” no menu, antes de responder que não entendeu.</li>'
    '<li>Oferecer horários à tarde na lista de horários livres: uma pessoa pediu a tarde, e a lista só tinha a manhã.</li>'
    '<li>Proteger o CPF também quando a pessoa digita com espaços: o teste encontrou um caso que passou sem máscara pelo registro.</li>'
    '<li>Testar as funções de quem volta, como remarcar e trocar de pet.</li>'
    '</ul>\n'
)

# Aprendizados do Tom: o teste com tutores aconteceu, então o próximo passo muda
TOM_APRENDIZADOS = ('Os próximos passos são testar o fluxo com tutores reais e desenhar o lembrete de consulta.',
                    'O teste confirmou o caminho principal. Os próximos passos são ensinar o Tom a reconhecer pedidos escritos e desenhar o lembrete de consulta.')

CSS = '''/* testes de usabilidade: tabela de metas e cartões de mudança */
.case-corpo h3{font-family:var(--titulo);color:var(--tinta);font-size:clamp(1.25rem,2.4vw,1.5rem);line-height:1.25;margin:16px 0 0}
.metas{overflow-x:auto;margin-top:8px;border-radius:var(--raio-m);border:1px solid color-mix(in srgb,var(--texto) 30%,transparent)}
.metas:focus-visible{outline:3px solid var(--tinta);outline-offset:3px}
.metas table{width:100%;border-collapse:collapse;min-width:560px;font-size:16px}
.metas caption{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.metas th,.metas td{text-align:left;padding:12px 16px;border-bottom:1px solid color-mix(in srgb,var(--texto) 20%,transparent);vertical-align:top;color:var(--texto)}
.metas thead th{background:var(--papel);color:var(--tinta);font-weight:700;font-size:14px}
.metas tbody th{color:var(--tinta);font-weight:600}
.metas tbody tr:last-child th,.metas tbody tr:last-child td{border-bottom:0}
.metas td{font-variant-numeric:tabular-nums}
.sit{display:inline-block;font-size:14px;font-weight:700;padding:2px 10px;border-radius:999px;border:1.5px solid currentColor;white-space:nowrap}
.sit.ok{color:var(--tinta)}
.sit.nao{color:var(--vermelho)}
.sit.base{color:var(--texto);border-style:dashed}
.case-corpo .mudancas{list-style:none;padding:0;margin:8px 0 0;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));gap:20px}
.mudancas li{background:var(--papel);border-radius:28px;padding:28px;display:flex;flex-direction:column;gap:8px}
.mudancas .quando{font-size:14px;font-weight:700;color:var(--texto);letter-spacing:.02em}
.mudancas strong{color:var(--tinta);font-size:19px;line-height:1.3}
.case-corpo .mudancas p{margin:0;font-size:16px}
.mudancas b{color:var(--tinta)}
'''
