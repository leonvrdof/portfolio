<!--
Case importado do portfólio no Framer, sem alterações no texto.
Fonte: https://leonvrdof.framer.ai/projeto/chatbot-veterinario
Copiado em 28/10/2026. Removidas só as sobras do modelo do Framer.
Ordem no novo portfólio: 2º (destaque)
-->

# Chatbot - Clínica Veterinária Vila Matilde

Resumo do card na home: O assistente que te auxilia 24h do dia.

## Resumo

Projetei o Tom, assistente virtual da Clínica Veterinária Vila Matilde no WhatsApp, para tirar do telefone as dúvidas simples e os agendamentos que hoje interrompem a equipe durante os atendimentos.

- Meu papel: conversation designer, do começo ao fim (pesquisa, persona, fluxos, conteúdo e documentação).
- Canal: WhatsApp.
- Ferramentas: Figma e Claude.
- Em números: 12 skills no fluxo micro, 47 termos travados no Glossário, 50 regras de conteúdo numeradas e 88 decisões registradas com o motivo de cada uma.

[Acessar o fluxo completo no Figma](https://www.figma.com/design/CJn2oRnApcGtfmjt3jlMvd/Chatbot---Cl%C3%ADnica-veterin%C3%A1ria-Vila-Matilde?node-id=6-915)

[Testar o MVP do Tom](https://tom-prototipo-de-testes.vercel.app/)

## Situação

Na Clínica Veterinária Vila Matilde, quem atende o telefone é a mesma pessoa que está cuidando de um pet. Com 38 anos de história e atendimento só por ligação, a veterinária ou a assistente interrompe a consulta para responder dúvidas simples, como valor, horário e endereço. Fora do expediente, o tutor fica sem resposta.

O WhatsApp é o canal certo: 82% dos usuários já falaram com empresas pelo aplicativo, 75% deles para tirar dúvidas. Mas 59% não gostam de respostas automáticas ([Opinion Box, junho de 2025](https://canaltech.com.br/apps/o-que-os-brasileiros-mais-fazem-no-whatsapp-segundo-pesquisa/)).

## Tarefa

Projetar, sozinho, um assistente no WhatsApp que resolva dúvidas e agendamentos sem interromper a equipe e que chame uma pessoa quando for preciso. O desafio incluía os limites de botões do WhatsApp, a LGPD e a regra do Conselho Federal de Medicina Veterinária, que impede diagnóstico pelo chat.

## Ação

Minha primeira versão (V1) foi feita sem regras escritas, e o fluxo ficou inconsistente. Na V2, criei a documentação do projeto (Glossário, Guidelines, registro de Decisões e System prompt) e revisei o fluxo inteiro com o Claude: ele comparava cada mensagem com as regras e propunha correções, e eu decidia o que entrava.

As decisões que mais mudaram a conversa:

- Pedir o mínimo de dados. O tutor é identificado pelo BSUID, o novo ID do WhatsApp, e o CPF só é pedido se for preciso.
- Cadastro dentro da conversa. Quem ainda não é cliente se cadastra com o Tom, sem esperar a equipe.
- Palavras acessíveis. Uma ação, um nome: “agendar” em todo o fluxo e “Selecione” no lugar de “Toque”.
- Saúde com limite. O Tom dá só orientação geral. Em emergência, passa o telefone da clínica e chama a equipe na hora.
- Confirmar antes de agendar. O tutor escolhe entre os horários livres e confere um resumo com o valor.

V1: “Toque em ‘Acessar menu’ e selecione uma das opções.”

V2: “Como posso te ajudar hoje? Selecione ‘Acessar menu’ para ver as opções.”

## Resultado

O Tom cobre a jornada do tutor de ponta a ponta e só chama a equipe quando o sistema falha ou há emergência. Simulei o caminho de um tutor novo, do cadastro ao pedido de receita, e corrigi os 4 problemas de experiência que apareceram.

Quando o Tom estiver no ar, vou medir a satisfação dos tutores, os agendamentos concluídos sem a equipe e a queda nas ligações para a clínica.

## Aprendizados

Consistência em conversa não se mantém de cabeça: precisa de registro. Com a documentação, cada texto novo segue as mesmas regras, seja escrito por mim ou pela IA. Os próximos passos são testar o fluxo com tutores reais e desenhar o lembrete de consulta.

---

## Imagens do case
- A página no Framer não tem imagens do projeto, só o link do Figma. Vale exportar 2 ou 3 telas do fluxo do Figma para assets/img/clinica/.

## Protótipo dentro do case (instrução para o site)
- Adicionar a seção "Converse com o Tom" no fim do case, com o protótipo https://tom-prototipo-de-testes.vercel.app/?modo=vitrine
- Detalhes em assets/prototipos-no-portfolio.md
