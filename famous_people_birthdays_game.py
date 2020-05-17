# МОДУЛЬ 4
'''
Задание
Улучшить программу Викторина из предыдущего дз
Есть 10 известных людей и их даты рождения в формате '02.01.1988' ('dd.mm.yyyy')
Программа выбирает из этих 10-и 5 случайных людей, это можно реализовать с помощью модуля random и функции sample
После того как выбраны 5 случайных людей, предлагаем пользователю ввести их дату рождения
пользователь вводит дату в формате 'dd.mm.yyyy'
если пользователь ответил неверно, то выводим правильный ответ, но уже в следующем виде: третье января 2009 года
В конце считаем количество правильных и неправильных ответов и предлагаем начать снова
'''
import random
famous_list = [
    ('Ньютон', '25.12.1642'),
    ('Колумб', '31.10.1451'),
    ('Энштейн', '14.03.1879'),
    ('Шекспир', '26.04.1564'),
    ('Дарвин', '12.02.1809'),
    ('Коперник', '19.02.1473'),
    ('Наполеон', '15.08.1769'),
    ('Максвел', '13.06.1831'),
    ('Вашингтон', '22.02.1731'),
    ('Маркс', '05.05.1818')]
days_list = (
    'первое', 'второе', 'третье', 'четвёртое', 'пятое',
    'шестое', 'седьмое', 'восьмое','девятое', 'десятое',
    'одиннадцатое', 'двенадцатое', 'тринадцатое', 'четырнадцатое', 'пятнадцатое',
    'шестнадцатое','семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое',
    'двадцать первое', 'двадцать второе', 'двадцать третье', 'двадацать четвёртое', 'двадцать пятое',
    'двадцать шестое','двадцать седьмое', 'двадцать восьмое', 'двадцать девятое', 'тридцатое',
    'тридцать первое')
months_list = (
    'января',
    'февраля',
    'марта',
    'апреля',
    'мая',
    'июня',
    'июля',
    'августа',
    'сентября',
    'октября',
    'ноября',
    'декабря')
user_choice = 'Y'
while user_choice == 'Y':
    questions = 3
    random_list = random.sample(famous_list, questions)
    true_answer = 0
    for element in random_list:
        birthday = input(f'Введите день рождения {element[0]}а в формате dd.mm.yyyy: ')
        if birthday == element[1]:
            true_answer += 1
        else:
            birthday_split = element[1].split('.')
            print(f'Правильный ответ: {days_list[int(birthday_split[0]) - 1]} {months_list[int(birthday_split[1]) - 1]} {birthday_split[2]} года')
    print('количество правильных ответов:', true_answer)
    print('количество неправильных ответов:', questions - true_answer)
    user_choice = input('Если хотите начать снова нажмите  Y: ')
    if user_choice != 'Y':
        break
