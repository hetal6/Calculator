from math import sqrt
from tkinter import*

entered_value= ""
def button_onclick(value, input_text):
    global entered_value
    entered_value= entered_value + str(value)
    input_text.set(entered_value)
def button_clear(input_text):
    global entered_value
    entered_value= ""
    input_text.set("")
def evaluate(input_text):
    global entered_value
    try:
        output=str(eval(entered_value))
        input_text.set(output)
        entered_value= ""
    except:
        entered_value= ""
def backspace(input_text):
    global entered_value
    entered_value= str(entered_value)[0:-1]
    input_text.set(entered_value)
def square_root(input_text):
    global entered_value
    number=str(eval(entered_value))
    new_number=sqrt(number)
    input_text.set(new_number)
def main():
    #Creating basic window
    window=Tk()
    window.title("Calculator")
    window.geometry("433x389")
    input_text=StringVar()
    window.resizable(0,0)
    window.config(background="black")
    input_text.set("")
    #================================Row-0================================
    text_display = Entry(window, width=20, textvariable=input_text, borderwidth=0, highlightthickness = 0, justify="right", font=('Times', 28, 'bold'), fg="white", bg="black")
    text_display.grid(row=0,column=0,columnspan=4,padx=(1,30),pady=1)
    text_display.insert(0,"0")
    # ================================Buttons-setup================================
    but_1 = Button(window, text="1", padx= 41, pady=20, command=lambda: button_onclick(1, input_text), font="Times 11")
    but_2 = Button(window, text="2", padx= 42, pady=20, command=lambda: button_onclick(2, input_text), font="Times 11")
    but_3 = Button(window, text="3", padx= 45, pady=20, command=lambda: button_onclick(3, input_text), font="Times 11")
    but_4 = Button(window, text="4", padx= 41, pady=20, command=lambda: button_onclick(4, input_text), font="Times 11")
    but_5 = Button(window, text="5", padx= 42, pady=20, command=lambda: button_onclick(5, input_text), font="Times 11")
    but_6 = Button(window, text="6", padx= 45, pady=20, command=lambda: button_onclick(6, input_text), font="Times 11")
    but_7 = Button(window, text="7", padx= 41, pady=20, command=lambda: button_onclick(7, input_text), font="Times 11")
    but_8 = Button(window, text="8", padx= 42, pady=20, command=lambda: button_onclick(8, input_text), font="Times 11")
    but_9 = Button(window, text="9", padx= 45, pady=20, command=lambda: button_onclick(9, input_text), font="Times 11")
    but_point = Button(window, text=".", padx= 42, pady=20, command =lambda: button_onclick(".", input_text), font="Times 11")
    but_0 = Button(window, text="0", padx= 42, pady=20, command=lambda: button_onclick(0, input_text), font="Times 11")
    but_equal = Button(window, text="=", padx= 45, pady=18, command=lambda: evaluate(input_text), font="Impact")
    but_add = Button(window, text="+", padx= 66, pady=18, fg="white", bg="orange", command=lambda: button_onclick("+", input_text), font="Impact")
    but_clear = Button(window, text="C", padx= 40, pady=20, fg="white", bg="#B0ACAB", command=lambda: button_clear(input_text), font="Times 11")
    but_per = Button(window, text="%", padx=40, pady=20, fg="white", bg="#B0ACAB", command=lambda: button_onclick("%", input_text), font="Times 11")
    but_sqrt = Button(window, text="√", padx= 40, pady=15, fg="white", bg="#B0ACAB", command=lambda: square_root(input_text), font="Times 16")
    but_del = Button(window, text="⌫", padx= 61, pady=18, fg="white", bg="#B0ACAB", command=lambda: backspace(input_text), font="Impact")
    but_sub = Button(window, text="-", padx= 68, pady=18, fg="white", bg="orange", command=lambda: button_onclick("-", input_text), font="Impact")
    but_mul = Button(window, text="x", padx= 68, pady=18, fg="white", bg="orange", command=lambda: button_onclick("*", input_text), font="Impact")
    but_div = Button(window, text="÷", padx= 66, pady=18, fg="white", bg="orange", command=lambda: button_onclick("/", input_text), font="Impact")
    #================================Row-5================================
    but_point.grid(row=5, column=0)
    but_0.grid(row=5, column=1)
    but_equal.grid(row=5, column=2)
    but_add.grid(row=5, column=3)
    #================================Row-4================================
    but_1.grid(row=4, column=0)
    but_2.grid(row=4, column=1)
    but_3.grid(row=4, column=2)
    but_sub.grid(row=4, column=3)
    #================================Row-3================================
    but_4.grid(row=3, column=0)
    but_5.grid(row=3, column=1)
    but_6.grid(row=3, column=2)
    but_mul.grid(row=3, column=3)
    #================================Row-2================================
    but_7.grid(row=2, column=0)
    but_8.grid(row=2, column=1)
    but_9.grid(row=2, column=2)
    but_div.grid(row=2, column=3)
    #================================Row-1================================
    but_clear.grid(row=1, column=0)
    but_per.grid(row=1, column=1)
    but_sqrt.grid(row=1, column=2)
    but_del.grid(row=1, column=3)

    window.mainloop()

if __name__ == '__main__':
      main()