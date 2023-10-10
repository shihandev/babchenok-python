sale_rate = int(input('Введите скидку:'))
prices = []

while True:
    new_price = int(input())
    if new_price == 0:
        break
    else:
        prices.append(new_price)
        print(sum(prices) * sale_rate)
