from behave import given, when, then
from selenium.webdriver import Safari

@given(u'que eu esteja na tela de busca')
def go_to_page(context):
    context.browser = Safari()
    context.browser.get('http://www.buscacep.correios.com.br')

@when(u'o campo CEP|Endereço for preenchido com o texto "69005-040"')
def fill_cep(context):
    context.browser.find_element_by_id('endereco').send_keys('69005-040')
    

@when(u'clica-se no botão buscar')
def click_search(context):
    context.browser.find_element_by_id('btn_pesquisar').click()

@then(u'deve-se ser redirecionado para a tela de resultado de busca')
def sucess_search(context):
   #assert 'Resultado da Busca por Endereço ou CEP' in context.browser.find_elements_by_xpath('//*[@id="mensagem-resultado"]')[0].text