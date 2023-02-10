# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

import os

def exponentiation (number1,number2):
    if number2 == 0:
        return 1
    elif number2 == 1:
        return number1
    else:
        number1 = number1*exponentiation(number1, number2-1)
        return number1

os.system('CLS')
print ("Возводим число А в целую степень В")

a = float(input("Введите число А=> "))
b = int(input("Введите число B=> "))
print(f"Результат возведения в степень: {exponentiation(a,b)}")













