from api import PetFriends
from settings import valid_email, valid_password
import os

pf = PetFriends()

def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status ==200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_pets(auth_key, filter)
    assert status ==200
    assert len(result['pets']) >0 

def test_get_api_key_for_valid_user(email='invalid_email@yandex.ru', password='Qwerty'):
    """При несуществующих данных авторизации получаем код 403"""
    status, result= pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result

def test_post_add_pet_without_photo(name ='murka', animal_type = 'кошка', age = '3'):
    """Добавление нового питомца"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_add_pet_without_photo(auth_key, name, animal_type, age)
    assert status ==200
    assert result['name'] == name

def test_post_add_pet_without_info_and_photo(name ='', animal_type = '', age = ''):
    """Добавление нового питомца без указания обязательных параметров(имя, тип, возраст)"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_add_pet_without_photo(auth_key, name, animal_type, age)
    assert status ==200
    assert result['name'] == name

def test_post_add_pet_without_photo(name ='murka', animal_type = 'кошка', age = '3333333333'):
    """ Добавление нового питомца c указанием слишком большого значения возраста"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_add_pet_without_photo(auth_key, name, animal_type, age)
    assert status ==200
    assert result['name'] == name

def test_post_add_pet_information_with_photo(name='boriska', animal_type='кот', age='5', pet_photo ='images/cat.jpg'):
    """ Добавление нового питомца с фото"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_add_pet_information_with_photo(auth_key, name, animal_type, age, pet_photo)
    assert status ==200
    assert result['name'] == name

def test_post_add_pet_wrong_name(name ='444', animal_type = 'кошка', age = '3'):
    """ Добавление нового питомца c указанием цифр вместо имени"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_add_pet_without_photo(auth_key, name, animal_type, age)
    assert status ==200
    assert result['name'] == name

def test_post_add_pet_wrong_type(name ='murka', animal_type = '111', age = '3'):
    """ Добавление нового питомца c указанием цифр вместо типа"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_add_pet_without_photo(auth_key, name, animal_type, age)
    assert status ==200
    assert result['name'] == name

def test_post_add_pet_information_with_photo(name='boriska', animal_type='кот', age='5', pet_photo ='images/boris.txt'):
    """ Добавление нового питомца с указанием текстового файла вместо фото"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_add_pet_information_with_photo(auth_key, name, animal_type, age, pet_photo)
    assert status ==200
    assert result['name'] == name





