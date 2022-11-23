tickets = int(input('Сколько билетов хотите приобрести::'))
cost = 0
for i in range(tickets):
    age = int(input('Введите возраст посетителя:'))
    if age < 18:
        cost += 0
        print('Для лиц младше 18 лет вход бесплатный')
    elif 18 <= age < 25:
        cost += 990
        print('Стоимость билета 990руб.')
    else:
        cost += 1390
        print('Стоимость билета 1390руб.') 
    if tickets > 3:
        cost = cost * 0.9
print(f'Сумма к оплате: {round(cost)}руб.')