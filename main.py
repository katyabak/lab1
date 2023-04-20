from pars import parse, save_to_file
if __name__ == "__main__":
    description = parse()  # вызываем функцию и сохраняем результат в переменную
    save_to_file(description, 'faculties.txt')  # вызываем функцию, передавая ей содержимое переменной description и имя файла для сохранения.
    parse()
