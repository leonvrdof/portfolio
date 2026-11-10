# Resumo no topo de cada case (auditoria RCD, item 4) e convite para conversar no fim (item 5).
# O resumo só junta o que já está escrito no case; nada do conteúdo original é removido.

def _resumo(id_, frase, ficha, numeros, links=''):
    dl = ''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in ficha)
    lk = f'\n  <p class="resumo-links">{links}</p>' if links else ''
    return f'''<section class="resumo largo" aria-labelledby="{id_}">
  <h2 class="ch" id="{id_}">Resumo</h2>
  <p class="resumo-frase">{frase}</p>
  <dl class="pg-ficha">{dl}</dl>
  <p class="resumo-num"><strong>Em números:</strong> {numeros}</p>{lk}
</section>
'''

FIG_LIA = 'https://www.figma.com/design/iS4Jq0wyODvgVXuYrSGNNh/Fluxo-Conversacional---Assistente-viagens?node-id=249-3258&amp;t=ekY5Blnh5QaFz3Wc-1'
FIG_DRO = 'https://www.figma.com/design/TVb5pWH3tjjAR1mfWDVTxu/Drogaria-Popular?node-id=0-1'

LIA = _resumo('resumo-lia',
    'Projetei a Lia, assistente de viagens no WhatsApp para pessoas com 50 anos ou mais. Ela guia o planejamento passo a passo, da escolha do destino ao checklist final.',
    [('Contexto', 'Bootcamp DCIA da Blip, 2025, com mentoria individual'),
     ('Meu papel', 'Conversation designer, da entrevista ao protótipo'),
     ('Canais', 'WhatsApp e BlipChat'),
     ('Modelo', 'Híbrido: menu guiado e IA em momentos específicos')],
    '1 entrevista guiada, fluxo feliz em 4 etapas principais, jornada detalhada em 10 etapas e fluxo revisado depois da validação com a entrevistada.',
    f'<a href="#lia-prototipo" data-scroll="1">Conversar com a Lia</a><a target="_blank" rel="noopener" href="{FIG_LIA}">Acessar os fluxos no Figma</a>')

DRO = _resumo('resumo-drogaria',
    'Desenhei o fluxo de um chatbot no WhatsApp para a Drogaria Popular. Ele confere se a pessoa tem cadastro e responde às dúvidas frequentes, sem IA.',
    [('Formato', 'Desafio de design'),
     ('Meu papel', 'Conversation designer e UX Writer'),
     ('Método', 'Double Diamond'),
     ('Ferramentas', 'Figma e Hemingway App')],
    'fluxo em 4 etapas (boas-vindas, validação do cadastro, dúvidas frequentes e finalização) e nenhuma resposta gerada por IA.',
    f'<a target="_blank" rel="noopener" href="{FIG_DRO}">Acessar o fluxo no Figma</a>')

PET = _resumo('resumo-petgram',
    'Em grupo, criamos o Petgram, um app para tutores trocarem histórias e dicas de cuidado com cães e gatos, da pesquisa ao teste de usabilidade.',
    [('Contexto', 'Curso de UX/UI Design, Cubos Academy'),
     ('Meu papel', 'Gestor do projeto, da pesquisa ao teste'),
     ('Formato', 'Projeto em grupo, com 3 designers')],
    'questionário com 58 pessoas, 6 entrevistas e teste no Maze com 15 pessoas e 3 tarefas.')

ASS = _resumo('resumo-assai',
    'Redesenhei o app do Assaí Atacadista para a compra acontecer dentro dele, com retirada na loja, sem depender do iFood e da Rappi.',
    [('Formato', 'Projeto individual'),
     ('Meu papel', 'UX/UI designer, da análise ao UI'),
     ('Plataforma', 'App Android e iOS')],
    '4 frustrações recorrentes nas avaliações de 1 estrela, benchmark com 3 concorrentes, 8 telas em wireframe e 4 telas finais.')

# frase da Drogaria: era um desafio, não um cliente; o texto não deve dizer que a farmácia contratou
DRO_DESAFIO = ('<p>A farmácia Drogaria Popular nos contratou para criar um chatbot no WhatsApp para atender seus clientes.</p>',
               '<p>O desafio: criar um chatbot no WhatsApp para atender os clientes da Drogaria Popular, uma farmácia.</p>')

