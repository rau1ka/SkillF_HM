import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_all_pets_are_present():
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

   '''Поверяем что на странице со списком моих питомцев хотя бы у половины питомцев есть фото'''
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))

   # Сохраняем в переменную ststistic элементы статистики
   statistic = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")

   # Сохраняем в переменную images элементы с атрибутом img
   images = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover img')

   # Получаем количество питомцев из данных статистики
   number = statistic[0].text.split('\n')
   number = number[1].split(' ')
   number = int(number[1])

   # Находим половину от количества питомцев
   half = number // 2

   # Находим количество питомцев с фотографией
   number_а_photos = 0
   for i in range(len(images)):
      if images[i].get_attribute('src') != '':
         number_а_photos += 1

   # Проверяем что количество питомцев с фотографией больше или равно половине количества питомцев
   assert number_а_photos >= half
   print(f'количество фото: {number_а_photos}')
   print(f'Половина от числа питомцев: {half}')