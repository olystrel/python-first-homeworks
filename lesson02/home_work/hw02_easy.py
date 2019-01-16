# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

print("Решение первого задания")
fruits=["яблоко", "банан", "киви", "клубника"]
for index, value in enumerate(fruits, 1):
	print("{}. {}".format(index, value))



# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

print("Решение второго задания")
fruits=["яблоко", "банан", "арбуз", "ананас"]
fruits_second=["яблоко", "банан", "голубика", "клубника"]
print(fruits)
print(fruits_second)

fruits_basket= set(fruits)
fruits_basket_second= set(fruits_second)

fruits_basket.difference_update(fruits_basket_second)
print(fruits_basket)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
print("Первое решение третьего  задания")
numbers=[1, 2, 3, 4, 5, 8]
print(numbers)
numbers_second = numbers.copy()

numbers_second=[i/4 if i % 2 ==0  else i*2 for i in numbers_second]
print(numbers_second)

#2решение

print("Второе решение третьего задания")
numbers=[1, 2, 3, 4, 5, 8]  
numbers_second=[i/4 if i % 2 == 0  else i*2 for i in numbers]
print(numbers_second)
