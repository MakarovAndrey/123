from seleniumbase import BaseCase

class HomePage(BaseCase):
    close_recommendation = "button[class*=ReRecommendationsFeedback__close]"
    assert_recommendation_title = "span[class*=ReRecommendationsFeedback__title]"
    assert_recommendation_text = "p[class*=ReRecommendationsFeedback__text]"
    assert_recommendation_button = "button[class*=btn_primary]" # таких 4 с одинаковым классом
    assert_title = "span[class*=RePulseWaveFilter__filter-title]"
    profile = "div[class*=ReAsideMainWrapper__user]"

# find element by xpath
#       pulse_wave = self.find_element("//*[starts-with(@class, 'RePulseWaveFilter__filter-title')]", timeout=20)
#       print(element.text)
#       self.assert_equal("Пульсовая волна", pulse_wave.text)

    def recommentation_or_home(self):
        a = self.wait_for_element(HomePage.assert_recommendation_title, timeout=20).text
        print(a)
        if a == "Вы запрашивали":
           self.click(HomePage.close_recommendation)
        else:
            self.click(HomePage.profile)
#            text = self.find_element(HomePage.assert_title, timeout=5)
#            self.assert_equal("Пульсовая волна1", text.text)

