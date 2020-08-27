from tkinter import *
import tkinter.ttk as ttk


def create_butt(v, x, y, com):
    ttk.Button(root, text=v, command=com).grid(row=x, column=y)


def click_number(n):
    if len(result.get()) < 25:
        result.set(result.get() + n)


def all_result():
    try:
        a = eval(result.get())
        if type(a) is float:
            result.set("%.2f" % a)
        else:
            result.set(a)
    except:
        result.set('Error')


def clean():
    result.set('')


def back():
    if len(result.get()) > 0:
        result.set(result.get()[:-1])


root = Tk()
root.title('Calculator')


result = StringVar()
result.set('')
ttk.Label(root, textvariable=result, width=30, anchor='e').grid(row=0, column=0, columnspan=4)


create_butt('1', 1, 0, lambda: click_number('1'))
create_butt('2', 1, 1, lambda: click_number('2'))
create_butt('3', 1, 2, lambda: click_number('3'))
create_butt('4', 1, 3, lambda: click_number('4'))
create_butt('5', 2, 0, lambda: click_number('5'))
create_butt('6', 2, 1, lambda: click_number('6'))
create_butt('7', 2, 2, lambda: click_number('7'))
create_butt('8', 2, 3, lambda: click_number('8'))
create_butt('9', 3, 0, lambda: click_number('9'))
create_butt('0', 3, 1, lambda: click_number('0'))
create_butt('.', 3, 2, lambda: click_number('.'))
create_butt('back', 3, 3, back)


create_butt('+', 4, 0, lambda: click_number('+'))
create_butt('-', 4, 1, lambda: click_number('-'))
create_butt('*', 4, 2, lambda: click_number('*'))
create_butt('/', 4, 3, lambda: click_number('/'))

create_butt('=', 5, 1, all_result)
create_butt('c', 5, 2, clean)

root.mainloop()






