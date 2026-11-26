# Resultados dos testes de usabilidade (rodada de 10 a 27/11/2026), com os números de 10 a 15/11.
# Fonte: relatórios "Lia: resultados do primeiro teste de usabilidade" e "Tom: resultados do primeiro teste
# de usabilidade" (docs de 15/11/2026), mais o MVP 1.1 da Lia (10/11). O teste segue aberto: ao atualizar,
# troque os números aqui e em RODADA.

RODADA = 'De 10 a 15/11/2026'


_ICONE = {
    'ok': '<svg aria-hidden="true" viewBox="0 0 16 16" width="14" height="14"><path d="M3 8.5l3 3 7-7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    'nao': '<svg aria-hidden="true" viewBox="0 0 16 16" width="14" height="14"><path d="M4 4l8 8M12 4l-8 8" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>',
}


def _sit(texto, cls='ok'):
    return f'<span class="sit {cls}">{_ICONE[cls]}{texto}</span>'


def _metas(linhas, rotulo):
    corpo = ''.join(
        f'<tr><th scope="row">{m}</th><td>{meta}</td><td>{res}</td><td>{_sit(sit, cls)}</td></tr>'
        for m, meta, res, sit, cls in linhas)
    return (f'<div class="metas largo" role="region" aria-label="{rotulo}" tabindex="0"><table>'
            f'<caption>{rotulo}</caption>'
            '<thead><tr><th scope="col">Métrica</th><th scope="col">Meta</th><th scope="col">Resultado</th><th scope="col">Situação</th></tr></thead>'
            f'<tbody>{corpo}</tbody></table></div>\n')


def _metas2(linhas, rotulo, n_todos=11, n_50=3):
    corpo = ''.join(
        f'<tr><th scope="row">{m}</th><td>{meta}</td><td>{todos}</td><td>{mais50}</td><td>{_sit(sit, cls)}</td></tr>'
        for m, meta, todos, mais50, sit, cls in linhas)
    return (f'<div class="metas largo" role="region" aria-label="{rotulo}" tabindex="0"><table>'
            f'<caption>{rotulo}</caption>'
            f'<thead><tr><th scope="col">Métrica</th><th scope="col">Meta</th><th scope="col">Todos ({n_todos})</th>'
            f'<th scope="col">50 anos ou mais ({n_50})</th><th scope="col">Situação</th></tr></thead>'
            f'<tbody>{corpo}</tbody></table></div>\n')


def _mudancas(itens):
    li = ''.join(
        f'<li><strong>{titulo}</strong>'
        f'<p><b>Por quê:</b> {porque}</p><p><b>O que mudou:</b> {mudou}</p><p><b>Resultado:</b> {res}</p></li>'
        for data, titulo, porque, mudou, res in itens)
    return f'<ol class="mudancas largo">{li}</ol>\n'


def _dados(itens, rotulo):
    # número grande + o que ele quer dizer + a meta ao lado (o número sozinho não diz se é bom)
    li = ''.join(f'<li><strong>{n}</strong><span>{t}</span>{_sit(meta, cls)}</li>' for n, t, meta, cls in itens)
    return f'<ul class="dados resultados largo" aria-label="{rotulo}">{li}</ul>\n'


BATIDA = ('Batida', 'ok')

