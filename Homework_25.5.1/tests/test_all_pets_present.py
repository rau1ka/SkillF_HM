import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_all_pets_present(test_show_my_pets):

   '''Проверяем что на странице со списком моих питомцев присутствуют все питомцы'''
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))

   # Сохраняем в переменную ststistic элементы статистики
   statistic = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

   # Сохраняем в переменную pets элементы карточек питомцев
   pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

   # Получаем количество питомцев из данных статистики
   number = statistic[0].text.split('\n')
   number = number[1].split(' ')
   number = int(number[1])

   # Получаем количество карточек питомцев
   number_of_pets = len(pets)

   # Проверяем что количество питомцев из статистики совпадает с количеством карточек питомцев
   assert number == number_of_pets
