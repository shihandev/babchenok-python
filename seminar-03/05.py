num = int(input())
summ = sum([int(x) for x in str(num)])

if summ % 3 == 0 and (num % 10) % 2 == 0:
    print('Yes')
else:
    print('No')
