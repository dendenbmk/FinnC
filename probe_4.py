list_otkaz = [1, 2, 3, 4]
list_zakaz = [4, 5, 6, 7, 8, 9]

a = 4
if a in list_otkaz:
    print(a,  'list otkaz', 'if, elif')
elif a in list_zakaz:
    print(a, 'list_zakaz', 'if, elif')

print()

a = 4
if a in list_otkaz:
    print(a,  'list otkaz', 'if, if')
if a in list_zakaz:
    print(a, 'list_zakaz', 'if, if')