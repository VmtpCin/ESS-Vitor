# Created by Vitor Paz at 18/02/2024
Feature: Store login
  As a store/supplier
    I want to login to the system
    So that I can update inventory and manage purchases

  Scenario: Login bem sucedido
        Given A loja "Hortifruti" foi registrada com sucesso com o cnpj "000000" e senha "1234"
        And Eu estou na pagina de "login de lojas"
        When Eu digito "000000" no campo "cnpj"
        And Eu digito "abracabra" no campo de "senha"
        And Eu seleciono a opção de "Login"
        Then Eu vejo a mensagem "Invalid CNPJ or password"
        And Os campos de "cnpj" e "senha" ficam vazios

  Scenario: Login mal sucedido
        Given A loja "Hortifruti" foi registrada com sucesso com o cnpj "000000" e senha "1234"
        And Eu estou na pagina de "login de lojas"
        When Eu digito "000000" no campo "cnpj"
        And Eu digito "1234" no campo de "senha"
        And Eu seleciono a opção de "Login"
        Then Eu vejo a mensagem "Hi! You have logged in successfully"
        And Eu vejo a homepage da minha loja