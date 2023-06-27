import redis
import json

red = redis.Redis(
    host='ваш хост',
    port=ваш портт,
    password='пароль'
)

# Записываем данные в кеш

red.set('var1', 'value1')  # записываем в кеш строку "value1"
print(red.get('var1'))  # считываем из кеша данные

# Добавляем словарь

dict1 = {'key1': 'value1', 'key2': 'value2'} # создаём словарь для записи
red.set('dict1', json.dumps(dict1)) # с помощью функции dumps() из модуля json превратим наш словарь в строчку

converted_dict = json.loads(red.get('dict1')) # с помощью знакомой нам функции превращаем данные,
# полученные из кеша обратно в словарь

print(type(converted_dict)) # убеждаемся, что мы получили действительно словарь
print(converted_dict) # ну и выводим его содержание

# Удаляем данные из кеша по ключу

red.delete('dict1')  # удаляются ключи с помощью метода .delete()
print(red.get('dict1'))
