from seleniumbase import BaseCase

class MainPage(BaseCase):
    title = "span[class*=ReGreeting__title]"
    sign_in = "button[class*=btn_default]"
    sign_up = "button[class*=btn btn_primary]"
    heading = "span[class*=ReGreeting__title]"
    title_select_language = "span[class*=ReGreeting__language-title]"
    select_language = "div[class*=flag-select]"

    def page_open(self):
        self.open("https://stage.omnio.site")

    def assert_heading_main(self):
        text = self.find_element(MainPage.heading, timeout=20)
        self.assert_equal("Зарегистрируйтесь или войдите в свой аккаунт", text.text)

    def assert_title_text_main(self):
        self.assert_title("Omnio - пульсовая диагностика организма со смартфона")

    def click_sign_in_main(self):
        self.click(MainPage.sign_in)
