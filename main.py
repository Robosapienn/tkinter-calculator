from tkinter import *
# Hary/ Robosapien

# initial tkinter setup
root = Tk()
root.title("Calculator")
root.configure(background="#142f44")
e = Entry(root, width=25, font=('Arial', 18), bg="#a2bbcf", fg="#000000", borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=20, pady=20)
# global variables used in the add, subtract, divide and multiply functions
global f_number
global math


# give functionality to the buttons
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    number1 = e.get()
    global f_number
    global math
    math = "+"
    f_number = float(number1)
    e.delete(0, END)


def button_subtract():
    number1 = e.get()
    global f_number
    global math
    math = "-"
    f_number = float(number1)
    e.delete(0, END)


def button_multiply():
    number1 = e.get()
    global f_number
    global math
    math = "*"
    f_number = float(number1)
    e.delete(0, END)


def button_divide():
    number1 = e.get()
    global f_number
    global math
    math = "/"
    f_number = float(number1)
    e.delete(0, END)


def button_equal():
    number2 = e.get()
    e.delete(0, END)
    if math == '+':
        e.insert(0, str(f_number + float(number2)))
    elif math == '-':
        e.insert(0, str(f_number - float(number2)))
    elif math == '*':
        e.insert(0, str(f_number * float(number2)))
    elif math == '/':
        e.insert(0, str(f_number / float(number2)))


# created buttons
button_0 = Button(root, text="0", bg="#205b7a", fg="white", padx=40, pady=20, command=lambda: button_click(0))
button_1 = Button(root, text="1", bg="#205b7a", fg="white", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", bg="#205b7a", fg="white", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", bg="#205b7a", fg="white", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", bg="#205b7a", fg="white", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", bg="#205b7a", fg="white", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", bg="#205b7a", fg="white", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", bg="#205b7a", fg="white", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", bg="#205b7a", fg="white", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", bg="#205b7a", fg="white", padx=40, pady=20, command=lambda: button_click(9))

button_add = Button(root, text="+", bg="#205b7a", fg="white", padx=40, pady=20, command=button_add)
button_subtract = Button(root, text="-", bg="#205b7a", fg="white", padx=40, pady=20, command=button_subtract)
button_multiply = Button(root, text="*", bg="#205b7a", fg="white", padx=40, pady=20, command=button_multiply)
button_divide = Button(root, text="/", bg="#205b7a", fg="white", padx=40, pady=20, command=button_divide)
button_equal = Button(root, text="=", bg="#205b7a", fg="white", padx=40, pady=20, command=button_equal)
button_clear = Button(root, text="C", bg="#205b7a", fg="white", padx=40, pady=20, command=button_clear)

# positioned buttons
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=1)

button_multiply.grid(row=1, column=3)
button_divide.grid(row=2, column=3)
button_add.grid(row=3, column=3)
button_subtract.grid(row=4, column=3)
button_clear.grid(row=4, column=2)
button_equal.grid(row=4, column=0)


root.mainloop()
