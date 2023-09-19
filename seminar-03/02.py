to_pay = float(input())
time = int(input())
sale_rate = 1
if 8 <= time <= 22:
    if 10 <= time <= 12:
        sale_rate = 0.5
    elif 20 <= time <= 22:
        sale_rate = 0.25
    print(to_pay * sale_rate)
else:
    print('Магазин закрыт!')
