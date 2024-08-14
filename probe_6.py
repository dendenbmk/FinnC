# import tkinter as tk

# window = tk.Tk()
# window.title('Сканируем штрих-кода отгрузки')
# window.geometry('1000x1000')
# window.resizable(False, False)

# button_add_list_zakaz = tk.Button(window, text='add_zakaz', width=10, height=2)
# button_add_list_zakaz.place(x=50, y=50)
# button_add_list_otkaz = tk.Button(window, text='add_otkaz', width=10, height=2)
# button_add_list_otkaz.place(x=100, y=50)

# number1_entry_list_zakaz = tr.Entry(window, width=40) 
# number1_entry_list_zakaz.place(x=70, y=50)
# number2_entry_list_otkaz = tr.Entry(window, width=40) 
# number2_entry_list_otkaz.place(x=120, y=50)

# number3_entry_list_ostalos_otgruzit = tr.Entry(window, width=40) 
# number3_entry_list_ostalos_otgruzit.place(x=700, y=50)
# number4_entry_list_otscan_today = tr.Entry(window, width=40) 
# number4_entry_list_otscan_today.place(x=750, y=50)
# number5_entry_list_otscan_otkazov = tr.Entry(window, width=40) 
# number5_entry_list_otscan_otkazov.place(x=800, y=50)





# window.mainloop()



list_otkaz = [1, 2, 3, 4]
list_otkaz_new =[]
list_zakaz = [5, 6, 7, 8, 9]
list_zakaz_new = [5, 6, 7, 8, 9]
list_not_find = []
list_otpicano = []
cod_finish = 555
# otskanirovano_raz_today = 1

def pic(sh_c):
    # global otskanirovano_raz_today
    if sh_c == cod_finish:
        # number3_entry_list_ostalos_otgruzit.insert(0, f'ЕЩЕ НУЖНО {len(list_zakaz_new)} Заказов отсканировать для отгрузки, список заказов ,{list_zakaz_n)
        # number4_entry_list_otscan_today.insert(0, f'ЕЩЕ НУЖНО {len(list_zakaz_new)} Заказов отсканировать для отгрузки, список заказов ,{list_zakaz_new}')
        print(f'ЕЩЕ НУЖНО {len(list_zakaz_new)} Заказов отсканировать для отгрузки, список заказов ,{list_zakaz_new}')
        print(len(list_zakaz) - len(list_zakaz_new), 'Заказов отсканировано для сегодняшней отгрузки')
        print(len(list_otpicano), 'Всего заказов отсканировано')
        print(len(list_not_find), 'Всего отсканировано заказов НЕ из сегодняшнего дня')
        print(len(list_otkaz_new), 'Всего отсканировано  "отазных " заказов')
        # number5_entry_list_otscan_otkazov.insert(0, f' {len(list_otkaz_new)}, Всего отсканировано  "отказных " заказов')

    
    if sh_c in list_otpicano:
        # otskanirovano_raz_today += 1
        print(sh_c, 'Уже было отсканировано сегодня') # , otskanirovano_raz_today, 'раза')
        list_otpicano.append(sh_c)

    if sh_c in list_otpicano and sh_c in list_zakaz:
        print('Было в заказах, НО УЖЕ БЫЛО ОТСКАНИРОВАНО СЕГОДНЯ')
        
    if sh_c in list_otpicano and sh_c in list_not_find:
        print(sh_c, 'Небыло сегодня и УЖЕ БЫЛО отпикано сегодня')
        # list_otpicano.append(sh_c)

    elif sh_c not in list_zakaz:
        print(sh_c, 'НЕБЫЛО в заказах сегодня')
        list_otpicano.append(sh_c)
        list_not_find.append(sh_c)    

    if sh_c in list_otkaz:
        print(sh_c, 'ОТКАЗ, нужно Убрать из доставки')
        list_otpicano.append(sh_c)
        list_otkaz_new.append(sh_c)

    if sh_c in list_zakaz:
        print( sh_c, 'Отсканили из заказа, удаляем из списка заказано_NEW, добавляем в список отпикано')
        list_otpicano.append(sh_c)
        list_zakaz_new.remove(sh_c)
        
    print(list_otpicano)
    print(list_otkaz_new)
    print()
    
while True:
    pic(int(input()))
print(list_otpicano)

# pic(5)
# print()
# pic(6)
# print()
# pic(7)
# print()
# pic(8)
# print()
# pic(4)
# print()
# pic(15)
# print()
# pic(15)
# print()
# pic(15)
# print()
# pic(16)
# print()
# pic(16)
# print()


pic(555)
pic(9)
print()
pic(555)


# pic(5)
# print(list_zakaz, "лист заказ, первая Итерация")
# print(list_zakaz_new, "лист заказ_New , первая Итерация")
# print(list_not_find, "лист не найденого в сегодн , первая Итерацияя")
# print(list_otpicano, "лист отпикано, первая Итерация")
# print('закончили первую итерацию')
# print()
# pic(6)
# print('закончили Вторую итерацию')
# print()
# pic(15)
# print(list_zakaz, "лист заказ")
# print(list_zakaz_new, "лист заказ_New")
# print(list_not_find, "лист не найденого в сегодня")
# print(list_otpicano, "лист отпикано")
# print('закончили Третью итерацию')
# print()
# pic(15)
# print(list_zakaz, "лист заказ")
# print(list_zakaz_new, "лист заказ_New")
# print(list_not_find, "лист не найденого в сегодня")
# print(list_otpicano, "лист отпикано")
# print('закончили Четвертую итерацию')
# print()
# pic(15)
# print(list_otpicano, "лист отпикано")
