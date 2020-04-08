from tkinter import *
import algs


def but_result1():

    global l1

    try:
        _a = ent_a1.get()
        _b = ent_b1.get()
        _c = ent_c1.get()
        if _a == '' or _b == '' or _c == '':
            _res = 'Вам варто заповнити ВСІ поля!'
        else:
            _res = round(algs.alg1(int(_a), int(_b), int(_c)), 3)
    except: _res = 'Введіть будь-ласка цифри.'

    if len(str(_res)) < 15:
        _c = 4
        _r = 7
        _cs = 3
    else:
        _c = 3
        _r = 8
        _cs = 7

    try:
        l1.destroy()
    finally:
        l1 = Label(root, text=_res, font=main_font, bg=bg_color1)
        l1.grid(column=_c, row=_r, columnspan=_cs, sticky=W)


def but_result2():


    global l2


    try:
        _a = int(ent_a2.get())
        _b = int(ent_b2.get())
        _c = int(ent_c2.get())
        _d = int(ent_d2.get())

        if _a == '' or _b == '' or _c == '' or _d == '':
            _res = 'Вам варто заповнити ВСІ поля!'
        else:
            _res = round(algs.alg2(int(_a), int(_b), int(_c), int(_d)), 3)
    except: _res = 'Введіть будь-ласка цифри'


    if len(str(_res)) < 15: # no errors
        _c = 4
        _r = 7
        _cs = 3
    else:
        _c = 3
        _r = 8
        _cs = 7

    try:
        l2.destroy()
    finally:
        l2 = Label(root, text=_res, font=main_font, bg=bg_color2)
        l2.grid(column=_c, row=_r, columnspan=_cs, sticky=W)


def but_result3():


    global l3


    try:
        _a = ent_a3.get().split(",")
        _b = ent_b3.get().split(",")
        _c = ent_b3.get().split(",")
        _d = ent_b3.get().split(",")

        _a = [int(i) for i in _a]
        _b = [int(i) for i in _b]
        _c = [int(i) for i in _c]
        _d = [int(i) for i in _d]

        if _a == '' or _b == ''  or _c == '' or _d == '':
            _res = 'Вам варто заповнити ВСІ поля!'
        else:
            _res = round(algs.alg3(_a,_b,_c,_d), 3)
    except: _res = 'Введіть будь-ласка цифри.'


    if len(str(_res)) < 15: # no errors
        _c = 4
        _r = 7
        _cs = 3
    else:
        _c = 3
        _r = 8
        _cs = 7

    try:
        l3.destroy()
    finally:
        l3 = Label(root, text=_res, font=main_font, bg=bg_color3)
        l3.grid(column=_c, row=_r, columnspan=_cs, sticky=W)



def but1_bind():

    global ent_a1, ent_b1, ent_c1
    root.geometry('1150x570')

    Label(root, text='', font='Calibri 14', width=80, height=25, bg=bg_color1)\
        .grid(row=0, column=1, rowspan=12, columnspan=10)

    Label(root, text='a', justify=RIGHT, font=main_font, bg=bg_color1).grid(column=2, row=1, sticky=E)
    Label(root, text='b', justify=RIGHT, font=main_font, bg=bg_color1).grid(column=2, row=3, sticky=E)
    Label(root, text='c', justify=RIGHT, font=main_font, bg=bg_color1).grid(column=2, row=5, sticky=E)

    ent_a1 = Entry(root, font='Calibri 14', width=10, bd=0)
    ent_b1 = Entry(root, font='Calibri 14', width=10, bd=0)
    ent_c1 = Entry(root, font='Calibri 14', width=10, bd=0)

    ent_a1.grid(column=3, row=1, columnspan=2, sticky=W, padx=5)
    ent_b1.grid(column=3, row=3, columnspan=2, sticky=W, padx=5)
    ent_c1.grid(column=3, row=5, columnspan=2, sticky=W, padx=5)

    def but_from_file1():
        with open(r"C:\Users\ASUS\PycharmProjects\AMO\Lab_1\venv\Include\input_file\input1.txt", "r") as file:
            text = file.read()
            text_list = text.split(",")
            a = int(text_list[0])
            b = int(text_list[1])
            c = int(text_list[2])
            ent_a1.insert(0,a)
            ent_b1.insert(0,b)
            ent_c1.insert(0,c)

    Button(root, text='Result', font=main_font, bg='#fcdf03', command=but_result1).grid(column=3, row=7)
    Button(root, text='From File', font=main_font, bg='#fcdf03', command=but_from_file1).grid(column=6, row=7)


