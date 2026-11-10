# Blocos visuais que substituem as imagens dos cases (texto transcrito das imagens do portfólio no Framer)
import base64
from pathlib import Path

IMG = str(Path(__file__).resolve().parent / 'imgs') + '/'

def b64(nome):
    return 'data:image/jpeg;base64,' + base64.b64encode(open(IMG + nome, 'rb').read()).decode()

def lista(itens):
    return '<ul>' + ''.join(f'<li>{i}</li>' for i in itens) + '</ul>'

# ---------- LIA ----------
LIA_EMPATIA = '''
<div class="emp largo" role="group" aria-label="Mapa de empatia da Dona Lígia">
  <p class="emp-centro"><span class="pg-foto" aria-hidden="true">L</span><span><span class="rotulo">Mapa de empatia</span><strong>Dona Lígia</strong></span></p>
  <section><h3>O que pensa e sente</h3>''' + lista([
    'Sente muita vontade de viajar e pensa nisso com frequência ("toda semana").',
    'Tem medo de errar em processos importantes (passagens, hotel, aeroporto).',
    'Se sente insegura por não saber planejar uma viagem sozinha.',
    'Pensa que o tempo está passando e que está envelhecendo, o que aumenta a urgência de viajar.']) + '''</section>
  <section><h3>O que ouve</h3>''' + lista([
    'Comentários e convites das amigas do bordado que viajam com frequência.',
    'Recomendações de pessoas próximas que já viajam bastante.',
    'A ideia de que agência de viagem é mais segura e confiável.']) + '''</section>
  <section><h3>O que vê</h3>''' + lista([
    'Vídeos no YouTube mostrando paisagens, destinos e lugares bonitos.',
    'Conteúdos de promoções e anúncios de viagens no celular.',
    'Vê pessoas próximas viajando (amigas e conhecidos), o que aumenta a vontade.']) + '''</section>
  <section><h3>O que faz e fala</h3>''' + lista([
    'Fala frequentemente sobre vontade de viajar, mas não coloca em prática.',
    'Evita viajar sozinha ou sem o marido, mesmo quando é convidada pelas amigas.',
    'Pede ajuda para pessoas próximas e confia em quem tem experiência.']) + '''</section>
</div>
'''

LIA_PERSONA = '''
<article class="pg-persona largo" aria-label="Persona Lígia Terriaga">
  <div class="pg-quem">
    <div class="pg-foto" aria-hidden="true">L</div>
    <div><h3>Lígia Terriaga</h3><p>66 anos · aposentada · São Paulo</p></div>
  </div>
  <p>Dona Lígia tem 66 anos, mora em São Paulo e é aposentada. Ela sonha em viajar, mas se sente insegura por não saber planejar uma viagem sozinha, principalmente na compra de passagens, escolha de hotel e processos do aeroporto. Além disso, a rotina de trabalho do marido influencia diretamente suas decisões, fazendo com que ela adie viagens com frequência. Por depender de outras pessoas para se sentir segura e por não conseguir colocar seus planos em prática, ela acaba acumulando frustração e ansiedade, com a sensação de que o tempo está passando e ela não está aproveitando como gostaria.</p>
  <blockquote><p>"Quero aproveitar a vida e viajar enquanto ainda tenho saúde, mas preciso de confiança para não me perder e não errar no caminho."</p></blockquote>
  <div class="pg-colunas">
    <section><h4>Objetivos</h4>''' + lista([
    'Viajar mais vezes e conhecer novos lugares enquanto ainda tem saúde e disposição.',
    'Ter confiança para planejar a viagem com autonomia, sem depender de outras pessoas.',
    'Escolher destinos e hospedagens com segurança, sabendo o que vale a pena.',
    'Sentir-se preparada para o aeroporto, sabendo exatamente o que fazer em cada etapa.']) + '''</section>
    <section><h4>Dores</h4>''' + lista([
    'Insegurança para planejar uma viagem sozinha (passagem, hotel, destino).',
    'Medo do aeroporto e do processo de embarque (check-in, portão, procedimentos).',
    'Dificuldade em escolher o destino certo, por não saber o que esperar do lugar.',
    'Frustração e ansiedade por adiar viagens, sentindo que o tempo está passando e ela não está aproveitando a vida.']) + '''</section>
  </div>
</article>
'''

