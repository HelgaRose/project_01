# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"


def remove_exclamation_marks(s: str) -> str:
 """Удаляет из текста все знаки "!"."""
 text = s
 i = text.find('!')
 while 0 <= i < len(text)-1:
    text = text[:i] + text[i+1:]
    i = text.find('!')
 if i == len(text) - 1:
    text = text[:len(text) - 1]
 return(text)

print(remove_exclamation_marks('!Чмоки! Всех!!! В этом чате!!!!'))

# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s: str) -> str:
 """Удаляет знак "!" в конце строки."""
 text = s
 i = text.rfind('!')
 if i == len(text) - 1:
     text = text[:len(text) - 1]
 return(text)

print(remove_last_em('Всем! Привет!!! Ура!'))

# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

# def remove_word_with_one_em(s):
#     pass