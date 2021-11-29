deposit = float(input('Введите сумму депозита: '))
total = float(input('Какую сумму вы хотите получить в конце?: '))
year_percent = float(input('Введите процентную ставку(в дробях): '))
month = 0

while deposit < total:
    deposit *= 1 + (year_percent / 12) / 100
    deposit = int(12 * deposit) / 12
    month += 1
print(deposit)
