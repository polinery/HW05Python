''' 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке. '''

f = open('my_file.txt')
txt = f.readlines()
print(f'Количество строк в файле - {len(txt)}')

for i in range(len(txt)):
    flag = 0
    word = 0
    for j in txt[i]:
        if j != ' ' and flag == 0:
            word += 1
            flag = 1
        elif j == ' ':
            flag = 0
    print(f'в строке {i + 1} - {word} слов(а/о)')
