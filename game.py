import random

number = '1000'
c1 = number[0]
c2 = number[1]
c3 = number[2]
c4 = number[3]
print('''Привет, дорогой друг!
Я предлагаю тебе сыграть в быков и коров
Правила очень просты:
Тебе нужно отгадать четырехзначное число,
в котором все цифры отличны :) 
Если вдруг захочешь закончить игру - 
напиши стоп''')
while not (number.count(c1) == 1 and number.count(c2) == 1 and number.count(c3) == 1 and number.count(c4) == 1): # цикл, чтобы рандомное число подходило под условия
    number = str(random.randint(1000, 9999))
trial = input('Введите четырехзначное число: ')
if len(trial) != 4 or not (trial.isdigit()) or not (trial.count(trial[0]) == 1 and trial.count(trial[1]) == 1 and trial.count(trial[2]) == 1 and trial.count(trial[3]) == 1): #проверка числа
    while len(trial) != 4 or not (trial.isdigit()) or not (trial.count(trial[0]) == 1 and trial.count(trial[1]) == 1 and trial.count(trial[2]) == 1 and trial.count(trial[3]) == 1): #цикл, чтобы пользователь ввел подходящее число
        if trial == 'стоп':
            print('Вы завершили игру. Ваше число было:', number)
            break
        if not (trial.isdigit()):
            print('Число должно состоять только из цифр :)')
        elif len(trial) != 4:
            print('Число должно состоять из четырех цифр :)')
        elif not (trial.count(trial[0]) == 1 and trial.count(trial[1]) == 1 and trial.count(trial[2]) == 1 and trial.count(trial[3]) == 1):
            print('Цифры не должны повторяться :)')
        trial = input('Введите четырехзначное число: ')
else:
    while number != trial or trial != 'стоп':
        cow = 0
        bull = 0
        for ind1 in range(len(trial)): #проверка двух чисел на сходство
            for ind2 in range(len(number)):
                if trial[ind1] == number[ind2]:
                    if ind1 == ind2:
                        bull += 1
                    else:
                        cow += 1
        if bull == 4:
            print('Поздравляю, вы отгадали число!')
            break
        else:
            print('Количество быков:', bull)
            print('Количество коров:', cow)
        bull = 0
        cow = 0
        trial = input('Введите четырехзначное число: ')
        if len(trial) != 4 or not (trial.isdigit()) or not (trial.count(trial[0]) == 1 and trial.count(trial[1]) == 1 and trial.count(trial[2]) == 1 and trial.count(trial[3]) == 1): #проверка числа
            while len(trial) != 4 or not (trial.isdigit()) or not (trial.count(trial[0]) == 1 and trial.count(trial[1]) == 1 and trial.count(trial[2]) == 1 and trial.count(trial[3]) == 1): #цикл, чтобы пользователь ввел подходящее число
                if trial == 'стоп':
                    print('Вы завершили игру. Ваше число было:', number)
                    break
                if not (trial.isdigit()):
                    print('Число должно состоять только из цифр :)')
                elif len(trial) != 4:
                    print('Число должно состоять из четырех цифр :)')
                elif not (trial.count(trial[0]) == 1 and trial.count(trial[1]) == 1 and trial.count(trial[2]) == 1 and trial.count(trial[3]) == 1):
                    print('Цифры не должны повторяться :)')
                trial = input('Введите четырехзначное число: ')

