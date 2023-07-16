# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!


def minimum(arr: list):
 """В списке целых чисел находит минимальное значение."""
 numbers = arr
 fmin = numbers[0]
 for i in numbers:
   if i < fmin:
    fmin = i
 return(f'Min = {fmin}')

print(minimum([3, 6, 4, -100]))

def maximum(arr: list):
 """В списке целых чисел находит максимальное значение."""
 numbers = arr
 fmax = numbers[0]
 for i in numbers:
   if i > fmax:
    fmax = i
 return(f'Max = {fmax}')

print(maximum([3, 6, 4, -100]))