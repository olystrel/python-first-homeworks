# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

lst=[1, 2, 4, 0]
lst1=[i**2 for i in lst]
print(lst1)


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
lst=["яблоко","ананас","банан","манго"]
lst1=["яблоко","клубника","банан","маракуйя"]
lst3=[i for i in lst and lst1 if i in lst and lst1]
print(lst3)


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

lst= [1, 2, 4, 0, 9, 15]
lst1=[i for i in lst if i%3==0 and i>0 and i%4 !=0]
print(lst1)

