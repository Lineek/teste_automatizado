#language: pt

Funcionalidade: Cadastrar cliente no Onboarding
   COMO um analista EU QUERO acessar a tela de Onboarding do Sofisa Digital
   ASSIM podendo cadastrar novos clientes

   Contexto:
        Dado que eu acesse o site "http://localhost:4200/"
        E estou logado
        E clico no menu "Processos" depois
        E clico no menu "Workflow operacional" depois
        E clico no menu "Onboarding" depois

   Cenário: Cadastrar cliente sem preencher
        Dado que estou na página do onboarding
        Quando eu clico em "Cadastrar novo cliente"
        Então o botão "Cadastrar" deve estar desabilitado

   Cenário: Cadastrar cliente com cnpj inválido
        Dado que estou na página do onboarding
        Quando eu clico em "Cadastrar novo cliente"
        E preecho o campo CNPJ com o valor "33532348600012"
        Então o botão "Cadastrar" deve estar desabilitado

   Cenário: Cadastrar cliente com cnpj incompleto
        Dado que estou na página do onboarding
        Quando eu clico em "Cadastrar novo cliente"
        E preecho o campo CNPJ com o valor "8445384403"
        Então o botão "Cadastrar" deve estar desabilitado

   Cenário: Cadastrar cliente não existente
        Dado que estou na página do onboarding
        Quando eu clico em "Cadastrar novo cliente"
        E preecho o campo CNPJ com o valor "59275792000150"
        E clico em "Cadastrar"
        Então a seção de "Envio de arquivos" deve aparecer

   Cenário: Cadastrar cliente existente
        Dado que estou na página do onboarding
        Quando eu clico em "Cadastrar novo cliente"
        E preecho o campo CNPJ com o valor "84453844034244"
        E clico em "Cadastrar"
        Então a mensagem Cliente já cadastrado esteira de onboarding e encontra-se na etapa cadastro deve ser mostrada

        