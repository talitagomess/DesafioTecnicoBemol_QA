Funcionalidade: Busca

Cenário: Busca de Hotel com sucesso

Dado que eu esteja na tela inicial

Quando o campo Hotel|Destino for preenchido com o texto "Manaus"
E clica-se no botão "Pesquisar"
E clicar na opção "Ordenar por" e selecionar “Avaliação e Sugestões"
Então verificar o nome do primeiro da lista com o texto "ibis budget Manaus"
E verificar a avaliação do primeiro da lista com o texto "Muito bom"
E verificar o valor do primeiro da lista com o texto "R$177,00"