CONVITE = '''  <section class="convite" aria-label="Contato">
    <div class="wrap">
      <h2>Gostou deste projeto?</h2>
      <p>Tem uma vaga ou um projeto de design conversacional? Me chama.</p>
      <div class="acoes"><a class="btn cheio" href="mailto:leonvrdof@gmail.com">Enviar e-mail</a><a class="btn vazio" href="https://www.linkedin.com/in/leonvrdof" target="_blank" rel="noopener">LinkedIn</a><a class="btn vazio" href="https://leonvrdof.vercel.app/curriculo.pdf" target="_blank" rel="noopener">Currículo (PDF)</a></div>
    </div>
  </section>
'''

CSS = '''/* resumo no topo dos cases e convite no fim (auditoria RCD, itens 4 e 5) */
.resumo{background:var(--papel);border-radius:var(--raio-g);padding:28px;display:flex;flex-direction:column;gap:16px;margin:0 0 24px}
.case-corpo .resumo h2.ch{margin:0}
.resumo p{margin:0}
.resumo-frase{font-size:1.125rem;color:var(--tinta)}
.resumo .pg-ficha{padding:0;margin:0;background:none;border-radius:0}
.resumo-links{display:flex;flex-wrap:wrap;gap:12px 24px}
.resumo-links a{display:inline-flex;align-items:center;min-height:44px;font-weight:600}
.convite{border-top:1px solid var(--linha)}
.convite .wrap{padding-block:56px;display:flex;flex-direction:column;gap:16px}
.convite h2{margin:0;font-size:clamp(1.6rem,3vw,2.2rem)}
.convite p{margin:0}
.convite .acoes{display:flex;flex-wrap:wrap;gap:12px;margin-top:8px}
@media (max-width:600px){.resumo{padding:20px}.convite .acoes .btn{flex:1 1 100%;justify-content:center}}
'''


# ---------- Tom: mesmo resumo em caixa dos outros cases e visuais feitos só com o que o case já diz ----------
FIG_TOM = 'https://www.figma.com/design/CJn2oRnApcGtfmjt3jlMvd/Chatbot---Cl%C3%ADnica-veterin%C3%A1ria-Vila-Matilde?node-id=6-915'

TOM = _resumo('resumo-tom',
    'Projetei o Tom, assistente virtual da Clínica Veterinária Vila Matilde no WhatsApp, para tirar do telefone as dúvidas simples e os agendamentos que hoje interrompem a equipe durante os atendimentos.',
    [('Formato', 'Projeto individual'),
     ('Meu papel', 'Conversation designer, do começo ao fim: pesquisa, persona, fluxos, conteúdo e documentação'),
     ('Canal', 'WhatsApp'),
     ('Ferramentas', 'Figma e Claude')],
    '12 skills no fluxo micro, 47 termos travados no Glossário, 50 regras de conteúdo numeradas e 88 decisões registradas com o motivo de cada uma.',
    f'<a href="#tom-prototipo" data-scroll="1">Conversar com o Tom</a><a target="_blank" rel="noopener" href="{FIG_TOM}">Acessar o fluxo completo no Figma</a>')

TOM_DADOS = '''<ul class="dados largo" aria-label="Dados da pesquisa Opinion Box, junho de 2025">
  <li><strong>82%</strong><span>dos usuários já falaram com empresas pelo WhatsApp</span></li>
  <li><strong>75%</strong><span>deles usaram o app para tirar dúvidas</span></li>
  <li class="alerta"><strong>59%</strong><span>não gostam de respostas automáticas</span></li>
</ul>
'''

TOM_DOC = '''<div class="doc largo">
  <p class="doc-t">A documentação da V2, em números</p>
  <ul>
    <li><strong>12</strong><span>skills no fluxo micro</span></li>
    <li><strong>47</strong><span>termos travados no Glossário</span></li>
    <li><strong>50</strong><span>regras de conteúdo numeradas</span></li>
    <li><strong>88</strong><span>decisões registradas, com o motivo</span></li>
  </ul>
</div>
'''