def but2_bind():

    global ent_a2, ent_b2, ent_c2, ent_d2
    root.geometry('1150x570')

    Label(root, text='', font='Calibri 14', width=80, height=25, bg=bg_color2)\
        .grid(row=0, column=1, rowspan=12, columnspan=10)

    Label(root, text='a', justify=RIGHT, font=main_font, bg=bg_color2).grid(column=2, row=1, sticky=E)
    Label(root, text='b', justify=RIGHT, font=main_font, bg=bg_color2).grid(column=2, row=3, sticky=E)
    Label(root, text='c', justify=RIGHT, font=main_font, bg=bg_color2).grid(column=6, row=1, sticky=E)
    Label(root, text='d', justify=RIGHT, font=main_font, bg=bg_color2).grid(column=6, row=3, sticky=E)

    ent_a2 = Entry(root, font='Calibri 14', width=10, bd=0)
    ent_b2 = Entry(root, font='Calibri 14', width=10, bd=0)
    ent_c2 = Entry(root, font='Calibri 14', width=10, bd=0)
    ent_d2 = Entry(root, font='Calibri 14', width=10, bd=0)

    ent_a2.grid(column=3, row=1, columnspan=2, sticky=W, padx=5)
    ent_b2.grid(column=3, row=3, columnspan=2, sticky=W, padx=5)
    ent_c2.grid(column=7, row=1, columnspan=2, sticky=W, padx=5)
    ent_d2.grid(column=7, row=3, columnspan=2, sticky=W, padx=5)

    def but_from_file2():
        with open(r"C:\Users\ASUS\PycharmProjects\AMO\Lab_1\venv\Include\input_file\input2.txt", "r") as file:
            text = file.read()
            text_list = text.split(",")
            a = int(text_list[0])
            b = int(text_list[1])
            c = int(text_list[2])
            d = int(text_list[3])
            ent_a2.insert(0,a)
            ent_b2.insert(0,b)
            ent_c2.insert(0,c)
            ent_d2.insert(0,d)

    Button(root, text='Result', font=main_font, bg='#fcce03', command=but_result2).grid(column=3, row=7)
    Button(root, text='From File', font=main_font, bg='#fcce03', command=but_from_file2).grid(column=6, row=7)



def but3_bind():


    global ent_a3, ent_b3
    root.geometry('1150x570')

    Label(root, text='', font='Calibri 14', width=80, height=25, bg=bg_color3)\
        .grid(row=0, column=1, rowspan=12, columnspan=10)

    Label(root, text='a', justify=RIGHT, font=main_font, bg=bg_color3).grid(column=2, row=1, sticky=E)
    Label(root, text='b', justify=RIGHT, font=main_font, bg=bg_color3).grid(column=2, row=3, sticky=E)
    Label(root, text='c', justify=RIGHT, font=main_font, bg=bg_color3).grid(column=4, row=1, sticky=E)
    Label(root, text='d', justify=RIGHT, font=main_font, bg=bg_color3).grid(column=4, row=3, sticky=E)

    ent_a3 = Entry(root, font='Calibri 14', width=10, bd=0)
    ent_b3 = Entry(root, font='Calibri 14', width=10, bd=0)
    ent_c3 = Entry(root, font='Calibri 14', width=10, bd=0)
    ent_d3 = Entry(root, font='Calibri 14', width=10, bd=0)

    ent_a3.grid(column=3, row=1, columnspan=2, sticky=W, padx=5)
    ent_b3.grid(column=3, row=3, columnspan=2, sticky=W, padx=5)
    ent_c3.grid(column=6, row=1, columnspan=2, sticky=W, padx=5)
    ent_d3.grid(column=6, row=3, columnspan=2, sticky=W, padx=5)

    def but_from_file3():
        with open(r"C:\Users\ASUS\PycharmProjects\AMO\Lab_1\venv\Include\input_file\input3.txt", "r") as file:
            text = file.read()
            text_list = text.split("\n")
            print(text_list)
            for i in range(len(text_list)):
                text_list[i] = text_list[i].split(",")
            print(text_list)
            a = text_list[0]
            b = text_list[1]
            c = text_list[2]
            d = text_list[3]

            ent_a3.insert(0,",".join(a))
            ent_b3.insert(0,",".join(b))
            ent_c3.insert(0,",".join(c))
            ent_d3.insert(0,",".join(d))

            a = [int(i) for i in text_list[0]]
            b = [int(i) for i in text_list[1]]
            c = [int(i) for i in text_list[2]]
            d = [int(i) for i in text_list[3]]

    Button(root, text='Result', font=main_font, bg='orange', command=but_result3).grid(column=3, row=7)
    Button(root, text='From File', font=main_font, bg='orange', command=but_from_file3).grid(column=6, row=7)


if __name__ == '__main__':
    root = Tk()
    root.title('Main window')
    root.resizable(width=False, height=False)
    root.geometry('370x570')


    bg_color1 = '#fce803'
    bg_color2 = '#fcdf03'
    bg_color3 = '#fcce03'
    main_font = 'Verdana 14'


    photo1 = PhotoImage(file=r"C:\Users\ASUS\PycharmProjects\AMO\Lab_1\venv\Include\images\1.png")
    photo2 = PhotoImage(file=r"C:\Users\ASUS\PycharmProjects\AMO\Lab_1\venv\Include\images\2.png")
    photo3 = PhotoImage(file=r"C:\Users\ASUS\PycharmProjects\AMO\Lab_1\venv\Include\images\3.png")

    Button(root, compound=BOTTOM, image=photo1, bd=0, text='', relief=GROOVE, width=370, height=175,
           font='Arial 14 bold', bg=bg_color1, activebackground=bg_color1, command=but1_bind)\
        .grid(column=0, row=0, rowspan=4,)

    Button(root, compound=BOTTOM, image=photo2, bd=0, text='', relief=GROOVE, width=370, height=230,
           font='Arial 14 bold', bg=bg_color2, activebackground=bg_color2, command=but2_bind)\
        .grid(column=0, row=4, rowspan=4,)

    Button(root, compound=BOTTOM, image=photo3, bd=0, text='', relief=GROOVE, width=370, height=170,
           font='Arial 14 bold', bg=bg_color3, activebackground=bg_color3, command=but3_bind)\
        .grid(column=0, row=8, rowspan=4,)

    root.mainloop()
