baza = {'Дили': set(), 'Били': set(), 'Вили': set()}
a = input()
while a != 'конец':
    name, liker = a.split(': ')
    baza[name].add(liker)
    a=input()
for k, val in sorted(baza.items(),key=lambda item: -len(item[1])):
    print(f'Количество уникальных комментаторов у {k} - {len(val)}')
