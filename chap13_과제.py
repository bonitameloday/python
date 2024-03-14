
from tkinter import *

def calculate():
    try:
        num1 = float(input_btn1.get())
        num2 = float(input_btn2.get())
        operator = operator_var.get()

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        else:
            result = "Invalid operator"

        result_lb.config(text=f"{result}")

    except ValueError:
        result_lb.config(text="숫자를 입력하세요.")
    except ZeroDivisionError:
        result_lb.config(text="0으로 나눌 수 없습니다.")

def set_operator(value):
    operator_var.set(value)
    calculate() 

def clear_entry():
    input_btn1.delete(0, END)
    input_btn2.delete(0, END)
    result_lb.config(text = '')


win = Tk()
win.geometry('400x150')
win.title("사칙연산 계산기")

title_lb1 = Label(win, text = '첫 번째 값')
title_lb1.grid(row = 0, column = 0, sticky = E)

input_btn1 = Entry(win)
input_btn1.grid(row = 0, column=1)

title_lb2 = Label(win, text = '두 번째 값')
title_lb2.grid(row = 1, column = 0, sticky = E)

input_btn2 = Entry(win)
input_btn2.grid(row = 1, column = 1)

title_lb2 = Label(win, text = '결과')
title_lb2.grid(row = 2, column = 0, sticky = W)

result_lb = Label(win)
result_lb.grid(row = 2, column = 1, columnspan = 2, sticky = W)

operator_var = StringVar()

add_btn = Button(win, text=" + ", command=lambda: set_operator('+'), width = 3, height = 1)
add_btn.grid(row = 3, column = 0, padx = 3, pady = 3)

sub_btn = Button(win, text=" - ", command=lambda: set_operator('-'),width = 3, height = 1)
sub_btn.grid(row = 3, column = 1, padx = 3, pady = 3)

mtp_btn = Button(win, text=" * ", command=lambda: set_operator('*'), width = 3, height = 1)
mtp_btn.grid(row = 3, column = 2, padx = 3, pady = 3)

div_btn = Button(win, text=" / ", command=lambda: set_operator('/'), width = 3, height = 1)
div_btn.grid(row = 3, column = 3, padx = 3, pady = 3)

clear_btn = Button(win, text=" AC ", command=clear_entry, width = 5, height = 2)
clear_btn.grid(row = 3, column = 4, padx = 3, pady = 3)

win.mainloop()
