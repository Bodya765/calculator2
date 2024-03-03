import tkinter as tk
import math

def button_click(number):
    current = entry.get()
    entry.delete(0, 'end')
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, 'end')

def button_operation(operator):
    global f_num
    global math_operator
    first_number = entry.get()
    math_operator = operator
    f_num = float(first_number)
    entry.delete(0, 'end')

def button_sin():
    number = float(entry.get())
    result = math.sin(math.radians(number))
    entry.delete(0, 'end')
    entry.insert(0, result)

def button_equal():
    second_number = entry.get()
    entry.delete(0, 'end')
    if math_operator == "addition":
        entry.insert(0, f_num + float(second_number))
    elif math_operator == "subtraction":
        entry.insert(0, f_num - float(second_number))
    elif math_operator == "multiplication":
        entry.insert(0, f_num * float(second_number))
    elif math_operator == "division":
        entry.insert(0, f_num / float(second_number))


root = tk.Tk()
root.title("Простий калькулятор")

entry = tk.Entry(root, width=20, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('sin', 5, 0), ('Exit', 5, 1)
]

for (text, row, col) in buttons:
    if text == 'sin':
        btn = tk.Button(root, text=text, padx=20, pady=20, command=button_sin)
    elif text == 'C':
        btn = tk.Button(root, text=text, padx=20, pady=20, command=button_clear)
    elif text == 'Exit':
        btn = tk.Button(root, text=text, padx=20, pady=20, command=root.destroy)
    else:
        btn = tk.Button(root, text=text, padx=20, pady=20, command=lambda t=text: button_click(
            t) if t != '=' else button_equal() if t != 'C' else button_operation(t))

    btn.grid(row=row, column=col)

root.mainloop()
