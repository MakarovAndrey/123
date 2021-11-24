from seleniumbase import BaseCase
import imaplib
import email
import re
import time

class AuthPage(BaseCase):
    def test_registration_good(self):
        self.open("https://stage.omnio.site")
        self.assert_title("Omnio - пульсовая диагностика организма со смартфона")
        self.click("button[class*=btn_primary]")
        self.send_keys('input#login', 'makcheck@yandex.ru')
        self.send_keys('input#password', '12345678')
        self.click("button[class*=btn_primary]")
        time.sleep(5)
        assert_title = self.find_element("span[class*=ReSignUp__title")
        self.assert_equal("Введите код", assert_title.text)
        mail = imaplib.IMAP4_SSL('imap.yandex.ru')
        mail.login('mytestnov@yandex.ru', 'YjdsqYjdsq123')
        mail.list()
        # Выводит список папок в почтовом ящике.
        mail.select("inbox") # Подключаемся к папке "входящие".
        result, data = mail.search(None, "ALL")
        ids = data[0] # Получаем строку номеров писем
        id_list = ids.split() # Разделяем ID писем
        latest_email_id = id_list[-1] # Берем последний ID
        result, data = mail.fetch(latest_email_id, "(RFC822)") # Получаем тело письма (RFC822) для данного ID
        raw_email = data[0][1].decode() # выводим письмо в читабельном виде
        msg = email.message_from_string(raw_email) #достает из raw_email в формат email-а. Чтобы потом можно было доставать легко отправителя, получаетля тело и т д
        payload = msg.get_payload()
        # find 4-8 digits number
        code = re.findall(r'(\d{4,8})', payload)
        print(code[0])
        self.send_keys("input#code", code[0])
        time.sleep(5)
        self.click("button[class*=btn_primary]")
