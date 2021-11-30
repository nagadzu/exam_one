deposit = float(input('deposit: '))
end_deposit = float(input('end_deposit: '))
percent = float(input('percent: '))
month = 0

x = ((percent / 12) * deposit)
x += deposit

while x < end_deposit:
    x +=   ((percent / 12) * x)
    month += 1

    print(month)