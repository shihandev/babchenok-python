items = [int(input()) for i in range(3)]

if items[0] < items[1] < items[2]:
    print('Акция!')
    print('К оплате:', sum(items) / 2)
elif items[0] > items[1] > items[2]:
    print('Акция!')
    print('К оплате:', sum(items) / 3)
else:
    print('К оплате:', sum(items))
