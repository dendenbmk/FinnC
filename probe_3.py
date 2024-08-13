list_otkaz = [1, 2, 3, 4]
list_zakaz = [5, 6, 7, 8, 9]
list_zakaz_new = list_zakaz
list_not_find = []
list_otpicano = []
otskanirovano_raz_today = 1

def pic(sh_c):
    global otskanirovano_raz_today

    if sh_c in list_otpicano and sh_c in list_zakaz:
        print('Было в заказах, НО УЖЕ БЫЛО ОТСКАНИРОВАНО СЕГОДНЯ')

    if sh_c in list_otpicano:
        otskanirovano_raz_today += 1
        print('Уже было отсканировано сегодня', otskanirovano_raz_today, 'раза')
        list_otpicano.append(sh_c)

    if sh_c in list_otkaz:
        print('ОТКАЗ', sh_c)
        list_otpicano.append(sh_c)

    if sh_c in list_zakaz:
        print('Отсканили из заказа, удаляем из списка заказано_NEW, добавляем в список отпикано')
        list_otpicano.append(sh_c)
        list_zakaz_new.remove(sh_c)

    if sh_c in list_otpicano and sh_c in list_not_find:
        print(sh_c, 'Небыло сегодня и УЖЕ БЫЛО отпикано сегодня')
        list_otpicano.append(sh_c)

    elif sh_c not in list_zakaz:
        print(sh_c, 'НЕБЫЛО в заказах сегодня')
        list_otpicano.append(sh_c)
        list_not_find.append(sh_c)


pic(5)
print(list_zakaz, "лист заказ")
print(list_zakaz_new, "лист заказ_New")
print(list_not_find, "лист не найденого в сегодня")
print(list_otpicano, "лист отпикано")
pic(6)
pic(15)
print(list_zakaz, "лист заказ")
print(list_zakaz_new, "лист заказ_New")
print(list_not_find, "лист не найденого в сегодня")
print(list_otpicano, "лист отпикано")
pic(15)
print(list_zakaz, "лист заказ")
print(list_zakaz_new, "лист заказ_New")
print(list_not_find, "лист не найденого в сегодня")
print(list_otpicano, "лист отпикано")