LIA = (
    '<h2 class="ch">Teste de usabilidade</h2>\n'
    '<p>11 pessoas testaram o MVP com uma tarefa: escolher o destino de uma viagem com a ajuda da Lia. '
    'Como a Lia foi desenhada pensando em quem tem 50 anos ou mais, separei também o resultado desse grupo.</p>\n'
    + _dados([
        ('7 de 11', 'pessoas escolheram o destino que queriam (64%)', 'Meta não batida: 80% ou mais', 'nao'),
        ('5,0', 'de facilidade média, numa escala de 1 a 5, em 7 notas', 'Meta batida: 4 ou mais', 'ok'),
        ('3 de 3', 'pessoas com 50 anos ou mais escolheram o destino que queriam, todas com nota 5', 'Metas batidas nesse grupo', 'ok'),
    ], 'Principais números do teste da Lia')
    + '<p>Das 11 pessoas, 8 confirmaram a viagem, mas uma conta como falha: pediu sugestões “para o Natal e Ano Novo” '
    'e a Lia entendeu a cidade de Natal. As outras 3 pararam no meio: uma não tinha as datas da viagem, '
    'e duas pararam nas perguntas de preferência das sugestões.</p>\n'
    + '<p>Quem confirmou levou 5 min 25 s, na mediana. A nota de facilidade é pedida no fim da conversa, '
    'por isso só quem chegou ao fim deu nota.</p>\n'
    + '<p>As 3 pessoas com 50 anos ou mais usaram a Lia sozinhas, mesmo quando algo saiu do previsto: uma corrigiu o número de pessoas '
    'pelo botão “Corrigir informações”, e outra mandou uma foto e a Lia trouxe a conversa de volta. '
    'Com 3 pessoas, é um bom sinal, mas ainda não é uma conclusão.</p>\n'
    + '<h3>O que mudei, e por quê</h3>\n'
    + '<p>Com poucas sessões, não dá para falar em melhora estatística. O que o teste mostra é o ciclo: '
    'um problema visto numa conversa real e a correção logo em seguida, com o teste rodando.</p>\n'
    + _mudancas([
        ('', 'Dicas de passeios',
         'depois de confirmar a viagem, um participante respondeu “Sim” em “Posso te ajudar com mais alguma coisa?” '
         'esperando dicas, e a Lia voltou para a escolha do destino.',
         'o Sim e o Não viraram “Dicas de passeios”, “Planejar nova viagem” e “Não, obrigado”. É o MVP 1.1.',
         'quem quer dicas recebe passeios do destino escolhido.'),
        ('', 'Cidade no lugar do país',
         'um participante digitou “Bolívia”, e a Lia não encontrou o destino.',
         'quem digita um país recebe as cidades daquele país para escolher.',
         'ninguém depois digitou só o país.'),
        ('', 'Soma de pessoas',
         'uma participante escreveu “4 adultos e 1 criança”, e a Lia entendeu 4.',
         'a Lia soma os grupos e ignora idades, como em “filho de 8 anos”.',
         'passou nos 23 casos de teste, e ninguém depois precisou corrigir.'),
        ('', 'Datas em aberto',
         'uma participante escreveu “não sei ainda” quando a Lia pediu as datas. A Lia só aceitava dia/mês/ano, e a conversa parou.',
         'entrou a opção “Ainda não sei”: a pessoa diz quanto tempo quer ficar e, se souber, o mês, '
         'como na busca flexível do Booking e do Airbnb. É o MVP 1.2.',
         'não ter as datas deixou de travar a conversa. Ninguém passou por esse caminho ainda.'),
    ])
    + '<h3>O que ainda falta</h3>\n'
    + '<ul>'
    '<li>Entender o pedido antes de ler um dado, como “Natal e Ano Novo” lido como a cidade de Natal.</li>'
    '<li>Descobrir por que 2 pessoas pararam nas perguntas de preferência das sugestões.</li>'
    '<li>Não encerrar a conversa por um “não” no meio de uma frase longa.</li>'
    '<li>Testar com mais pessoas de 50 anos ou mais.</li>'
    '</ul>\n'
)

