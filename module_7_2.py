def custom_write(file_name, strings):
    strings_positions = {}
    string_number = 0
    file = open(file_name, 'w', encoding='utf-8')
    for line_write in strings:
        begin_byte = file.tell()
        string_number += 1
        dict_index = (string_number, begin_byte)
        strings_positions[dict_index] = line_write
        file.write(str(line_write) + '\n')

    file.close()
    return strings_positions


info = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!']
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
