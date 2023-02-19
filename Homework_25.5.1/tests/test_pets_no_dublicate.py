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

   '''Поверяем что на странице со списком моих питомцев нет повторяющихся питомцев'''

   # Устанавливаем явное ожидание
   element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

   # Сохраняем в переменную pet_data элементы с данными о питомцах
   pet_data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

   # Перебираем данные из pet_data, оставляем имя, возраст, и породу остальное меняем на пустую строку
   # и разделяем по пробелу.
   list_data = []
   for i in range(len(pet_data)):
        data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        list_data.append(split_data_pet)

   # Склеиваем имя, возраст и породу, получившиеся склееные слова добавляем в строку
   # и между ними вставляем пробел
   line = ''
   for i in list_data:
        line += ''.join(i)
        line += ' '

   # Получаем список из строки line
   list_line = line.split(' ')

   # Превращаем список в множество
   set_list_line = set(list_line)

   # Находим количество элементов списка и множества
   a = len(list_line)
   b = len(set_list_line)

   # Из количества элементов списка вычитаем количество элементов множества
   result = a - b

   # Если количество элементов == 0 значит карточки с одинаковыми данными отсутствуют
   assert result == 0
