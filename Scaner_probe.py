
def add():
    num1 = float(number1_entry.get()) # Что бы получить информацию мы создадим переменную num1
                           # и воспользуемся методом .get(), а для того что бы получать целые числа обернем это в int()
    num2 = float(number2_entry.get())  # так мы вытащили информацию с двух полей
    res = num1 + num2      # создали переменную которая сохраняет сумму этих двух значений
    answer_entry.delete(0, 'end')   # очищаем поле answer_entry, что бы не наслаивались ответы друг за другом,
    # указываем с какого индекса начнем удалять и до какого, в нашем случаи воспользуемся значением 'end',
    # что бы захвать последнее поле даже если число очень большое.
    answer_entry.insert(1, res) # с помощью метода .insert() где нужно 1 -указать индекс, куда мы будем вставлять
                                               # это значение а потом Что(res - в нашем случаи) мы будем вставлять

# Для следующих (как можно было сделать и для этой функции (перед ней)), что бы не повторять одно и тоже делаем функцию,
# которая будет выдавать нам значения num1 b num2

def get_values(): # создаем возвращающию функцию, которая получает значения после ввода в поля number1_entry и number2_entry
    num1 = float(number1_entry.get())
    num2 = float(number2_entry.get())
    return  num1, num2


def insert_values(values): # создаем принимающию функцию, которая будет принимать значение (res) и подставлять его в значение (values)
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, values)
                      # ПОЧЕМУ ТУТ 0 в index, а выше там 1???
def sub():  # Создаем функцию вычитания
    num1, num2 = get_values() # получает значения от фукции get_values()
    res = num1 - num2         # из num1 вычетает num2
    insert_values(res)      # функцией insert_values() - очищает поле вывода и выводит результат


def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)


def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)

window = tk.Tk()                # Создали окно с помощью класса 'Tk()', назвали его 'window'
window.title('Калькулятор')      # наверху будем видеть название Калькулятор создали методом .title()
window.geometry('350x350')       # командой .geometry() сделали размер нашего окна 350 х 350
window.resizable(False, False)  # командой .resizable(и значениями False и False)
                                                                   # запретили изменять размер(растягивать) нашего окна
button_add = tk.Button(window, text="+", width=2, height=2, command=add) # создаем первый элемент - Виджет,
# создав переменную (button_add) в котором он будет храниться c помощью команды из библиотеки tk (tk.Button)
# указываем чему эта кнопка будет принадлежать (нашему главному окошку (window)) и с помощью длбавления параметра
# (,  text = "+:) что будет на ней написано (надпись), а с помощью параметров width и height можем указать ширину
# и высоту кнопки, с помощью параметра (command) запускаем функцию (add) которая считает сумму двух введеных чисел.
button_add.place(x=100, y=200)          # что бы наша кнопка появилась, с помощью метода .place указываем Где она будет
# Есть 3 способа размещения элементов на экране  .place , .pack и .grete - изучить самомтоятельно
button_sub = tk.Button(window, text="-", width=2, height=2, command=sub)
button_sub.place(x=150, y=200)
button_mul = tk.Button(window, text="*", width=2, height=2, command=mul)
button_mul.place(x=200, y=200)
button_div = tk.Button(window, text="/", width=2, height=2, command=div)
button_div.place(x=250, y=200)
number1_entry = tk.Entry(window, width=28) # делаем поле для ввода цифр с помощью команды .Entry() из библиотеки (tk)
# которое будет принадлежать нашему окну window и добавляем ширину (width=28)
number1_entry.place(x=100, y=75)
number2_entry = tk.Entry(window, width=28)
number2_entry.place(x=100, y=150)
answer_entry = tk.Entry(window, width=28)
answer_entry.place(x=100, y=300)
number1 = tk.Label(window, text='Введите первое число: ')  # С помощью команды tk.Label создаем текстовую надпись
number1.place(x=100, y=50)                                   # и рамещаем ее там где нам нужно при помощи команды .place
number2 = tk.Label(window, text='Введите второе число: ')
number2.place(x=100, y=125)
answer = tk.Label(window, text='Ответ: ')
answer.place(x=100, y=275)

window.mainloop()    # .mainloop() - команда запускает цикл обновления событий, обновляет информацию и происходящем
         # на экране, весь код который будем писать будет писаться между строк    window = tk.Tk()  и  window.mainloop()

# Для того что бы программу могли запускаить на лубом компьютере (даже без установленного Пайтона)
# В терминале набираем pip install auto-py-to-exe, после установки набираем  auto-py-to-exe и моздаем наше приложение
# pip install auto-py-to-exe
#  auto-py-to-exe





# запретили изменять размер(растягивать) нашего окна