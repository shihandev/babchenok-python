summ = 0
while True:
    new_sum = int(input())
    if new_sum == 0:
        break
    else:
        summ += new_sum

if summ % 2 == 0:
    while summ % 2 == 0:
        summ /= 2
    print('К оплате:', summ)
else:
    print(summ * 0.75)