LIA_FLUXO_FELIZ = '''<ol class="as-flow largo" aria-label="As quatro etapas principais do fluxo feliz">
<li><strong>Escolher o destino ideal</strong></li>
<li><strong>Comprar a passagem</strong><span>e receber orientação passo a passo sobre o aeroporto</span></li>
<li><strong>Reservar a hospedagem</strong><span>com segurança</span></li>
<li class="fim"><strong>Receber dicas</strong><span>de pontos turísticos e atividades no destino escolhido</span></li>
</ol>'''

_ETAPAS = [
    ('Escolher o destino', [
        'Dona Lígia inicia a conversa com o chatbot no WhatsApp.',
        'O chatbot apresenta o menu principal e ela escolhe “Planejar uma viagem completa”.',
        'Dona Lígia informa suas preferências (tipo de viagem: frio/calor, praia/interior).',
        'Ela define o orçamento e o período desejado para viajar.',
        'O chatbot sugere destinos ideais e Dona Lígia seleciona o destino desejado.']),
    ('Passagem e aeroporto', [
        'O chatbot orienta Dona Lígia a comprar a passagem aérea com segurança (datas, horários e sites confiáveis).',
        'O chatbot explica o passo a passo do aeroporto (check-in, portão de embarque).']),
    ('Hospedagem', [
        'O chatbot orienta Dona Lígia a escolher e reservar uma hospedagem com critérios seguros (localização, avaliações, cancelamento).']),
    ('No destino', [
        'O chatbot envia dicas e pontos turísticos do destino escolhido.']),
    ('Fim da conversa', [
        'Dona Lígia recebe um resumo final com checklist completo da viagem e uma mensagem de confirmação.']),
]

def _jornada():
    n = 1
    partes = ['<div class="jornada largo">']
    for i, (fase, passos) in enumerate(_ETAPAS):
        partes.append(f'<section class="j-fase"><h3><span class="rotulo">Parte {i+1}</span>{fase}</h3><ol start="{n}">')
        for p in passos:
            partes.append(f'<li><span class="j-num" aria-hidden="true">{n:02d}</span><p><span class="sr">Etapa {n}: </span>{p}</p></li>')
            n += 1
        partes.append('</ol></section>')
    partes.append('</div>')
    return ''.join(partes)

LIA_JORNADA = _jornada()

LIA_CANAIS = '<ul class="pg-chips pg-chips-claros canais" aria-label="Canais"><li>BlipChat</li><li>WhatsApp</li></ul>'

# ---------- DROGARIA ----------
DRO_DIAMANTE = '''<ol class="pg-diamante dd largo" aria-label="As quatro fases do Double Diamond">
  <li><em>Diverge</em><strong>Descobrir</strong><span>Quais são e de onde vêm os problemas?</span></li>
  <li><em>Converge</em><strong>Definir</strong><span>Qual o problema devemos focar em resolver?</span></li>
  <li><em>Diverge</em><strong>Desenvolver</strong><span>Quais são as soluções possíveis para o problema?</span></li>
  <li><em>Converge</em><strong>Entregar</strong><span>A nossa solução de fato resolve o problema?</span></li>
</ol>'''

DRO_FLUXO = '''<ol class="as-flow largo" aria-label="Definição do fluxo conversacional">
<li><strong>Onboarding</strong></li><li><strong>Validação cadastral</strong></li><li><strong>FAQ</strong></li><li class="fim"><strong>Finalização</strong></li>
</ol>'''

def _ramo(cond, txt):
    return f'<li class="mm-ramo"><b>{cond}</b> {txt}</li>'

