# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:



# ################СОЗДАНИЕ ТАБЛИЦЫ##################
# import sqlite3
# connection = sqlite3.connect("teachers_hw.db")
# cursor = connection.cursor()
# query = """CREATE TABLE Students (
# Student_Id Integer, 
# Student_Name Text, 
# School_Id Integer Primary key);"""
# cursor.execute(query)
# connection.commit()
# connection.close()


# ################ЗАПОЛНЕНИЕ ТАБЛИЦЫ################

# import sqlite3

# connection = sqlite3.connect("teachers_hw.db")
# cursor = connection.cursor()
# query = """INSERT INTO Students (Student_Id, Student_Name, School_Id)
# VALUES
# (201, 'Иван', 1),
# (202, 'Петр', 2),
# (203, 'Анастасия', 3),
# (204, 'Игорь', 4);"""
# cursor.execute(query)
# connection.commit()
# connection.close()

# import sqlite3

# def get_connection():
#   connection = sqlite3.connect("teachers_hw.db")
#   return connection

# def close_connection(connection):
#   if connection :
#     connection.close()

# def records(): 
#   try:
#     connection= get_connection()
#     cursor = connection.cursor()
#     cursor.execute("SELECT * FROM Students")
#     records = cursor.fetchall()
#     print("Ваш запрос: ", records)
#     close_connection(connection)
#   except (Exception, sqlite3.Error) as error:
#     print("Ошибка получения данных:", error)


# records()

# ################ИНФОРМАЦИЯ О СТУДЕНТЕ################
import sqlite3

def get_connection():
  connection = sqlite3.connect("teachers_hw.db")
  return connection

def close_connection(connection):
  if connection :
    connection.close()

def student_info(student_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    sql_query = "SELECT * FROM Students JOIN School ON Students.School_Id = School.School_Id WHERE Students.Student_Id = ?"
    cursor.execute(sql_query,(student_id,))
    records = cursor.fetchall()
    # print(records)
    close_connection(connection)
    print("Данные по студенту:")
    for row in records:
      print("ID студента:", row[0])
      print("Имя студента:", row[1])
      print("ID школы:", row[2])
      print("Название школы:", row[4],'\n')
  except (Exception, sqlite3.Error) as error:
    print("Ошибка получения данных:", error)

student_info(204)