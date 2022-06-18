from pickle import FALSE
from behave import given, when, then

@given(u'que eu esteja na tela de busca')
def go_to_page(context):
    context.browser.get('http://www.buscacep.correios.com.br')

@when(u'o campo CEP|Endereço for preenchido com o texto "69005-040"')
def fill_cep(context):
    context.browser.find_element_by_id('endereco').send_keys('69005-040')

@when(u'clica-se no botão buscar')
def click_search(context):
    context.browser.find_element_by_id('btn_pesquisar').click()

@then(u'deve-se ser redirecionado para a tela de resultado de busca')
def sucess_search(context):
    table = context.browser.find_element_by_xpath('/html/body/main/form/div[1]/div[2]/div/div[3]/table')
    table_html = table.get_attribute('outerHTML')
    assert table.is_displayed() == True
    assert '<th data-th="Logradouro/Nome">Logradouro/Nome</th>' in table_html
    assert '<th data-th="Logradouro/Nome">Logradouro/Nome</th>' in table_html
    assert '<th data-th="Bairro/Distrito">Bairro/Distrito</th>' in table_html
    assert '<th data-th="Localidade/UF">Localidade/UF</th>' in table_html
    assert '<th data-th="CEP">CEP</th>' in table_html