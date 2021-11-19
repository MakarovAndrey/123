from seleniumbase import BaseCase

#https://www.youtube.com/c/AutomationBro/videos

class MainPage(BaseCase):
    def test_open(self):
        self.open("https://stage.omnio.site")
        self.assert_title("Omnio - пульсовая диагностика организма со смартфона")
        self.click("button.btn.btn_default")
        self.send_keys('input#login', 'mal@inveramed.ru')
        self.send_keys('input#password', '12345678')
        self.click(".ReSignInForm__buttons-item")
        # find element by xpath
        pulse_wave = self.find_element("//*[starts-with(@class, 'RePulseWaveFilter__filter-title')]", timeout=20)
#       print(element.text)
        self.assert_equal("Пульсовая волна", pulse_wave.text)
        self.click(".ReAsideMainWrapper__user")
        profile = self.find_element(".ReProfile__self-title")
        self.assert_equal("Профиль", profile.text)

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