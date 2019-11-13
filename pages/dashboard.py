from framework.wepapp import webapp
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class Dashboard():
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Dashboard()
        return cls.instance

    def __init__(self):
        self.driver = webapp.get_driver()

    def ir_para_url(self):
        self.driver.get('http://localhost:4200/')

    def verificar_url(self):
        assert "localhost:4200/" in self.driver.current_url

    def logar(self):
        try:
            self.esperar_pagina_login()
            self.preencher_usuario("giannotta.3mpk")
            self.preencher_senha("@3Minhasenhaegrande")
            self.clicar_login()
        except TimeoutException:
            pass
        assert len(webapp.wait_for_element((By.XPATH, "//span[@class='so-header--user--info--name']")).get_attribute("innerText")) > 0
    
    def verificar_pagina_onboarding(self):
        try:
            assert webapp.wait_for_element((By.XPATH, "//h2[@class='so-header--pages--title'][text()='Workflow Onboarding - Middle']"))
        except TimeoutException:
            assert False
    
    def verificar_secao_envio(self):
        try:
            assert webapp.wait_for_element((By.XPATH, "//div[@class='form__title'][text()='Envio de arquivos']"))
        except TimeoutException:
            assert False

    def verificar_mensagem_cadastro_existente(self):
        try:
            assert webapp.wait_for_element((By.XPATH, "//div[text()=' Cliente já cadastrado esteira de onboarding e encontra-se na etapa cadastro ']"))
        except TimeoutException:
            assert False

    def esperar_pagina_login(self):
        webapp.wait_for_element((By.ID, "kc-page-title"), 5)
    
    def preencher_usuario(self, usuario):
        webapp.wait_for_element((By.ID, "username")).send_keys(usuario)

    def preencher_senha(self, senha):
        webapp.wait_for_element((By.ID, "password")).send_keys(senha)
        
    def preencher_campo_cnpj(self, cnpj):
        webapp.wait_for_element((By.ID, "cnpj")).send_keys(cnpj)

    def clicar_login(self):
        webapp.wait_for_element((By.ID, "kc-login")).click()

    def clicar_menu_processos(self):
        webapp.wait_for_element((By.XPATH, "//so-nav/nav/ul/li/a/span[text()='Processos']")).click()

    def clicar_menu_workflow_operacional(self):
        webapp.wait_for_element((By.XPATH, "//so-nav/nav/ul/li/ul/li/a/span[text()='Workflow operacional']")).click()
        
    def clicar_menu_onboarding(self):
        webapp.wait_for_element((By.XPATH, "//so-nav/nav/ul/li/ul/li/ul/li/a/span[text()='Onboarding']")).click()
    
    def clicar_botao_cadastrar_novo_cliente(self):
        webapp.wait_for_element((By.XPATH, "//a[text()='Cadastrar novo cliente']")).click()

    def clicar_botao_cadastrar(self):
        webapp.wait_for_element((By.ID, "enviar")).click()
        
    def estado_botao_cadastrar(self):
        classlist = webapp.wait_for_element((By.CSS_SELECTOR, "#enviar > a")).get_attribute("class")
        return "disabled" not in classlist
        
        

dashboard = Dashboard.get_instance()