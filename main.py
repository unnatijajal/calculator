from tkinter import *

global op, no2, no1

root = Tk()

root.title("Simple Calculator")

txt = Entry(root, width=30, borderwidth=3)
txt.grid(row=0, column=0, columnspan=4)


def button_add(num):
    n = txt.get()
    txt.delete(0, END)
    txt.insert(0, str(n) + str(num))


button1 = Button(root, text="1", padx=20, pady=15, command=lambda: button_add(1)).grid(row=1, column=0)
button2 = Button(root, text="2", padx=20, pady=15, command=lambda: button_add(2)).grid(row=1, column=1)
button3 = Button(root, text="3", padx=20, pady=15, command=lambda: button_add(3)).grid(row=1, column=2)

button4 = Button(root, text="4", padx=20, pady=15, command=lambda: button_add(4)).grid(row=2, column=0)
button5 = Button(root, text="5", padx=20, pady=15, command=lambda: button_add(5)).grid(row=2, column=1)
button6 = Button(root, text="6", padx=20, pady=15, command=lambda: button_add(6)).grid(row=2, column=2)

button7 = Button(root, text="7", padx=20, pady=15, command=lambda: button_add(7)).grid(row=3, column=0)
button8 = Button(root, text="8", padx=20, pady=15, command=lambda: button_add(8)).grid(row=3, column=1)
button9 = Button(root, text="9", padx=20, pady=15, command=lambda: button_add(9)).grid(row=3, column=2)
period = Button(root, text=".", padx=21, pady=15).grid(row=4, column=1)
zero = Button(root, text="0", padx=20, pady=15, command=lambda: button_add(0)).grid(row=4, column=0)


def clr():
    txt.delete(0, END)


clear = Button(root, text="C", command=clr, padx=102, pady=15).grid(row=5, column=0, columnspan=4)


def addition():
    global no1, op
    no1 = txt.get()
    txt.delete(0, END)
    op = "+"


def sub():
    global no1, op
    no1 = txt.get()
    txt.delete(0, END)
    op = "-"


def multiply():
    global no1, op
    no1 = txt.get()
    txt.delete(0, END)
    op = "*"


def division():
    global no1, op
    no1 = txt.get()
    txt.delete(0, END)
    op = "/"


def equal():
    global no2
    no2 = txt.get()
    if op == "+":
        txt.delete(0, END)
        txt.insert(0, int(no1) + int(no2))
    elif op == "-":
        txt.delete(0, END)
        txt.insert(0, (int(no1) - int(no2)))
    elif op == "*":
        txt.delete(0, END)
        txt.insert(0, (int(no1) * int(no2)))
    elif op == "/":
        txt.delete(0, END)
        txt.insert(0, (int(no1) / int(no2)))


add = Button(root, text="+", command=addition, padx=19, pady=15).grid(row=1, column=3)
minus = Button(root, text="-", command=sub, padx=20, pady=15).grid(row=2, column=3)
div = Button(root, text="/", command=division, padx=20, pady=15).grid(row=4, column=3)
product = Button(root, text="*", command=multiply, padx=20, pady=15).grid(row=3, column=3)

answer = Button(root, text="=", command=equal, padx=19, pady=15).grid(row=4, column=2)

root.mainloop()
