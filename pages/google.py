from framework.wepapp import webapp
from selenium.webdriver.common.by import By


class Google():
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Google()
        return cls.instance

    def __init__(self):
        self.driver = webapp.get_driver()
    
    def escrever_texto(self, texto):
        input = self.driver.find_element_by_name('q')
        input.send_keys(texto)

    def verificar_url(self):
        assert self.driver.current_url == 'https://www.google.com/'

    def verificar_texto_nas_buscas(self, texto):
        webapp.wait_for_element((By.ID, 'search'))
        spans = self.driver.find_elements_by_xpath('//span[@class="st"]')
        validacao = False
        for span in spans:
            if (texto in span.text):
                validacao = True
                break
        assert validacao
    
    def clicar_botao_pesquisar(self):
        webapp.wait_for_element((By.NAME, 'btnK')).click()



google = Google.get_instance()