DRO_MAPA = '''<div class="mm largo" role="group" aria-label="Mapa mental do fluxo, redesenhado a partir do esboço à mão">
  <section><h4><span class="rotulo">01</span>Onboarding</h4><ol>
    <li>Mensagem do usuário</li>
    <li>É o primeiro contato?</li>''' + _ramo('Sim:', 'boas-vindas (“Sou sua assistente virtual e vou te ajudar”), envio da política de privacidade em PDF e pedido de aceite') + _ramo('Não:', '“Olá, seja bem-vindo de volta” e política de privacidade') + '''
    <li>Aceitou a política?</li>''' + _ramo('Sim:', 'validar cadastro') + _ramo('Não:', 'voltar para o fluxo') + '''
  </ol></section>
  <section><h4><span class="rotulo">02</span>Validar cadastro</h4><ol>
    <li>“Agora, preciso saber se você tem cadastro com a gente”</li>
    <li>“Envie seu CPF (somente números)”</li>
    <li>API valida o CPF</li>''' + _ramo('Não encontrou:', '“Como deseja continuar?” Corrigir o CPF ou fazer um novo cadastro') + _ramo('Encontrou:', 'avisa que encontrou e pergunta se deseja continuar. Se não, corrigir o CPF') + '''
  </ol></section>
  <section><h4><span class="rotulo">03</span>FAQ</h4><ol>
    <li>“Selecione o botão para acessar o menu”</li>
    <li>Lista com as opções de dúvidas</li>
  </ol></section>
  <section><h4><span class="rotulo">04</span>Finalização</h4><ol>
    <li>“Te ajudo com algo mais?”</li>''' + _ramo('Sim:', 'voltar para o fluxo') + _ramo('Não:', 'finalizar a conversa') + '''
  </ol></section>
  <section class="mm-exc"><h4>Exceções</h4><ul>
    <li><b>Erro no CPF:</b> “CPF errado, digite novamente”</li>
    <li><b>Erro no telefone:</b> “Telefone errado, digite novamente”</li>
    <li><b>Erro no botão</b></li>
    <li><b>Erro no sim/não</b></li>
  </ul></section>
</div>'''

# ---------- PETGRAM ----------

# ---------- ASSAÍ ----------

# ---------- PETGRAM recriado no padrão do case (substitui as imagens) ----------
_AFIN = [
  ('Incentivos que fizeram ter um pet', None, [
    'Sempre adorei gatos e queria a companhia de um. Pesquisei sobre diferentes raças de gatos, fiquei fascinado por um específico e decidi pegar pra mim',
    'O fato de ter uma conexão com o animal foi determinante',
    'Vi uma amiga minha postando que tinha encontrado na rua, não teve nenhum detalhe em específico, foi mais isso de ter visto a foto e ficar pensando o tempo todo',
    'Minha decisão de ter um pet foi bastante ponderada. Já desde a infância eu era apaixonada por animais e sempre quis tê-los como parte da família',
    'Sim, eu tenho dois filhos, e aí um deles sempre comentava que gostaria de ter animal',
    'O detalhe mais determinante para mim foi a personalidade do pet']),
  ('Adoção e resgate do pet', None, [
    'Eu tenho uma gata, vi uma amiga minha postando que tinha encontrado na rua, e que ela precisava doar',
    'O Loop que é meu cachorro e a Pandora que é minha gata, os dois são adotados',
    'Quando fui adotar o Léo, um gato, ele se aproximou e demonstrou uma simpatia incrível',
    'Só resgatei a coitada no meio da noite']),
  ('Compra do pet', None, [
    'Foi uma benção ter o meu animal do meu lado. E ele foi comprado, tá? Não foi adotado não',
    'Sempre adorei gatos e queria a companhia de um. Pesquisei sobre diferentes raças de gatos, fiquei fascinado por um específico e decidi pegar pra mim, acabei comprando']),
  ('Mudanças comportamentais', 'Bem-estar do pet', [
    'Teve um episódio que eu tava comendo e aí quando eu olhei pra minha gata ela tava babando muito. Eu peguei ela na hora e procurei um veterinário 24 horas',
    'Sim, teve uma vez que ele ficou muito tempo sem comer e não queria mais brincar com ninguém, além de estar bem desanimado',
    'Chegando em casa ele começou a vomitar, e eu percebi que aquilo não estava normal. E no meio do vômito eu encontrei uma borrachinha que foi exatamente aquela que ele tinha comido na casa do meu filho',
    'O Loop, às vezes, pode ser um pouco travesso e roubar algumas comidas, isso acaba o fazendo mal, aí eu percebo logo quando ele fez isso porque ele fica tristinho',
    'Somente no começo quando resgatei ela da rua, ficava sempre encolhida e com medo de interagir mas foi se soltando até sair e brincar normalmente',
    'Houve um episódio em que ele demonstrou comportamento apático e, após consultar o veterinário, percebemos que era uma reação a um novo alimento que tentamos introduzir em sua dieta']),
  ('Quando precisa de itens para o pet', 'Bem-estar do pet', [
    'Compra on-line, quase tudo on-line, porque acaba sendo mais barato e algumas lojas, dessas grandes, tem programas de fidelidade e aí dão desconto, então eu acabo sempre comprando on-line',
    'Compra on-line, a comodidade em primeiro lugar né? Sem dúvida. Muito mais tranquilo. Comprar, depois é só retirar na loja. Muito mais fácil, preço também acessível, é mais acessível do que se eu comprar na loja física',
    'Prefiro comprar online, dá pra pesquisar e comparar produtos com facilidade. Além disso, a entrega em casa é muito melhor',
    'Prefiro fazer compras para o Leo em lojas físicas',
    'Gosto de fazer compras para meus pets em lojas físicas']),
  ('Ida ao veterinário', 'Bem-estar do pet', [
    'A parte da ida até o veterinário é super tranquila',
    'Não pude levar ainda pela falta de dinheiro e alguns problemas em casa',
    'Eu não tenho nenhum problema em levá-lo no veterinário',
    'É tranquilo. Meu gato é bastante calmo, mas sempre tomo cuidado de escolher um veterinário experiente com a raça',
    'Levar meus pets ao veterinário é um quesito que eu peco um pouco, eu os levo para o veterinário apenas para vacinação',
    'Levar o Léo ao veterinário é uma parte importante do cuidado. Ele passa por exames de rotina, vacinações e consultas periódicas']),
  ('Notícias sobre pets', None, [
    'Eu gosto de acompanhar pessoas que fazem conteúdos, mas que são dessa área, tipo, veterinários, assim',
    'Eu gosto de ver bastante, eu faço parte do grupo de Canil, eu acho que isso daí me interage bastante, porque as pessoas dão algumas informações que às vezes eu vejo que são necessárias para mim',
    'Tenho muito interesse em conteúdos relacionados a pets',
    'Sim, gosto de ler sobre cuidados pra raça do meu gato',
    'Sim, qualquer conteúdo informativo que me ajude a cuidar da minha gata melhor',
    'Gosto de assistir vídeos engraçados e também sigo tutores de outros animais para aprender mais sobre cuidados e dicas, como alimentação, coisinhas para o pelo, brinquedos']),
  ('Comunidade para pets', None, [
    'Nunca participei de nada relacionado',
    'Eu participo do próprio grupo do canil onde eu comprei meu cachorro',
    'Sim, já participei de um grupo online de tutores de animais de estimação']),
]

