
file = open('POLSKA PANDA.txt', 'r', encoding='utf-8').read()
lines = file.split('\n')
ilosc = 0
for line in lines:
    if ('firstname,secondname' in line):
        print(line)
        ilosc += 1
print(ilosc)
