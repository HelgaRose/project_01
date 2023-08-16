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


def remove_word_with_one_em(text):

  words = text.split(' ')
  words2=[]
  for i in range(0, len(words)):
    if words[i].find('!') != words[i].rfind('!'):
      words2.append(words[i])
    elif words[i].find('!') == -1:
      words2.append(words[i])
  print(' '.join(words2))  

remove_word_with_one_em('!Слово слово!!! Сло!во слово слово! еще !слово и слово') 