import re
f = open('myFile.html', 'r')
s = f.read()
result = re.findall('[a-z0-9]+@[a-z]+\.[a-z]{2,3}', s)
if result:
    print("Результаты поиска: ", result)
    f.close()
else:
    print("Совпадений не найдено")
