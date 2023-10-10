while True:
    game = input('Выберите действие:').lower()
    if game == 'game':
        print('Угадай Число!')
        for i in range(3):
            if int(input()) == 5:
                print('Вы выиграли билет на концерт!')
                break
    elif game == 'off':
        break