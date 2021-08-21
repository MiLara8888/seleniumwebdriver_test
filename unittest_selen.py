#Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
#Создайте новый файл
#Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
#Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
#Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
#Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
#Запустите получившиеся тесты из файла

import unittest
from selenium import webdriver
import time


class test_class(unittest.TestCase):
    def test_func1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        inp1 = browser.find_element_by_css_selector('[placeholder="Input your first name"]')
        inp1.send_keys('ivan')
        inp2 = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
        inp2.send_keys('ivanov')
        inp3 = browser.find_element_by_css_selector('[placeholder="Input your email"]')
        inp3.send_keys('email@email')
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual( "Congratulations! You have successfully registered!", welcome_text,'error test1')
        time.sleep(3)
        browser.quit()

    def test_func2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        inp1 = browser.find_element_by_css_selector('[placeholder="Input your first name"]')
        inp1.send_keys('ivan')
        inp2 = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
        inp2.send_keys('ivanov')
        inp3 = browser.find_element_by_css_selector('[placeholder="Input your email"]')
        inp3.send_keys('email@email')
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,'error test2')
        time.sleep(3)
        browser.quit()


if __name__=='__main__':
    unittest.main()