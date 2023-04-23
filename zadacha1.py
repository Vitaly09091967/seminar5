# Задача 26:  Посчитать факториал (произведение 1 до N) и треугольное число 
# (сумма чисел от 1 до N) для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def triang_num(n):
    if n == 1:
        return 1
    else:
        return n + triang_num(n-1)

n = int(input("Введите число N: "))
print("Факториал числа", n, "равен", factorial(n))
print("Треугольное число для", n, "равно", triang_num(n))