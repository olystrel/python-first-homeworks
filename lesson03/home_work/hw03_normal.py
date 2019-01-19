# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
   
	i = 2
	list1 = [1, 1]
	while i < m:
		a = list1[i - 1] + list1[i - 2]
		list1.append(a)
		i = i + 1
	return list1[n-1: m]


print(fibonacci(3, 5))
print(fibonacci(4, 100))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    	b = origin_list
	c = True

	while c:
		c = False
		i = 0
		while i < len(b) - 1:
			h = b[i]
			l = b[i + 1]
			if h > l:
				b[i] = l
				b[i + 1] = h
				c = True
			i = i + 1

	return b


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def my_filter(foo, lst):
    return [x for x in lst if foo(x)]


my_foo = lambda x: x > 0
my_lst = [-2, 1, 0, -5, 8]
print(my_filter(my_foo, my_lst))



# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def are_parallel(x1, y1, x2, y2):
    return x1 * y2 - y1 * x2 == 0 #условие параллельности векторов (x1, y1) и (x2, y2)

def is_parallelogram(x1, y1, x2, y2, x3, y3, x4, y4):
    return (are_parallel(x2 - x1, y2 - y1, x3 - x4, y3 - y4) and are_parallel(x3 - x2, y2 - y3, x4 - x1, y4 - y1)) \
        or (are_parallel(x3 - x1, y3 - y1, x2 - x4, y2 - y4) and are_parallel(x2 - x3, y2 - y3, x1 - x4, y1 - y4))

print(is_parallelogram(0, 0, 1, 1, 2, 1, 1, 0))
