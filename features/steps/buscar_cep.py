from behave import given, when, then
from framework.wepapp import webapp
from pages.google import google

@given(u'que eu acesse o site "http://www.google.com"')
def step_impl(context):
    print('STEP: Given que eu acesse o site "http://www.google.com"')
    webapp.load_website()
    

@given(u'que estou na página do Google')
def step_impl(context):
    print('STEP: Given que estou na página do Google')
    google.verificar_url()


@when(u'eu preencho o endereço "{endereco}"')
def step_impl(context, endereco):
    print('STEP: When eu preencho o endereço "Rua Torres da Barra cep"')
    google.escrever_texto(endereco)


@when(u'clico no botão "Pesquisa Google"')
def step_impl(context):
    print('STEP: When clico no botão "Pesquisa Google"')
    google.clicar_botao_pesquisar()


@then(u'o CEP "{cep}" deve aparecer nas buscas')
def step_impl(context, cep):
    print('STEP: Then o CEP "05037-055" deve aparecer nas buscas')
    google.verificar_texto_nas_buscas(cep)