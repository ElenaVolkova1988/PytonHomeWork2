# Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

num=int(input(' Input a number: '))
lst = [round((1+1/i)**i, 2) for i in range(1, num+1)]
print(lst)
print (sum(lst))