def pet_afinidades():
    p = ['<div class="afin largo" role="group" aria-label="Diagrama de afinidades: falas das entrevistas agrupadas por tema">']
    for i, (tema, grupo, falas) in enumerate(_AFIN):
        tag = f'<span class="rotulo">{grupo}</span>' if grupo else ''
        p.append(f'<section class="afin-g c{i % 4}"><h3>{tag}{tema} <span class="afin-n">{len(falas)} falas</span></h3><ul>')
        p += [f'<li>“{f}”</li>' for f in falas[:2]]
        p.append('</ul>')
        if len(falas) > 2:
            resto = len(falas) - 2
            p.append(f'<details class="afin-mais"><summary>Ler mais {resto} {"fala" if resto == 1 else "falas"}</summary><ul>' + ''.join(f'<li>“{f}”</li>' for f in falas[2:]) + '</ul></details>')
        p.append('</section>')
    p.append('</div>')
    return ''.join(p)

def pet_empatia():
    blocos = [
      ('O que pensa e sente', [
        'Sente um profundo e incondicional amor pela Mel, considerando-a parte integral de sua vida e membro da família.',
        'Sente uma grande responsabilidade e preocupação em prover o melhor cuidado para sua gata.',
        'Vê a Mel como uma fonte constante de alegria e companheirismo na vida cotidiana.',
        'Se preocupa em saber se Mel está segura e se o ambiente tem suprido suas necessidades de estímulos.',
        'Se sente influenciada por tutores de animais experientes que compartilham seus conhecimentos e experiências.',
        'Sente que sua profissão como enfermeira é uma extensão natural do cuidado que ela tem com as pessoas e com a Mel.',
        'Se preocupa em manter uma rotina organizada para conseguir usufruir dos bons momentos com a Mel e a família.',
        'Sonha em proporcionar a Mel uma vida longa, saudável e repleta de felicidade.',
        'Deseja que seus filhos cresçam aprendendo sobre a importância do cuidado e respeito aos animais.']),
      ('O que ouve', [
        '"Deve dar muito trabalho cuidar da sua gata"', '"Muito legal da sua parte ter adotado a Mel"', '"Eles têm um lar tão acolhedor!"',
        '"Por que uma gata?"', '"Gostaria de ter outro animal de estimação?"', '"Ela é muito bem cuidada por você, né?"']),
      ('O que vê', [
        'Outros tutores com as mesmas dúvidas e questionamentos que ela teve quando adotou a Mel.',
        'A importância de ter um ambiente seguro para Mel.',
        'Que sempre está aprendendo algo novo sobre a Mel.',
        'Vê a importância em participar de grupos voltados para os cuidados com os pets.',
        'Blogs e matérias sobre dicas e cuidados com a Mel são seu ponto fraco.',
        'A importância da adoção responsável graças a convivência com a Mel.',
        'Vê a mudança que a adoção proporcionou na vida da Mel e a diferença que isso fez em sua vida.']),
      ('O que fala e faz', [
        'Comenta bastante sobre a preocupação que sente em relação com a saúde e bem-estar da Mel.',
        'Sempre opta por frequentar lojas locais pela possibilidade de examinar os produtos pessoalmente e também de obter conselhos dos atendentes.',
        'Gosta de pesquisar dicas para proporcionar um ambiente mais enriquecedor para a Mel, com brinquedos e atividades estimulantes.',
        'Fala sobre a rotina agitada e que gostaria de passar mais tempo com a Mel e os filhos.',
        'Fala que vai levar Mel mais frequentemente no veterinário mas acaba deixando essa opção de lado devido a rotina agitada e as questões financeiras.',
        'Navega diariamente na internet e gosta de ler notícias e novidades.']),
      ('Dores', [
        'Se preocupa com a segurança de Mel quando ela não está em casa.',
        'Se sente mal quando não consegue conciliar a rotina profissional com a pessoal, principalmente quando não consegue dar atenção a Mel.',
        'Preocupação com o bem-estar da Mel enquanto ela não está em casa.',
        'Frustração em lidar com as mudanças comportamentais da Mel, dúvidas sobre suas reais necessidades.',
        'Preocupação com a alimentação e nutrição adequada da Mel.',
        'Dificuldade em encontrar soluções para problemas de saúde ou comportamento da pet.',
        'Fica aflita em como adaptar a casa para criar um ambiente enriquecido onde a Mel possa se distrair e brincar sempre que quiser.']),
      ('Ganhos', [
        'Saber que existe 100% de garantia que a Mel não irá para a rua enquanto não estiver sob a supervisão de ninguém.',
        'Fortalecimento das relações interpessoais ao compartilhar experiências com outros tutores.',
        'Ela almeja tornar-se uma tutora ainda mais consciente e informada.',
        'Criação de memórias especiais e momentos marcantes com a Mel e sua família.',
        'Conseguir compreender melhor sobre a alimentação da Mel, dando a ela uma ração de qualidade.',
        'Procura atingir um estado de equilíbrio e harmonia em sua vida cotidiana, uma rotina com mais tempo para família e a Mel.',
        'Sensação de plenitude ao cuidar e proporcionar bem-estar ao pet.',
        'Passar a praticar atividades físicas frequentemente e enriquecer o ambiente para manter Mel estimulada.',
        'Contar com o suporte e a compreensão de seu marido e filhos em relação aos cuidados com Mel a tornaria mais segura enquanto está longe.']),
    ]
    p = ['<div class="emp emp-pet largo" role="group" aria-label="Mapa de empatia da Juliana">',
         '<p class="emp-centro"><span class="pg-foto" aria-hidden="true">J</span><span><span class="rotulo">Mapa de empatia</span><strong>Juliana</strong></span></p>']
    for i, (t, itens) in enumerate(blocos):
        cls = ' class="emp-dor"' if t == 'Dores' else (' class="emp-ganho"' if t == 'Ganhos' else '')
        extra = ''
        if len(itens) > 3:
            r = len(itens) - 3
            extra = f'<details class="afin-mais"><summary>Ler mais {r} {"item" if r == 1 else "itens"}</summary>' + lista(itens[3:]) + '</details>'
        p.append(f'<section{cls}><h3>{t}</h3>' + lista(itens[:3]) + extra + '</section>')
    p.append('</div>')
    return ''.join(p)


