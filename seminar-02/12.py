raw = input()
for i in raw:
    if not i.isdigit():
        raw = raw.replace(i, '')

print(int(raw) + 1)
