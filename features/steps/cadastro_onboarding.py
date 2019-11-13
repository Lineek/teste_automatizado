from behave import given, when, then
from framework.wepapp import webapp
from pages.dashboard import dashboard


@given(u'que eu acesse o site "http://localhost:4200/"')
def step_acessar_site_impl(context):
    print('STEP: Given que eu acesse o site "http://localhost:4200/"')
    dashboard.ir_para_url()

@given(u'estou logado')
def step_logado_impl(context):
    print('STEP: Given estou logado')
    dashboard.logar()

@given(u'clico no menu "Processos" depois')
def step_clicar_menu_processos_impl(context):
    print('STEP: Given clico no menu "Processos" depois')
    dashboard.clicar_menu_processos()


@given(u'clico no menu "Workflow operacional" depois')
def step_clicar_menu_workflow_operacional_impl(context):
    print('STEP: Given clico no menu "Workflow operacional" depois')
    dashboard.clicar_menu_workflow_operacional()


@given(u'clico no menu "Onboarding" depois')
def step_clicar_menu_onboarding_impl(context):
    print('STEP: Given clico no menu "Onboarding" depois')
    dashboard.clicar_menu_onboarding()


@given(u'que estou na página do onboarding')
def step_esperar_pagina_onboarding_impl(context):
    print('STEP: Given que estou na página do onboarding')
    dashboard.verificar_pagina_onboarding()


@when(u'eu clico em "Cadastrar novo cliente"')
def step_clicar_botao_cadastrar_novo_cliente_impl(context):
    print('STEP: When eu clico em "Cadastrar novo cliente"')
    dashboard.clicar_botao_cadastrar_novo_cliente()


@then(u'o botão "Cadastrar" deve estar desabilitado')
def step_verificar_botao_cadastrar_desabilitado_impl(context):
    print('STEP: Then o botão "Cadastrar" deve estar desabilitado')
    estado = dashboard.estado_botao_cadastrar()
    assert estado == False


@when(u'preecho o campo CNPJ com o valor "33532348600012"')
def step_preencho_cnpj_invalido_impl(context):
    print('STEP: When preecho o campo CNPJ com o valor "33532348600012"')
    cnpj = "33532348600012"
    dashboard.preencher_campo_cnpj(cnpj)


@when(u'preecho o campo CNPJ com o valor "8445384403"')
def step_preencho_cnpj_incompleto_impl(context):
    print('STEP: When preecho o campo CNPJ com o valor "8445384403"')
    cnpj = "8445384403"
    dashboard.preencher_campo_cnpj(cnpj)

@when(u'preecho o campo CNPJ com o valor "59275792000150"')
def step_preencho_cnpj_inexistente_impl(context):
    print('STEP: When preecho o campo CNPJ com o valor "59275792000150"')
    cnpj = "59275792000150"
    dashboard.preencher_campo_cnpj(cnpj)


@when(u'preecho o campo CNPJ com o valor "84453844034244"')
def step_preencho_cnpj_existente_impl(context):
    print('STEP: When preecho o campo CNPJ com o valor "84453844034244"')
    cnpj = "84453844034244"
    dashboard.preencher_campo_cnpj(cnpj)


@when(u'clico em "Cadastrar"')
def step_clicar_cadastrar_impl(context):
    print('STEP: When clico em "Cadastrar"')
    dashboard.clicar_botao_cadastrar()


@then(u'a seção de "Envio de arquivos" deve aparecer')
def step_verificar_secao_envio_arquivos_impl(context):
    print('STEP: Then a seção de "Envio de arquivos" deve aparecer')
    dashboard.verificar_secao_envio()


@then(u'a mensagem Cliente já cadastrado esteira de onboarding e encontra-se na etapa cadastro deve ser mostrada')
def step_verificar_mensagem_cadastro_existente_impl(context):
    print('STEP: Then a mensagem "Cliente já cadastrado esteira de onboarding e encontra-se na etapa cadastro deve ser mostrada"')
    dashboard.verificar_mensagem_cadastro_existente()