# ---------- telas no mesmo padrão (Assaí e Petgram) ----------
def telas(itens, rotulo, cols=4):
    """itens: (arquivo, legenda, alt, [(x%, y%, tamanho%), ...] manchas de calor)"""
    p = [f'<ul class="telas largo" style="--cols:{cols}" aria-label="{rotulo}">']
    for arq, leg, alt, calor in itens:
        manchas = ''.join(f'<i style="left:{x}%;top:{y}%;width:{r}%"></i>' for x, y, r in calor)
        camada = f'<span class="calor" aria-hidden="true">{manchas}</span>' if calor else ''
        p.append(f'<li><figure><div class="tela-cel"><img src="{b64(arq)}" alt="{alt}" loading="lazy" decoding="async">{camada}</div><figcaption>{leg}</figcaption></figure></li>')
    p.append('</ul>')
    return ''.join(p)

def assai_ui():
    return telas([
        ('as-inicio.jpg', 'Início', 'Tela inicial: loja de retirada no topo, busca, banner de ofertas, categorias e as principais ofertas do dia, com atalho para a sacola.', []),
        ('as-sacola.jpg', 'Sacola', 'Sacola aberta sobre a tela inicial: lista de produtos com preço e quantidade, e o botão Continuar com o total.', []),
        ('as-checkout.jpg', 'Checkout', 'Checkout: dados da pessoa, loja de retirada, prazo de retirada e resumo do pedido com subtotal, taxa de serviço e total.', []),
        ('as-pagamento.jpg', 'Pagamento', 'Pagamento: escolha entre Pix e cartão de crédito, dados do cartão preenchidos e o botão verde Confirmar e pagar.', []),
    ], 'Quatro telas-chave do app redesenhado') + '<p class="telas-mais">As telas mostram o caminho principal: do início ao pagamento, com retirada na loja.</p>'


