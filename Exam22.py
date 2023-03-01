import random
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

count_list_1=int(input("Введите количество элементов первого списка: "))
count_list_2=int(input("Введите количество элементов второго списка: "))
list_1=[random.randint(0,10) for i in range(count_list_1)]
list_2=[random.randint(0,10) for i in range(count_list_2)]
total_list=[]

if count_list_1>count_list_2:
    for i in range(len(list_1)):
        if list_1[i] in list_2:
            if list_1[i] not in total_list:
                total_list.append(list_1[i])
total_list.sort()
print(list_1)
print(list_2)
print(total_list)
