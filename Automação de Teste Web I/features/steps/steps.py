from behave import given, when, then
import time

delay = 10

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
    time.sleep(delay) #time to load the page
    elements = context.browser.find_elements_by_xpath('/html/body/main/form/div[1]/div[2]/div/div[3]/table/tbody/tr/td[1]')
    html_nome = elements[0].get_attribute('outerHTML')
    assert '<td data-th="Logradouro/Nome">Rua Miranda Leão</td>' in html_nome

    elements = context.browser.find_elements_by_xpath('/html/body/main/form/div[1]/div[2]/div/div[3]/table/tbody/tr/td[2]')
    html_district = elements[0].get_attribute('outerHTML')
    assert '<td data-th="Bairro/Distrito">Centro</td>' in html_district

    elements = context.browser.find_elements_by_xpath('/html/body/main/form/div[1]/div[2]/div/div[3]/table/tbody/tr/td[3]')
    html_locale = elements[0].get_attribute('outerHTML')
    assert '<td data-th="Localidade/UF">Manaus/AM</td>' in html_locale

    elements = context.browser.find_elements_by_xpath('/html/body/main/form/div[1]/div[2]/div/div[3]/table/tbody/tr/td[4]')
    html_CEP = elements[0].get_attribute('outerHTML')
    assert '<td data-th="CEP">69005-040</td>' in html_CEP
