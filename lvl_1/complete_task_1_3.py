# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!

month = {
    1: ['Январь', '31 день'],
    2: ['Февраль', '28 дней'],
    3: ['Март', '31 день'],
    4: ['Апрель', '30 дней'],
    5: ['Май', '31 день'],
    6: ['Июнь', '30 дней'],
    7: ['Июль', '31 день'],
    8: ['Август', '31 день'],
    9: ['Сентябрь', '30 дней'],
    10: ['Октябрь', '31 день'],
    11: ['Ноябрь', '30 дней'],
    12: ['Декабрь', '31 день'],
}

m = int(input('Введите номер месяца '))
if m > 12:
  print('Такого месяца нет')
else:
  print(f'Вы ввели {month[m][0]}. В этом месяце {month[m][1]}') 