# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них. 
# примеры:
# 1,4,8,7,5 -> 8

numbers_list = input("Введите 5 чисел, разделенных пробелом: ").split()
num_list = list(map(int, numbers_list))
print('Наибольшее число:', max(num_list))