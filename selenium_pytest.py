# открыть страницу
# ввести правильный ответ
# нажать кнопку "Отправить"
# дождаться фидбека о том, что ответ правильный
#
# проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"
# Опциональный фидбек — это текст в черном поле, как показано на скриншоте:


import pytest
from selenium import webdriver
import time
from math import *


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser

    browser.quit()


@pytest.mark.parametrize('url', ['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1',
                                 'https://stepik.org/lesson/236897/step/1', 'https://stepik.org/lesson/236898/step/1',
                                 'https://stepik.org/lesson/236899/step/1', 'https://stepik.org/lesson/236903/step/1',
                                 'https://stepik.org/lesson/236904/step/1', 'https://stepik.org/lesson/236905/step/1'])
def test_guest_should_see_login_link(browser, url):
    link = url
    browser.get(link)
    time.sleep(5)
    inp = browser.find_element_by_css_selector('.ember-text-area').send_keys(str(log(int(time.time()))))
    but = browser.find_element_by_css_selector('.submit-submission').click()
    time.sleep(5)
    textt = browser.find_element_by_css_selector('.smart-hints__hint').text
    assert textt == 'Correct!', f' текст- {textt}'
