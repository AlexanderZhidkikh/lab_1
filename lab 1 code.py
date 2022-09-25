import csv
import random

with open('books.csv') as csv_file:
    table = list(csv.reader(csv_file, delimiter = ';'))

    #1

    print("Количество записей:", len(table)-1)

    #2

    count = 0
    for row in table[1:]:
        if len(row[1])>30:
            count += 1
    print('Количество записей у которых в поле "Название" более 30 символов:', count, end="\n\n")
    
    #3
    print("Поиск книги по автору")
    author = input('Введите имя автора: ')

    print("Книги по запросу " + author + ":", end="\n\n")
    for row in table[1:]:
        if author in row[4]:
            date = int(row[6][6:10])
            if date in {2014, 2016, 2017}:
                print(row[1])

    #4

    with open('Библиографические ссылки.txt','w') as ft4:
        for i in range(1,21):
            row = random.randint(1, len(table))
            aut = table[row][4]
            book = table[row][1]
            year = table[row][6][0:4]
            s = f'{i}. {aut}. {book} - {year}'
            ft4.write(s + '\n')
    print()

    #1 dop

    tags = set()
    print("Все теги без повторений:", end="\n\n")
    for row in table:
        temp = row[12].split('#')[1:]
        for el in temp:
            tags.add('#'+el)
    print(*tags, sep='\n', end="\n\n")

    #2 dop
    print("20 самых популярных книг:", end="\n\n")
    list_count = []
    list_name = []

    for row in table[1:]:
        list_count.append(row[8])
        list_name.append(row[1])

    for i in range(1, 21):
        el = max(list_count)
        index = list_count.index(el)
        print(f'{i}. {list_name[index]}')
        del list_count[index]
        del list_count[index]
