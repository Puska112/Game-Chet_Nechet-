from tkinter import *
from random import *
from tkinter import messagebox


def result(chet_count, nechet_count):
    for i in range(5):
        if btn[i][i]['text'] == '1':
            nechet_count += 1
        elif btn[i][i]['text'] == 'O':
            chet_count += 1
    stats_chet.append(chet_count)
    stats_nechet.append(nechet_count)
    print(f'количество нечетных {nechet_count}, количество четных {chet_count}')
    if chet_count > nechet_count:
        messagebox.showinfo('Победитель', 'Четный победил')
    elif chet_count < nechet_count:
        messagebox.showinfo('Победитель', 'Нечетный победил')
    elif chet_count == nechet_count:
        messagebox.showinfo('Победитель', 'Ничья')
    file(chet_count, nechet_count)
    new_game()


def file(chet_count, nechet_count):
    with open('result.txt', 'a') as file:
        file.writelines('Чет ' + str(chet_count))                        #запись данных в файла
        file.writelines(" - ")
        file.writelines('Нечет ' + str(nechet_count) + '\n')


def new_game():
    global ROW, COL
    for i in range(5):
        for j in range(5):
            btn[i][j]['text'] = ' '                     #новая игра
            btn[i][j]['background'] = 'lavender'
    global chet_count, nechet_count, count
    chet_count = 0
    nechet_count = 0
    count = 0


def computer_move(nechet_count):
    global chet_count
    while True:
        row = randint(0, ROW-1)
        col = randint(0, COL-1)
        if nechet_count == 13:
            break
        else:
            if btn[row][col]['text'] == ' ':
                btn[row][col]['text'] = 'O'                     # ход четного компа
                btn[row][col]['background'] = 'royalblue'
                chet_count += 1
                break


def click(row, col):
    global nechet_count, chet_count
    if btn[row][col]['text'] == ' ':
        btn[row][col]['text'] = '1'                               #ход нечетного
        btn[row][col]['background'] = 'seagreen'
        nechet_count += 1
        computer_move(nechet_count)
        print(f'количество нечетных {nechet_count}, количество четных {chet_count}')


def creat_result_win():             #окно статистики
    win_result = Toplevel(win)
    win_result.geometry('225x230')
    listbox = Listbox(win_result)
    listbox.grid(row=1, column=0, padx=45)
    label=Label(win_result, text = "Статистика", font = 'Times 15').grid(row=0, column=0, padx=45)
    with open('result.txt', 'r') as file:
        lst = file.readlines()
    for item in lst:                                         #вывод данных из файла
        listbox.insert(END, item)
    button1 = Button(win_result, text='Очистить результаты', width=17, background='lavender', command=lambda :clear(listbox)).grid(pady=5)           #кнопка очистки


def clear(listbox):
    with open('result.txt', 'w') as file:        # очистка статистика
        file.writelines('')
    listbox.delete(0, END)


win = Tk()
win.title('Chet - NeChet')

ROW = 5
COL = 5
btn = []               # матрица кнопок
stats_chet = []
stats_nechet = []
chet_count = 0
nechet_count = 0


for i in range(ROW):
    spic = []
    for j in range(COL):
        button = Button(win, text=' ', width=4, height=2, font=('Verdana', 20, 'bold'), background='lavender')   # создали кнопку
        button.grid(row=i, column=j, sticky='nsew')
        button.config(command=lambda row=i, col=j: click(row, col))  # функционал кнопки
        spic.append(button)
    btn.append(spic)


new_button = Button(win, text='Победитель', command=lambda: result(chet_count, nechet_count))           # кнопка результата
new_button.grid(row=ROW, column=0, columnspan=COL, sticky='nsew')


menubar = Menu(win)                       #основа выпадающего меню
win.config(menu=menubar)


settings_menu = Menu(menubar, tearoff=0)
settings_menu.add_command(label='Новая играть', command=new_game)
settings_menu.add_command(label='Статистика', command=creat_result_win)                      #выпадающее меню
settings_menu.add_command(label='Выход', command=win.destroy)
menubar.add_cascade(label='Файл', menu=settings_menu)


win.mainloop()