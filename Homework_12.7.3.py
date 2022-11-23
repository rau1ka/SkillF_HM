money = int(input("Введите сумму вклада:"))

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = [] 
for i in per_cent:
    deposit.append(per_cent[i]*money /100)

print(deposit)
print(f"Максимальная сумма, которую вы можете заработать: {max(deposit)}")