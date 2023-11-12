import math
from pyfiglet import Figlet
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
#import sys

preview_text = Figlet(font='Small') #Whimsy, Small
print(preview_text.renderText('MATH'))

input_language = str(input("Select language (ru/en): "))

while True:
    if input_language == "ru":
        print("[0] Выход\n[1] Сумма x и y\n[2] Разница x и y\n[3] Произведение чисел x и y\n[4] Деление x на y, остаток от деления x на y\n[5] График функции\n[6] Возведение числа (х) в степень (у)\n[7] Квадратный корень числа x\n[8] Синус x\n[9] Косинус x\n[10] Тангенс x\n[11] Логарифм x\n[12] Вычислить гипотенузу треугольника с катетами х и у\n[13] Modulus of number x\n[14] Факториал числа x\n[15] Число Пи")
        input_number = int(input("Выберите номер операции: "))

        if input_number == 0:
            break

        if input_number == 1:
            while True:
                try:
                    user_number11 = float(input("Введите первое слогаемое: "))
                    user_number12 = float(input("Введите второе слогаемое: "))
                    sum = math.fsum([user_number11, user_number12])
                    print(f"{user_number11} + {user_number12}= {sum}")
                    continue_or_exit = input("Хотите продолжить вычислять сумму чисел? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break
                except ValueError:
                    print("Ошибка ввода")
                    continue_or_exit = input("Хотите продолжить вычислять сумму чисел? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break

        if input_number == 2:
            while True:
                try:
                    user_number21 = float(input("Введите уменьшаемое: "))
                    user_number22 = float(input("Введите вычитаемое: "))
                    diff = math.fsum([user_number21, -user_number22])
                    print(f"{user_number21} - {user_number22}= {diff}")
                    continue_or_exit = input("Хотите продолжить вычислять разницу чисел? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break
                except ValueError:
                    print("Ошибка ввода")
                    continue_or_exit = input("Хотите продолжить вычислять разницу чисел? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break

        if input_number == 3:
            while True:
                try:
                    user_number31 = float(input("Введите первый множитель: "))
                    user_number32 = float(input("Введите второй множитель: "))
                    prod = math.prod([user_number31, user_number32])
                    print(f"{user_number31} * {user_number32}= {prod}")
                    continue_or_exit = input("Хотите продолжить вычислять произведение чисел? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break
                except ValueError:
                    print("Ошибка ввода")
                    continue_or_exit = input("Хотите продолжить вычислять произведение чисел? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break

        if input_number == 4:
            while True:
                try:
                    user_number41 = float(input("Введите делимое: "))
                    user_number42 = float(input("Введите делитель: "))
                    if user_number42 == 0:
                        print("Деление на ноль невозможно")
                        continue_or_exit = input("Хотите продолжить вычислять частное чисел? (y/n): ")
                        if continue_or_exit.lower() != "y":
                            break
                    else:
                        div = math.prod([user_number41, 1 / user_number42])
                        fmod = math.fmod(user_number41, user_number42)
                        print(f"{user_number41} / {user_number42}= {div}\nОстаток: {fmod}")

                        continue_or_exit = input("Хотите продолжить вычислять частное чисел? (y/n): ")
                        if continue_or_exit.lower() != "y":
                            break

                except ValueError:
                    print("Ошибка ввода")
                    continue_or_exit = input("Хотите продолжить вычислять частное чисел? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break

        if input_number == 5:
            while True:
                print(
                    "Инструкция:\nПлюс: +\nМинус: -\nУмножить: *\nРазделить: /\nВозвести в степень: **\nПример правильного запроса: x**2 + 2*x - 4")
                ex = input("Введите функцию: ")
                x = sp.symbols('x')
                try:
                    parsed_ex = sp.sympify(ex)
                    f = sp.lambdify(x, parsed_ex, 'numpy')
                    x_values = np.linspace(-50, 50, 500)
                    y_values = f(x_values)
                    plt.plot(x_values, y_values)
                    plt.title(f'График функции y = {ex}')
                    # plt.xlabel('x')
                    # plt.ylabel('y')
                    plt.axhline(0, color='black', linewidth=0.5)
                    plt.axvline(0, color='black', linewidth=0.5)
                    plt.xlim(-20, 20)
                    plt.ylim(-20, 20)
                    plt.show()
                    continue_or_exit = input("Хотите продолжить рисовать график функции? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break
                except (sp.SympifyError, ValueError):
                    print("Ошибка ввода функции")
                    continue_or_exit = input("Хотите продолжить рисовать график функции? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break

        if input_number == 14:
            while True:
                try:
                    user_number14 = int(input("Введите число, факториал которого вы хотите узнать: "))
                    factorial = math.factorial(user_number14)
                    print(f"Факториал числа {user_number14}: {factorial}")

                    continue_or_exit = input("Хотите продолжить вычислять факториал? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break
                except ValueError:
                    print("Ошибка ввода")
                    continue_or_exit = input("Хотите продолжить вычислять факториал? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break

        if input_number == 13:
            while True:
                try:
                    user_number13 = float(input("Введите число, модуль которого вы хотите узнать: "))
                    fabs = math.fabs(user_number13)
                    print(f"Модуль числа {user_number13}: {fabs}")
                    continue_or_exit = input("Хотите продолжить вычислять модуль? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break
                except ValueError:
                    print("Ошибка ввода")
                    continue_or_exit = input("Хотите продолжить вычислять модуль чисел? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break

        if input_number == 7:
            while True:
                try:
                    user_number7 = float(input("Введите число, квадратный корень которого вы хотите узнать: "))
                    sqrt = math.sqrt(user_number7)
                    print(f"Квадратный корень числа {user_number7}: {sqrt}")
                    continue_or_exit = input("Хотите продолжить вычислять квадратный корень? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break
                except ValueError:
                    print("Ошибка ввода")
                    continue_or_exit = input("Хотите продолжить вычислять квадратный корень? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break

        if input_number == 8:
            while True:
                try:
                    user_number8 = float(input("Введите число, синус которого вы хотите узнать: "))
                    sin = math.sin(user_number4)
                    print(f"Синус угла {user_number8}: {sin}")
                    continue_or_exit = input("Хотите продолжить вычислять синус? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break
                except ValueError:
                    print("Ошибка ввода")
                    continue_or_exit = input("Хотите продолжить вычислять синус? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break

        if input_number == 9:
            while True:
                try:
                    user_number5 = float(input("Введите число, косинус которого вы хотите узнать: "))
                    cos = math.cos(user_number9)
                    print(f"Косинус угла {user_number9}: {cos}")
                    continue_or_exit = input("Хотите продолжить вычислять косинус? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break
                except ValueError:
                    print("Ошибка ввода")
                    continue_or_exit = input("Хотите продолжить вычислять косинус? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break

        if input_number == 10:
            while True:
                try:
                    user_number10 = float(input("Введите число, тангенс которого вы хотите узнать: "))
                    tan = math.tan(user_number6)
                    print(f"Тангенс угла {user_number10}: {tan}")
                    continue_or_exit = input("Хотите продолжить вычислять тангенс? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break
                except ValueError:
                    print("Ошибка ввода")
                    continue_or_exit = input("Хотите продолжить вычислять тангенс? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break

        if input_number == 11:
            while True:
                try:
                    user_number11 = float(input("Введите число, логарифм которого вы хотите узнать: "))
                    log = math.log(user_number11)
                    print(f"Логарифм {user_number11}: {log}")
                    continue_or_exit = input("Хотите продолжить вычислять логарифм? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break
                except ValueError:
                    print("Ошибка ввода")
                    continue_or_exit = input("Хотите продолжить вычислять логарифм? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break

        if input_number == 12:
            while True:
                try:
                    user_number121 = float(input("Введите длину первого катета (без едениц измерения): "))
                    user_number122 = float(input("Введите длину второго катета (без едениц измерения): "))
                    hypot = math.hypot(user_number121, user_number122)
                    print(f"Гипотенуза с катетами {user_number121, user_number122}: {hypot}")
                    continue_or_exit = input("Хотите продолжить вычислять гипотенузу? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break
                except ValueError:
                    print("Ошибка ввода")
                    continue_or_exit = input("Хотите продолжить вычислять гипотенузу? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break

        if input_number == 15:
            while True:
                pi = math.pi
                print(f"Число Пи: {pi}")

                continue_or_exit = input("Хотите продолжить вычислять число Пи? (y/n): ")
                if continue_or_exit.lower() != "y":
                    break

        if input_number == 6:
            while True:
                try:
                    user_number61 = float(input("Введите число, которое хотите возвести в степень: "))
                    user_number62 = float(input("Введите степень, в который будете возводить число: "))
                    pow = math.pow(user_number61, user_number62)
                    print(f"Число {user_number61} в степени {user_number62}= {pow}")
                    continue_or_exit = input("Хотите продолжить возводить числа в степень? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break
                except ValueError:
                    print("Ошибка ввода")
                    continue_or_exit = input("Хотите продолжить возводить числа в степень? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break
    if input_language == "en":
        print("[0] Exit\n[1] Sum of x and y\n[2] Difference between x and y\n[3] Product of numbers x and y\n[4] Division of x by y, remainder of x divided by y\n[5] Graph of a function\n[6] Exponentiation of a number (x) to a power (y)\n[7] Square root of x\n[8] Sine of x\n[9] Cosine of x\n[10] Tangent of x\n[11] Logarithm of x\n[12] Calculate the hypotenuse of a triangle with legs x and y\n[13] Absolute value of x\n[14] Factorial of x\n[15] Value of Pi")
        input_number = int(input("Choose the operation number: "))

        if input_number == 0:
            break

        if input_number == 1:
            while True:
                try:
                    user_number11 = float(input("Enter the first addend: "))
                    user_number12 = float(input("Enter the second addend: "))
                    sum_result = math.fsum([user_number11, user_number12])
                    print(f"{user_number11} + {user_number12}= {sum_result}")
                    continue_or_exit = input("Do you want to continue calculating the sum? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break
                except ValueError:
                    print("Input error")
                    continue_or_exit = input("Do you want to continue calculating the sum? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break

        if input_number == 2:
            while True:
                try:
                    user_number21 = float(input("Enter the minuend: "))
                    user_number22 = float(input("Enter the subtrahend: "))
                    diff_result = math.fsum([user_number21, -user_number22])
                    print(f"{user_number21} - {user_number22}= {diff_result}")
                    continue_or_exit = input("Do you want to continue calculating the difference? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break
                except ValueError:
                    print("Input error")
                    continue_or_exit = input("Do you want to continue calculating the difference? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break

        if input_number == 3:
            while True:
                try:
                    user_number31 = float(input("Enter the first factor: "))
                    user_number32 = float(input("Enter the second factor: "))
                    prod_result = math.prod([user_number31, user_number32])
                    print(f"{user_number31} * {user_number32}= {prod_result}")
                    continue_or_exit = input("Do you want to continue calculating the product? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break
                except ValueError:
                    print("Input error")
                    continue_or_exit = input("Do you want to continue calculating the product? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break

        if input_number == 4:
            while True:
                try:
                    user_number41 = float(input("Enter the dividend: "))
                    user_number42 = float(input("Enter the divisor: "))
                    if user_number42 == 0:
                        print("Division by zero is not possible")
                        continue_or_exit = input("Do you want to continue calculating the quotient? (y/n): ")
                        if continue_or_exit.lower() != "y":
                            break
                    else:
                        quotient_result = math.prod([user_number41, 1 / user_number42])
                        remainder_result = math.fmod(user_number41, user_number42)
                        print(f"{user_number41} / {user_number42}= {quotient_result}\nRemainder: {remainder_result}")

                        continue_or_exit = input("Do you want to continue calculating the quotient? (y/n): ")
                        if continue_or_exit.lower() != "y":
                            break
                except ValueError:
                    print("Input error")
                    continue_or_exit = input("Do you want to continue calculating the quotient? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break

        if input_number == 5:
            while True:
                print(
                    "Instructions:\nAddition: +\nSubtraction: -\nMultiplication: *\nDivision: /\nExponentiation: **\nExample of a valid input: x**2 + 2*x - 4")
                ex = input("Enter the function: ")
                x = sp.symbols('x')
                try:
                    parsed_ex = sp.sympify(ex)
                    f = sp.lambdify(x, parsed_ex, 'numpy')
                    x_values = np.linspace(-50, 50, 500)
                    y_values = f(x_values)
                    plt.plot(x_values, y_values)
                    plt.title(f'Graph of the function y = {ex}')
                    plt.axhline(0, color='black', linewidth=0.5)
                    plt.axvline(0, color='black', linewidth=0.5)
                    plt.xlim(-20, 20)
                    plt.ylim(-20, 20)
                    plt.show()
                    continue_or_exit = input("Do you want to continue drawing the graph of the function? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break
                except (sp.SympifyError, ValueError):
                    print("Input error in the function")
                    continue_or_exit = input("Do you want to continue drawing the graph of the function? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break

        if input_number == 14:
            while True:
                try:
                    user_number14 = int(input("Enter the number for which you want to calculate the factorial: "))
                    factorial_result = math.factorial(user_number14)
                    print(f"The factorial of {user_number14}: {factorial_result}")

                    continue_or_exit = input("Do you want to continue calculating the factorial? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break
                except ValueError:
                    print("Input error")
                    continue_or_exit = input("Do you want to continue calculating the factorial? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break

        if input_number == 13:
            while True:
                try:
                    user_number13 = float(input("Enter the number for which you want to calculate the modulus value: "))
                    abs_result = math.fabs(user_number13)
                    print(f"The absolute value of {user_number13}: {abs_result}")
                    continue_or_exit = input("Do you want to continue calculating the modulus value? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break
                except ValueError:
                    print("Input error")
                    continue_or_exit = input("Do you want to continue calculating the absolute value? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break

        if input_number == 7:
            while True:
                try:
                    user_number7 = float(input("Enter the number for which you want to calculate the square root: "))
                    sqrt_result = math.sqrt(user_number7)
                    print(f"The square root of {user_number7}: {sqrt_result}")
                    continue_or_exit = input("Do you want to continue calculating the square root? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break
                except ValueError:
                    print("Input error")
                    continue_or_exit = input("Do you want to continue calculating the square root? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break

        if input_number == 8:
            while True:
                try:
                    user_number8 = float(input("Enter the number for which you want to calculate the sine: "))
                    sin_result = math.sin(user_number8)
                    print(f"The sine of angle {user_number8}: {sin_result}")
                    continue_or_exit = input("Do you want to continue calculating the sine? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break
                except ValueError:
                    print("Input error")
                    continue_or_exit = input("Do you want to continue calculating the sine? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break

        if input_number == 9:
            while True:
                try:
                    user_number9 = float(input("Enter the number for which you want to calculate the cosine: "))
                    cos_result = math.cos(user_number9)
                    print(f"The cosine of angle {user_number9}: {cos_result}")
                    continue_or_exit = input("Do you want to continue calculating the cosine? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break
                except ValueError:
                    print("Input error")
                    continue_or_exit = input("Do you want to continue calculating the cosine? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break

        if input_number == 10:
            while True:
                try:
                    user_number10 = float(input("Enter the number for which you want to calculate the tangent: "))
                    tan_result = math.tan(user_number10)
                    print(f"The tangent of angle {user_number10}: {tan_result}")
                    continue_or_exit = input("Do you want to continue calculating the tangent? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break
                except ValueError:
                    print("Input error")
                    continue_or_exit = input("Do you want to continue calculating the tangent? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break

        if input_number == 11:
            while True:
                try:
                    user_number11 = float(input("Enter the number for which you want to calculate the logarithm: "))
                    log_result = math.log(user_number11)
                    print(f"The logarithm of {user_number11}: {log_result}")
                    continue_or_exit = input("Do you want to continue calculating the logarithm? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break
                except ValueError:
                    print("Input error")
                    continue_or_exit = input("Do you want to continue calculating the logarithm? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break

        if input_number == 12:
            while True:
                try:
                    user_number121 = float(input("Enter the length of the first leg (without units): "))
                    user_number122 = float(input("Enter the length of the second leg (without units): "))
                    hypot_result = math.hypot(user_number121, user_number122)
                    print(f"The hypotenuse with legs {user_number121, user_number122}: {hypot_result}")
                    continue_or_exit = input("Do you want to continue calculating the hypotenuse? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break
                except ValueError:
                    print("Input error")
                    continue_or_exit = input("Do you want to continue calculating the hypotenuse? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break

        if input_number == 15:
            while True:
                pi = math.pi
                print(f"The value of Pi: {pi}")

                continue_or_exit = input("Do you want to continue calculating the value of Pi? (y/n): ")
                if continue_or_exit.lower() != "y":
                    break

        if input_number == 6:
            while True:
                try:
                    user_number61 = float(input("Enter the number you want to raise to a power: "))
                    user_number62 = float(input("Enter the power to which the number will be raised: "))
                    pow_result = math.pow(user_number61, user_number62)
                    print(f"The number {user_number61} raised to the power {user_number62}= {pow_result}")
                    continue_or_exit = input("Do you want to continue raising numbers to a power? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break
                except ValueError:
                    print("Input error")
                    continue_or_exit = input("Do you want to continue raising numbers to a power? (y/n): ")
                    if continue_or_exit.lower() != "y":
                        break