import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_all_pets_different_names(test_show_my_pets):
   # # Вводим email
   # pytest.driver.find_element(By.ID, 'email').send_keys('raul-edil@yandex.ru')
   # time.sleep(2)
   #  # Вводим пароль
   # pytest.driver.find_element(By.ID, 'pass').send_keys('Pirelli7')
   # time.sleep(2)
   #  # Нажимаем на кнопку входа в аккаунт
   # pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   # time.sleep(3)
   #  #Нажимаем на кнопку "Мои питомцы"
   # pytest.driver.find_element(By.CSS_SELECTOR, 'div#navbarNav > ul > li > a').click()

   '''Проверяем что на странице со списком моих питомцев присутствуют все питомцы'''
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
   # Сохраняем в переменную pet_data элементы с данными о питомцах
   pet_data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

   # Перебираем данные из pet_data, оставляем имя, возраст, и породу остальное меняем на пустую строку
   # и разделяем по пробелу.Выбераем имена и добавляем их в список pets_name.
   pets_name = []
   for i in range(len(pet_data)):
      data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
      split_data_pet = data_pet.split(' ')
      pets_name.append(split_data_pet[0])

   # Перебираем имена и если имя повторяется то прибавляем к счетчику r единицу.
   # Проверяем, если r == 0 то повторяющихся имен нет.
   r = 0
   for i in range(len(pets_name)):
      if pets_name.count(pets_name[i]) > 1:
         r += 1
   assert r == 0
   print(r)
   print(pets_name)