TOM_DECISOES = '''<ul class="principios decisoes largo">
  <li><strong>Pedir o mínimo de dados</strong><span>O tutor é identificado pelo BSUID, o novo ID do WhatsApp, e o CPF só é pedido se for preciso.</span></li>
  <li><strong>Cadastro dentro da conversa</strong><span>Quem ainda não é cliente se cadastra com o Tom, sem esperar a equipe.</span></li>
  <li><strong>Palavras acessíveis</strong><span>Uma ação, um nome: “agendar” em todo o fluxo e “Selecione” no lugar de “Toque”.</span></li>
  <li><strong>Saúde com limite</strong><span>O Tom dá só orientação geral. Em emergência, passa o telefone da clínica e chama a equipe na hora.</span></li>
  <li><strong>Confirmar antes de agendar</strong><span>O tutor escolhe entre os horários livres e confere um resumo com o valor.</span></li>
</ul>
'''

TOM_V1V2 = '''<div class="v1v2 largo">
  <figure><figcaption>Antes, V1</figcaption><p class="bolha">Toque em ‘Acessar menu’ e selecione uma das opções.</p><span class="nota">Começa com uma ordem e usa “Toque”, que não serve para quem usa leitor de tela ou teclado.</span></figure>
  <figure class="depois"><figcaption>Depois, V2</figcaption><p class="bolha">Como posso te ajudar hoje? Selecione ‘Acessar menu’ para ver as opções.</p><span class="nota">Abre a conversa com uma pergunta e usa “Selecione”, que vale para qualquer forma de acesso.</span></figure>
</div>
'''

CSS_TOM = '''/* Tom: dados, documentação, decisões e antes e depois */
.case-corpo .dados{list-style:none;padding:0;margin:8px 0 0;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,200px),1fr));gap:16px}
.dados li{background:var(--papel);border-radius:var(--raio-m);padding:24px;display:flex;flex-direction:column;gap:4px}
.dados strong{color:var(--tinta);font-family:var(--titulo);font-size:clamp(2.6rem,5vw,3.6rem);line-height:1}
.dados li.alerta strong{color:var(--vermelho)}
.dados span{color:var(--texto)}
.doc{background:var(--tinta);color:var(--ceu);border-radius:var(--raio-g);padding:28px;display:flex;flex-direction:column;gap:16px;margin-block:8px}
.case-corpo .doc p.doc-t{margin:0;font-weight:600;color:var(--ceu)}
.case-corpo .doc ul{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,120px),1fr));gap:20px}
.doc li{display:flex;flex-direction:column;gap:4px}
.doc strong{font-family:var(--titulo);font-size:clamp(2.6rem,5vw,3.6rem);line-height:1}
.case-corpo .doc li,.case-corpo .doc strong{color:var(--ceu)}
.case-corpo .doc span{color:color-mix(in srgb,var(--ceu) 82%,var(--tinta))}
.case-corpo .decisoes{list-style:none;padding:0;margin:8px 0 0;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));gap:20px}
.decisoes li strong{color:var(--tinta);font-size:19px;line-height:1.3}
.decisoes li span{font-size:16px}
.decisoes li{background:var(--papel);border-radius:28px;padding:28px;display:flex;flex-direction:column;gap:8px}
.v1v2{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,280px),1fr));gap:16px;margin-top:8px}
.v1v2 figure{margin:0;background:#EFEAE2;border:1px solid #8A8478;border-radius:var(--raio-m);padding:20px;display:flex;flex-direction:column;gap:12px;color:#121212}
.v1v2 figcaption{font-weight:700;font-size:14px}
.v1v2 .depois figcaption{color:#0B6B3A}
.v1v2 figure:not(.depois) figcaption{color:#A10D25}
.case-corpo .v1v2 .bolha{color:#121212;margin:0;align-self:flex-start;max-width:92%;background:#fff;border-radius:4px 12px 12px 12px;padding:12px 14px;font-family:system-ui,-apple-system,"Segoe UI",sans-serif;font-size:16px;line-height:1.4;border:1px solid #8A8478}
.case-corpo .v1v2 .nota{font-size:14px;color:#3B3B3B}
/* escuro: cartão e balão com borda de pelo menos 3:1, para a forma não sumir no fundo */
html[data-tema="escuro"] .v1v2 figure{background:#1B2228;border-color:#6B7780;color:#E9EDEF}
html[data-tema="escuro"] .case-corpo .v1v2 .bolha{background:#33424C;border-color:#6B7780;color:#E9EDEF}
html[data-tema="escuro"] .case-corpo .v1v2 .nota{color:#C9D1D6}
html[data-tema="escuro"] .v1v2 .depois figcaption{color:#5FD08F}
html[data-tema="escuro"] .v1v2 figure:not(.depois) figcaption{color:#FF8A9A}
'''