TOM = (
    '<p>Coloquei o Tom em teste de usabilidade com 8 pessoas e uma tarefa: agendar uma consulta para o pet '
    'pelo WhatsApp, sem ligar para a clínica. O teste continua aberto, e estes números são atualizados até o fim da rodada.</p>\n'
    + _dados([
        ('8 de 8', 'pessoas agendaram a consulta sozinhas (100%)', 'Meta batida: 80% ou mais', 'ok'),
        ('0 de 8', 'precisaram da equipe da clínica (0%)', 'Meta batida: 20% ou menos', 'ok'),
        ('6 de 6', 'notas de satisfação foram 4 ou 5 (CSAT de 100%)', 'Meta batida: 80% ou mais', 'ok'),
    ], 'Principais números do teste do Tom')
    + '<h3>Métricas e metas</h3>\n'
    + _metas([
        ('Agendaram sem ajuda', '80% ou mais', '8 de 8 (100%)', *BATIDA),
        ('Satisfação: notas 4 e 5 (CSAT)', '80% ou mais', '6 de 6 (100%)', *BATIDA),
        ('Precisaram da equipe', '20% ou menos', '0 de 8 (0%)', *BATIDA),
    ], 'Métricas do teste do Tom contra as metas')
    + '<p>Da primeira mensagem até a consulta confirmada, a mediana foi de 2 min 47 s. Duas pessoas não deram nota, por isso são 6 notas.</p>\n'
    + '<h3>O que mudei, e por quê</h3>\n'
    + '<p>O primeiro teste já mudou o fluxo: as duas primeiras mudanças entraram antes dos outros 7 participantes.</p>\n'
    + _mudancas([
        ('12/11', 'Minhas consultas',
         'o primeiro participante agendou, voltou para agendar de novo, e o Tom começou outro agendamento sem mostrar a consulta marcada.',
         'ao agendar, o Tom mostra a consulta já marcada, com Reagendar, Cancelar consulta e Nova consulta. Também virou item do menu.',
         'resolve o caso do primeiro teste. Ainda falta alguém que volte para remarcar.'),
        ('12/11', 'Trocar pet e Outro pet',
         'no mesmo teste, faltava um jeito de agendar para outro pet sem recomeçar a conversa.',
         'o resumo da consulta ganhou Trocar pet, e a escolha do pet sempre mostra Outro pet, mesmo com um pet cadastrado.',
         'os 7 participantes seguintes escolheram o pet sem erro. O custo foi um toque a mais.'),
        ('', 'CPF protegido também com espaços',
         'um participante digitou o CPF com um espaço entre os números, e o registro do teste guardou o número inteiro, sem máscara.',
         'a máscara passou a reconhecer o CPF com pontos, traço ou espaços entre os números, no navegador e no servidor. O registro antigo foi corrigido.',
         'nenhum CPF fica inteiro no registro dos testes.'),
    ])
    + '<h3>O que ainda falta</h3>\n'
    + '<ul>'
    '<li>Reconhecer pedidos escritos, como “gostaria de agendar uma consulta para meu pet” no menu, antes de responder que não entendeu.</li>'
    '<li>Oferecer horários à tarde na lista de horários livres: um participante pediu a tarde, e a lista só tinha a manhã.</li>'
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
/* cor de status sempre junto de ícone e texto: verde batida, vermelho não batida (contraste 4.5:1 nos dois temas) */
:root{--ok:#0B6B3A;--ok-fundo:#E3F3EA;--nao:#A10D25;--nao-fundo:#FBE6E9}
html[data-tema="escuro"]{--ok:#6FDB9C;--ok-fundo:#123323;--nao:#FF8A9A;--nao-fundo:#3A1820}
.sit{display:inline-flex;align-items:center;gap:6px;font-size:14px;font-weight:700;line-height:1.3;padding:4px 10px;border-radius:999px;border:1.5px solid currentColor;width:fit-content}
.sit svg{flex:none}
.sit.ok{color:var(--ok);background:var(--ok-fundo)}
.sit.nao{color:var(--nao);background:var(--nao-fundo)}
.case-corpo .resultados li{gap:8px}
.case-corpo .resultados .sit{margin-top:auto}
.case-corpo .mudancas{list-style:none;padding:0;margin:8px 0 0;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));gap:20px}
.mudancas li{background:var(--papel);border-radius:28px;padding:28px;display:flex;flex-direction:column;gap:8px}
.mudancas .quando{font-size:14px;font-weight:700;color:var(--texto);letter-spacing:.02em}
.mudancas strong{color:var(--tinta);font-size:19px;line-height:1.3}
.case-corpo .mudancas p{margin:0;font-size:16px}
.mudancas b{color:var(--tinta)}
'''
