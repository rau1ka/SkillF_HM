import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
    # Автоматически загружаем Гугл-драйвер (предварительно установили pip install webdriver-manager)
   pytest.driver = webdriver.Chrome('с:/chromedriver.exe')
    # pytest.driver = webdriver.Chrome('/GoogleDriver/chromedriver.exe')
    # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')
   time.sleep(5)

   yield

   pytest.driver.quit()


def test_show_my_pets():
    # Вводим email
   pytest.driver.find_element(By.ID, 'email').send_keys('raul-edil@yandex.ru')
   time.sleep(2)
    # Вводим пароль
   pytest.driver.find_element(By.ID, 'pass').send_keys('Pirelli7')
   time.sleep(2)
    # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   time.sleep(3)
    #Нажимаем на кнопку "Мои питомцы"
   pytest.driver.find_element(By.CSS_SELECTOR, 'div#navbarNav > ul > li > a').click()
   assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'