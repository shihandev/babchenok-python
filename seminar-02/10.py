num = '+ 7 (123) 234 - 56 - 78'
for i in num:
    if not i.isdigit() and i != '+':
        num = num.replace(i, '')

print(num)
