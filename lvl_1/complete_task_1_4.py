# Задача 1.4.

# Есть словарь кодов товаров titles

titles = {
    'Кроссовки тип 3 (Adidas)': '100000110',
    'Мячик тип 2 (Adidas)': '100000146',
    'Кепка тип 1 (Adidas)': '100000149',
    'Ремень тип 2 (Nike)': '100000194',
    'Футболка тип 1 (Adidas)': '100000224',
    'Шапка тип 5 (Puma)': '100000280',
}

# Товары находятся на складе и сохранены в виде словаря списков словарей,
# которые отражают количество товаров в магазине по каждому коду.

store = {
    '100000110': [{'quantity': 31, 'price': 1637}],
    '100000146': [ {'quantity': 4, 'price': 45}, {'quantity': 10, 'price': 48}],
    '100000149': [ {'quantity': 28, 'price': 279}, {'quantity': 32, 'price': 291}],
    '100000194': [{'quantity': 8, 'price': 220}, {'quantity': 1, 'price': 170}],
    '100000224': [{'quantity': 61, 'price': 438}, {'quantity': 23, 'price': 302},  {'quantity': 50, 'price': 412}],
    '100000280': [{'quantity': 26, 'price': 175}, ]
}

# Рассчитайте на какую сумму лежит каждого товара на складе.
#
# Вывести суммарную стоимость каждого товара в магазине в формате:
# "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"

# Пример: "Кроссовки тип 3 (Adidas) - 31 шт, стоимость 50747 руб"

for code in store:
  number = store.get(code)
  if len(number) == 1:
    total_cost = number[0].get('quantity')*number[0].get('price')
    total_quantity = number[0].get('quantity')
  if len(number) == 2:
    total_cost = number[0].get('quantity')*number[0].get('price') + number[1].get('quantity')*number[1].get('price')
    total_quantity = number[0].get('quantity') + number[1].get('quantity')
  if len(number) == 3:
    total_cost = number[0].get('quantity')*number[0].get('price') + number[1].get('quantity')*number[1].get('price') + number[2].get('quantity')*number[2].get('price')
    total_quantity = number[0].get('quantity') + number[1].get('quantity') + number[2].get('quantity')
  for product in titles:
    if titles[product] == code:
      print(f'{product} - {total_quantity} шт, стоимость {total_cost}')