def pet_maze():
    T1 = [
      ('pg-home1.jpg', 'Início', 'Feed na aba Início. Os cliques se concentram na foto de perfil da Mel, no topo do post, e na aba Meus pets.', [(14,28,22),(79,20,20),(48,48,14)]),
      ('pg-home3.jpg', 'Meus pets', 'Aba Meus pets. Os cliques se concentram no card da Mel.', [(26,37,34)]),
      ('pg-perfil.jpg', 'Perfil da Mel', 'Perfil da Mel. Os cliques se concentram na linha Vacinas.', [(36,51,24),(58,51,24)]),
      ('pg-vacinas.jpg', 'Vacinas', 'Tela de vacinas vazia. Os cliques se concentram no botão Adicionar vacina.', [(48,50,30)]),
      ('pg-vacina-form.jpg', 'Nova vacina', 'Formulário de vacina. Os cliques se concentram nos campos nome, laboratório e próxima dose, e no botão Adicionar.', [(72,60,16),(72,69,16),(72,78,16),(66,94,24)]),
    ]
    T2 = [
      ('pg-home1.jpg', 'Início', 'Feed na aba Início. Os cliques vão direto ao ícone de Mensagens, na barra de baixo.', [(76,95,22)]),
      ('pg-mensagens.jpg', 'Mensagens', 'Lista de mensagens. Os cliques se concentram na conversa com a Amora, a primeira da lista.', [(22,20,22),(44,20,22),(66,20,20)]),
      ('pg-chat.jpg', 'Conversa', 'Conversa com a Amora aberta. Tarefa concluída.', []),
    ]
    T3 = [
      ('pg-home1.jpg', 'Início', 'Feed na aba Início. Os cliques vão para a aba Dicas e Cuidados.', [(43,20,24)]),
      ('pg-home2.jpg', 'Dicas e Cuidados', 'Aba Dicas e Cuidados. Os cliques se concentram no card de enriquecimento ambiental.', [(40,84,26),(62,84,22)]),
      ('pg-materia.jpg', 'Matéria', 'Matéria sobre enriquecimento ambiental aberta. Tarefa concluída.', []),
    ]
    def bloco(n, titulo, achado, itens):
        return (f'<section class="maze-t"><div class="maze-txt"><span class="rotulo">Tarefa {n}</span><h3>{titulo}</h3><p>{achado}</p></div>'
                + telas(itens, f'Mapas de calor da tarefa {n}', cols=5) + '</section>')
    return ('<div class="maze-tarefas largo">'
      + bloco(1, 'Acesse o perfil da Mel e adicione uma vacina', 'As pessoas estavam "cortando caminho" pela foto de perfil da Mel. <b>Mudança:</b> a foto de perfil também passou a levar ao perfil do pet.', T1)
      + bloco(2, 'Navegue até as mensagens e acesse a conversa com a Amora', '<b>100% de assertividade.</b> Sem alterações.', T2)
      + bloco(3, 'Acesse a matéria sobre enriquecimento ambiental', '<b>Grande acerto.</b> Não foram necessárias alterações.', T3)
      + '<p class="telas-mais">Mapas de calor do teste no Maze, redesenhados sobre as telas atuais do Petgram.</p></div>')
