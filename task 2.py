def get_count_char(str_):
    abc_dict = {}
    str_ = "".join(str_.split())
    str_ = str_.lower()

    for sign in str_:
        if sign.isalpha():
            if sign in abc_dict:
                abc_dict[sign] += 1
            else:
                abc_dict[sign] = 1

    return abc_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
def get_percent_char(abc_dict):
    length = sum(abc_dict.values())
    for sign in abc_dict:
        abc_dict[sign] = round(abc_dict.get(sign) * 100 / length, 1)
    return abc_dict

