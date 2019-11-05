#language: pt

Funcionalidade: Buscar CEP no Google
   COMO mero usuário comum
   QUERO descobrir meu cep digitando meu endereço
   ASSIM podendo utilizar em diversas coisas

   Contexto:
        Dado que eu acesse o site "http://www.google.com"

   Esquema do Cenário: CEP deve aparecer nos resultados
        Dado que estou na página do Google
        Quando eu preencho o endereço "<enderecos>"
        E clico no botão "Pesquisa Google"
        Então o CEP "<ceps>" deve aparecer nas buscas
    
    Exemplos:
    | enderecos               | ceps      |
    | Rua Torres da Barra cep | 05037-055 |