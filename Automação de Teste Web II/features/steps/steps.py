from behave import given, when, then
from selenium.webdriver import Safari


@given(u'que eu esteja na tela inicial')
def go_to_page(context):
    ...

@when(u'o campo Hotel|Destino for preenchido com o texto "Manaus"')
def fill_location(context):
    ...

@when(u'clica-se no botão "Pesquisar"')
def click_search(context):
    ...

@when(u'Clicar na opção "Ordenar por"')
def click_search_by(context):
    ...
    
@when(u'Selecionar a opção “Avaliação e Sugestões"')
def select_search_by(context):
    ...

@then(u'verificar o nome do primeiro da lista com o texto "ibis budget Manaus"')
def check_first_name(context):
    ...
    
@then(u'verificar a avaliação do primeiro da lista com o texto "Muito bom"')
def check_first_element_evaluation(context):
    ...

@then(u'verificar o valor do primeiro da lista com o texto "R$177,00"')
def check_first_element_value(context):
    ...