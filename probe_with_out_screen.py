from pickle import GLOBAL
from stringprep import in_table_c5

import winsound

freg = 800
dur = 900


list_otkaz = [300456937581000, 300457056992000]
list_not_find = []
total_scans = 0
sum_from_today = int(555555555555555)
list_ostalos_naiti = int(444444444444444)


list_zakaz_control = [900458264164000,
700457917429000,
900458265258000,
200679640102000,
600457321294000,
600457238350000,
700457901152000,
800457559470000,
300454461735000,
800456545526000]

list_zakaz = [900458264164000,
700457917429000,
900458265258000,
200679640102000,
600457321294000,
600457238350000,
700457901152000,
800457559470000,
300454461735000,
800456545526000]


def pic(sh_cod):
    global total_scans
    # print(list_not_find)

    if sh_cod == sum_from_today:
        print(f'Отсканировано "Сегодняшних" заказов: {total_scans}, осталось отсканировать {len(list_zakaz)}')

    elif sh_cod in list_not_find:           #  if int(sh_cod[1:]) in list_not_find:
        print('Этот заказ уже БЫЛ Отсканирован сегодня')
        winsound.Beep(freg, dur + 100)

    elif sh_cod in list_otkaz:                        # if int(sh_cod[1:]) in list_otkaz:
        print('OTKAZ')
        # print(list_zakaz, 'list_zakaz - 2')
        winsound.Beep(freg, dur + 500)


    elif sh_cod not in list_zakaz:                      #  if int(sh_cod[1:]) not in list_zakaz:
        print(sh_cod, ' - Этого номера НЕТ в сегодняшних заказах')

        list_not_find.append(sh_cod)                  # list_not_find.append(int(sh_cod[1:]))
        # print(list_not_find, 3)
        winsound.Beep(freg, dur + 200)

    if sh_cod not in list_zakaz and sh_cod in list_zakaz_control:
        print('Этот номер уже БЫЛ Отсканирован сегодня')
        winsound.Beep(freg, dur + 800)

    if sh_cod == list_ostalos_naiti:
        print(list_zakaz)

    elif sh_cod in list_zakaz:

            list_zakaz.remove(sh_cod)          #   list_zakaz.remove(int(sh_cod[1:]))
            total_scans += 1
            winsound.Beep(freg, dur - 710)
            print(f'Осталось отсканировать {len(list_zakaz)}, from else')

    else:
        pass


while True:
    pic(int(input()))

# print(list_zakaz)
# a = 900456665078000
# b = 500455940710000
# c = 300454461735000
# d = 500455940710000
# f = 900456528361000



# pic(a)
# print(900456665078000, ' есть  в списке заказов')
# # print(list_not_find, 'sh_cod not find in today orders')
# # print(list_zakaz)
# pic(b)
# print(500455940710000, "есть в списке ОТКАЗОВ")
# pic(c)
# print(300454461735000, "НЕБЫЛО в списке заказов")
# pic(d)
# print(500455940710000, ' есть  в списке заказов')
# pic(f)
# print(900456528361000, ' есть  в списке заказов')
# pic(a)
# print(900456665078000, "был в списке заказо, но введен ПОВТОРНО")
# pic(c)
# print(300454461735000, "небыло в списке заказов и введен ПОВТОРНО")

# print(8)
# pic(input())
# print(9)
# pic(input())
# print(10)
