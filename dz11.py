def custom_write(file_name, strings):  #название файла для записи/список строк для записи
    dict_strings = {}
    strings_positions = 0
    file = open(file_name, 'a', encoding='utf-8')

    for string in strings: #позиции
        strings_positions += 1
        cursor = file.tell() #текст из файла
        dict_strings[(strings_positions, cursor)] = string
        file.write(string + '\n')  #
    file.close() #закрытие файла
    return dict_strings

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
