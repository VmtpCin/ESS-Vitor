from pytest_bdd import scenario, given, when, then


@given('A loja "Hortifruti" foi registrada com sucesso com o cnpj "000000" e senha "1234"')
def step_impl():
    raise NotImplementedError(
        u'STEP: Given A loja "Hortifruti" foi registrada com sucesso com o cnpj "000000" e senha "1234"')


@given("Eu estou na pagina de login")
def step_impl():
    raise NotImplementedError(u'STEP: And Eu estou na pagina de login')


@given('Eu estou na pagina de "login de lojas"')
def step_impl():
    raise NotImplementedError(u'STEP: And Eu estou na pagina de "login de lojas"')


@when('Eu digito "000000" no campo "cnpj"')
def step_impl():
    raise NotImplementedError(u'STEP: When Eu digito "000000" no campo "cnpj"')


@given('Eu digito "abracabra" no campo de "senha"')
def step_impl():
    raise NotImplementedError(u'STEP: And Eu digito "abracabra" no campo de "senha"')


@given('Eu seleciono a opção de "Login"')
def step_impl():
    raise NotImplementedError(u'STEP: And Eu seleciono a opção de "Login"')


@then('Eu vejo a mensagem "Invalid CNPJ or password"')
def step_impl():
    raise NotImplementedError(u'STEP: Then Eu vejo a mensagem "Invalid CNPJ or password"')


@given('Os campos de "cnpj" e "senha" ficam vazios')
def step_impl():
    raise NotImplementedError(u'STEP: And Os campos de "cnpj" e "senha" ficam vazios')


@given('Eu digito "1234" no campo de "senha"')
def step_impl():
    raise NotImplementedError(u'STEP: And Eu digito "1234" no campo de "senha"')


@then('Eu vejo a mensagem "Hi! You have logged in successfully"')
def step_impl():
    raise NotImplementedError(u'STEP: Then Eu vejo a mensagem "Hi! You have logged in successfully"')


@given("Eu vejo a homepage da minha loja")
def step_impl():
    raise NotImplementedError(u'STEP: And Eu vejo a homepage da minha loja')