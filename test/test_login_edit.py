#from seleniumbase import BaseCase
from page_objects.main_page import MainPage
from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage


#https://www.youtube.com/c/AutomationBro/videos



class AuthPage(MainPage, LoginPage, HomePage):

    def test_auth_access(self):
        self.auth_success()
    def test_login_not_found(self):
        self.login_not_found()

#    def test_login_good1(self):
 #       self.page_open()
#        self.assert_title_text_main()
 #       self.assert_heading_main()
 #       self.click_sign_in_main()
 #       self.assert_link_registration()
 #       self.assert_heading_login()
 #       self.input_login()
 #       self.input_password()
 #       self.click_sign_in_login()
 #       self.recommentation_or_home()
#        self.click(".ReAsideMainWrapper__user")
#        profile = self.find_element(".ReProfile__self-title")
#        self.assert_equal("Профиль", profile.text)

 #   def test_login_not_found1(self):
 #       self.page_open()
 #       self.assert_title("Omnio - пульсовая диагностика организма со смартфона")
 #       self.click("button.btn.btn_default")
 #       self.send_keys('input#login', '12345@inveramed.ru')
 #       self.send_keys('input#password', '12345678')
  #      self.click(".ReSignInForm__buttons-item")
  #      error_1 = self.find_element("div[class*=input--wrapper_description]", timeout=2)
  #      self.assert_equal("Неверный логин или пароль", error_1.text)



        #class *=input--wrapper_description
        #find element by css-selector
        # span[class*=ReMeasurementDiagram__icon-tooltip-text]

 #       self.assert_element("a.active.ReAsideMainWrapper__nav-button.ReAsideMainWrapper__nav-button_active", timeout=30)
 #           self.click("span.ReAsideMainWrapper__exit-button-text")
#      elif self.assert_text('Помогли ли вам рекомендации по питанию', 'span.ReRecommendationsFeedback__title'):
 #           print('Recomendation')
 #       else:
 #   def test_click(self):
 #       self.open("https://stage.omnio.site")
 #       self.assert_title("Omnio - пульсовая диагностика организма со смартфона")
 #       self.click("button.btn.btn_default")
 #       self.send_keys('input#login', 'mal@misbox.ru')
 #       self.send_keys('input#password', '12345678')
 #       self.click("button.btn.btn_primary.ReSignInForm__buttons-item")
 #       self.click("a.ReAsideMainWrapper__nav-button", timeout=30)
 #       self.click("a.ReAsideMainWrapper__nav-button", timeout=30)
 #       self.assert_text("Профиль", "span.ReProfile__self-title")
#