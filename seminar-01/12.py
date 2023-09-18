surface_width = float(input())
surface_height = float(input())
paint_cons = float(input())
volume = int(input())
stock_percent = int(input())

print(round(surface_height * surface_width, 2))
print(round(volume * stock_percent / paint_cons, 2))
print((surface_height * surface_width) // volume + 1)
