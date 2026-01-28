import random
a = 1
krubl = 76.55
def play():
    rand = random.randint(1, 6)
    print("Поздравляю! ваше число:", rand)
def chit_1():
    print("Что вы хотите посчитать?\n"
          "1. Валюты💸\n"
          "2. Цифры")
def vib_1():
    print(first_number - second_number)
def vib_2():
        print(second_number - first_number)
def vib_3():
    print(first_number + second_number)
def vib_4():
    print(first_number * second_number)
def vib_5():
        print(first_number / second_number)
def vib_6():
        print(second_number / first_number)
def vib_7():
        print(first_number ** second_number)
def vib_8():
        print(second_number ** first_number)
    
while a == 1:
    print("Выберите что бы вы хотели сделать:\n"
      "1. Кинуть кубик👾\n"
      "2. Посчитать🤓\n")

    first_v = int(input())
    if first_v == 1:
        play()
    elif first_v == 2:
        chit_1()
        shitat = int(input())
        if shitat == 1:
            print("Сколько Долларов вы хотите перевести в рубли?")
            vall = int(input())
            print(vall*krubl,'₽')
        elif shitat == 2:
            print("Введите два числа")
            first_number = float(input())
            second_number = float(input())
            print("Выберите что бы вы хотели сделать\n"
                  "1. Из 1 числа вычесть второе\n"
                  "2. Из 2 числа вычесть первое\n"
                  "3. Сложить числа\n"
                  "4. Умножить числа\n"
                  "5. 1 число разделить на второе\n"
                  "6. 2 чсило разделить на первое\n"
                  "7. 1 число возвести в степень второго числа\n"
                  "8. 2 число возевсти в степень первого числа")
            big_vibor = int(input())
            if big_vibor == 1:
                vib_1()
            elif big_vibor == 2:
                vib_2()
            elif big_vibor == 3:
                vib_3()
            elif big_vibor == 4:
                vib_4()
            elif big_vibor == 5:
                vib_5()
            elif big_vibor == 6:
                vib_6()
            elif big_vibor == 7:
                vib_7()
            elif big_vibor == 8:

                vib_8()
