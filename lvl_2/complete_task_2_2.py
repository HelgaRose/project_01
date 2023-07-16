# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

def quarter_of(month):
  year = {
    1: 'Январь',
    2: 'Февраль',
    3: 'Март',
    4: 'Апрель',
    5: 'Май',
    6: 'Июнь',
    7: 'Июль',
    8: 'Август',
    9: 'Сентябрь',
    10: 'Октябрь',
    11: 'Ноябрь',
    12: 'Декабрь',
}
  if month > 12:
    return(f'Такого месяца нет')
  else:
    if month < 4:
      return(f'Месяц {month} ({year[month]}) является частью первого квартала')
    if 3 < month < 7:
      return(f'Месяц {month} ({year[month]}) является частью второго квартала')
    if 6 < month < 10:
      return(f'Месяц {month} ({year[month]}) является частью третьего квартала')
    if 9 < month <= 12:
      return(f'Месяц {month} ({year[month]}) является частью четвертого квартала')

print(quarter_of(9))

