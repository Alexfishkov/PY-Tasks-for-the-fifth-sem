# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# 2 2
# 4

import os

def addition (a,b):
    if a == 0:
        return b
    else:
        b = 1 + addition(a-1,b)
    return b
    
os.system('CLS')
print("Складываем два целых неотрицательных числа a и b методом рекурсии")
a = int(input("Введите число a=> "))
b = int(input("Введите число b=> "))

print(f"a+b = {addition(a,b)}")

