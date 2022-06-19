from behave import given, when, then
from selenium.webdriver import Safari
from selenium.webdriver.support.select import Select
import time

delay = 5
timestamp = 60

@given(u'que eu esteja na tela inicial')
def go_to_page(context):
    context.browser.get('http://www.trivago.com.br')

@when(u'o campo Hotel|Destino for preenchido com o texto "Manaus"')
def fill_location(context):
    context.browser.find_element_by_id('input-auto-complete').send_keys('Manaus')
    time.sleep(delay) #Time to load element
    context.browser.find_elements_by_class_name('AutoComplete_suggestion__XEZ1N')[0].click()

@when(u'clica-se no botão "Pesquisar"')
def click_search(context):
    context.browser.find_element_by_xpath('//*[@id="__next"]/div[1]/main/div[3]/div[2]/div/div[1]/div/div/form/div[3]/button/span/span').click() #botao de pesquisa correto
    time.sleep(timestamp)  #Time to load page

@when(u'clicar na opção "Ordenar por" e selecionar “Avaliação e Sugestões"')
def click_sort_by(context):
    element = context.browser.find_element_by_xpath('/html/body/div[1]/div[1]/main/div[4]/div[3]/div/div[1]/div/select')
    select_object = Select(element)
    select_object.select_by_index(1)
    time.sleep(delay)  #Time to load list

@then(u'verificar o nome do primeiro da lista com o texto "ibis budget Manaus"')
def check_first_name(context):
    elements = context.browser.find_elements_by_id('__next')
    html = elements[0].get_attribute('outerHTML')
    assert '<span itemprop="name">ibis budget Manaus</span>' in html

@then(u'verificar a avaliação do primeiro da lista com o texto "Muito bom"')
def check_first_element_evaluation(context):
    elements = context.browser.find_elements_by_id('__next')
    html = elements[0].get_attribute('outerHTML')
    assert '<strong class="leading-none">Muito bom&nbsp;</strong>' in html

@then(u'verificar o valor do primeiro da lista com o texto "R$177,00"')
def check_first_element_value(context):
    elements = context.browser.find_elements_by_id('__next')
    html = elements[0].get_attribute('outerHTML')
    assert 'data-cos="recommendedPrice" itemprop="price">R$177</p>' in html
