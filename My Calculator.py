from logging import root
import tkinter as tk

calculation = ""


def add_to_text_input(symbol):
    global calculation
    calculation += str(symbol)
    text_input.delete(1.0, "end")
    text_input.insert(1.0, calculation)


def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        text_input.delete(1.0, "end")
        text_input.insert(1.0, result)
    except:
        clear_field()
        text_input.insert(1.0, "Error")


def clear_field():
    global calculation
    calculation = ""
    text_input.delete(1.0, "end")

root = tk.Tk()

root.title("My Calculotor")
root.geometry("330x280")
root.config(background="powder blue")

text_input = tk.Text(root, height="2", width="16", font=("Verdana", 24))
text_input.grid(columnspan=5)

btn1 = tk.Button(root, text="1", command=lambda: add_to_text_input(1), width=5, font=("Arial", 14)).grid(row=2, column=1)
btn2 = tk.Button(root, text="2", command=lambda: add_to_text_input(2), width=5, font=("Arial", 14)).grid(row=2, column=2)
btn3 = tk.Button(root, text="3", command=lambda: add_to_text_input(3), width=5, font=("Arial", 14)).grid(row=2, column=3)
btn4 = tk.Button(root, text="4", command=lambda: add_to_text_input(4), width=5, font=("Arial", 14)).grid(row=3, column=1)
btn5 = tk.Button(root, text="5", command=lambda: add_to_text_input(5), width=5, font=("Arial", 14)).grid(row=3, column=2)
btn6 = tk.Button(root, text="6", command=lambda: add_to_text_input(6), width=5, font=("Arial", 14)).grid(row=3, column=3)
btn7 = tk.Button(root, text="7", command=lambda: add_to_text_input(7), width=5, font=("Arial", 14)).grid(row=4, column=1)
btn8 = tk.Button(root, text="8", command=lambda: add_to_text_input(8), width=5, font=("Arial", 14)).grid(row=4, column=2)
btn9 = tk.Button(root, text="9", command=lambda: add_to_text_input(9), width=5, font=("Arial", 14)).grid(row=4, column=3)
btn0 = tk.Button(root, text="0", command=lambda: add_to_text_input(0), width=5, font=("Arial", 14)).grid(row=5, column=2)

btn_plus = tk.Button(root, text="+", command=lambda: add_to_text_input("+"), width=5, activeforeground="powder blue", activebackground="yellow", font=("Arial", 14)).grid(row=2, column=4)
btn_minus = tk.Button(root, text="-", command=lambda: add_to_text_input("-"), width=5, activeforeground="powder blue", activebackground="yellow", font=("Arial", 14)).grid(row=3, column=4)
btn_mul = tk.Button(root, text="*", command=lambda: add_to_text_input("*"), width=5, activeforeground="powder blue", activebackground="yellow", font=("Arial", 14)).grid(row=4, column=4)
btn_div = tk.Button(root, text="/", command=lambda: add_to_text_input("/"), width=5, activeforeground="powder blue", activebackground="yellow", font=("Arial", 14)).grid(row=5, column=4)
btn_openbra = tk.Button(root, text="(", command=lambda: add_to_text_input("("), width=5, font=("Arial", 14)).grid(row=5, column=1)
btn_closebra = tk.Button(root, text=")", command=lambda: add_to_text_input(")"), width=5, font=("Arial", 14)).grid(row=5, column=3)
btn_clear = tk.Button(root, text="C", command=clear_field, width=11, activeforeground="powder blue", activebackground="red", font=("Arial", 14)).grid(row=6, column=1, columnspan=2)
btn_equals = tk.Button(root, text="=", command=evaluate_calculation, width=11, image="", activeforeground="powder blue", activebackground="green", font=("Arial", 14)).grid(row=6, column=3, columnspan=2)

root.mainloop()