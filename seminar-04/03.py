login = input()

banned_symbols = '=?^$№@_'

for i in banned_symbols:
    if i in login:
        print(f'Запрещённый символ {i}!')