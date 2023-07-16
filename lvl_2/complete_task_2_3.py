# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!

def switch_it_up(number):
  """Принимает цифры от 0 до 9 и возвращает их значение прописью."""
  numeric = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  number_in_words = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    }
  while number in numeric:
    return(number_in_words[number])
    
  while number not in numeric:
    break
    
  

print(switch_it_up(1.4))