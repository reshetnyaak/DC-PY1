main_str - """
   Данное предложение будет разбиваться на отдельные слова.
   В качествер разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов.
   Далее нужно отсортировать слова в алфавитном порядке, а после сртировки склеить их с помощью метода строк join. Приступим !!!!
"""

low_main_str = main_str.lower()
print(low_main_str)
letter_dict = {}
def get_count_char(str_):
    for letter in low_main_str:
           if low_main_str.isalpha():
               if letter in dict_:
                   letter_dict[letter] += 1
               else:
                   letter_dict[letter] = 1
    return letter_dict

print(get_count_char(main_str))
