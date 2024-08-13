import winsound

freg = 800
dur = 900

# skan_ = input()
# scan = int(skan_[1:])
# print(scan)
# scan = 300454461735000

list_otkaz = [500455940710000]
list_not_find = []
# print(scan, type(scan))
total_scans = 0
winsound.Beep(freg, dur)

list_zakaz = [900456665078000, 900456528361000, 500455940710000] #~300454461735000
# , 300454461735000]
print(list_zakaz, 'list_zakaz - 1')

def pic(sh_cod):
    print(list_not_find)
    if sh_cod in list_not_find:           #  if int(sh_cod[1:]) in list_not_find:
        print('This order was alredy today')

    if sh_cod in list_otkaz:                        # if int(sh_cod[1:]) in list_otkaz:
        print('OTKAZ')
        print(list_zakaz, 'list_zakaz - 2')

    if sh_cod not in list_zakaz:                      #  if int(sh_cod[1:]) not in list_zakaz:
        print(sh_cod, ' - Not in orders today')

        list_not_find.append(sh_cod)                  # list_not_find.append(int(sh_cod[1:]))
        print(list_zakaz, 3)
        winsound.Beep(freg, dur + 500)


    else:
        list_zakaz.remove(sh_cod)          #   list_zakaz.remove(int(sh_cod[1:]))
        print(list_zakaz, 4)


a = 900456665078000
b = 500455940710000
c = 300454461735000
d = 500455940710000
f = 900456528361000



pic(a)
print(900456665078000, ' есть  в списке заказов')
# print(list_not_find, 'sh_cod not find in today orders')
# print(list_zakaz)
pic(b)
print(500455940710000, "есть в списке ОТКАЗОВ")
pic(c)
print(300454461735000, "НЕБЫЛО в списке заказов")
pic(d)
print(500455940710000, ' есть  в списке заказов')
pic(f)
print(900456528361000, ' есть  в списке заказов')
pic(a)
print(900456665078000, "был в списке заказо, но введен ПОВТОРНО")
pic(c)
print(300454461735000, "небыло в списке заказов и введен ПОВТОРНО")
# pic(input())
# print(8)
# pic(input())
# print(9)
# pic(input())
# print(10)

