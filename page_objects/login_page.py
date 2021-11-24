from seleniumbase import BaseCase

class LoginPage(BaseCase):
    heading = "span[class*=ReSignIn__title]"
    sign_in = "button[class*=btn_default]"
    login = "input#login"
    password = "input#password"
    login_button = "button[class*=btn_primary]"

    def assert_heading_login(self):
        text = self.find_element(LoginPage.heading, timeout=20)
        self.assert_equal("Вход", text.text)