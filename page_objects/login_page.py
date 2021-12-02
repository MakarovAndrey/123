from seleniumbase import BaseCase
from page_objects.main_page import MainPage
from page_objects.home_page import HomePage
import time

class LoginPage(BaseCase):
    heading = "span[class*=ReSignIn__title]"
    sign_in = "button[class*=btn_default]"
    link_registration = "a[class*=ReSignInForm__registration-link]"
    login = "input#login"
    password = "input#password"
    login_button = "button[class*=btn_primary]"
    exit = "span[class*=ReAsideMainWrapper__exit-button-text]"
    error_text_login = "div[class*=input--wrapper_description]"

    def auth_success(self):
        self.open("https://stage.omnio.site")
#        self.assert_title("Omnio - пульсовая диагностика организма со смартфона")
        self.click(MainPage.sign_in)
        self.send_keys(self.login, "mal@inveramed.ru")
        self.send_keys(self.password, "12345678")
        self.click(self.login_button)
        time.sleep(5)
        text = self.find_element(self.exit)
        self.assert_equal("Выд", text.text)
        self.click(self.exit)

    def login_not_found(self):
        self.open("https://stage.omnio.site")
#        self.assert_title("Omnio - пульсовая диагностика организма со смартфона")
        self.click(MainPage.sign_in)
        self.send_keys(self.login, '12345@inveramed.ru')
        self.send_keys(self.password, '12345678')
        self.click(self.login_button)
        error = self.find_element(self.error_text_login, timeout=5)
        self.assert_equal("Неверный логин или пароль", error.text)


