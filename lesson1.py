import tkinter as tk

form=tk.Tk()
form.geometry('500x500+500+350')
form.minsize(400,400)
form.maxsize(550,550)
form.title('Calculator')
label=tk.Label(form,text='Calculator')
label.pack()
label2=tk.Label(form,text='github: hazal-hk',fg='red',font='Times 15 italic')
label2.pack()

entry1=tk.Entry(form, width=50)
entry1.pack()

entry2=tk.Entry(form, width=50)
entry2.pack()


def sum():
    try:
        number1=int(entry1.get())
        number2=int(entry2.get())
        result= number1 + number2
        label_result.config(text=f"Result: {result}")
    except ValueError:
        label_result.config(text=("please enter valid numbers "))
def extract():
    try:
        number1=int(entry1.get())
        number2=int(entry2.get())
        result= number1 - number2
        label_result.config(text=f"Result: {result}")
    except ValueError:
        label_result.config(text=("please enter valid numbers "))
def multiplication():
    try:
        number1=int(entry1.get())
        number2=int(entry2.get())
        result= number1 * number2
        label_result.config(text=f"Result: {result}")
    except ValueError:
        label_result.config(text=("please enter valid numbers "))
def divide():
    try:
        number1=int(entry1.get())
        number2=int(entry2.get())
        result= number1 / number2
        label_result.config(text=f"Result: {result}")
    except ValueError:
        label_result.config(text=("please enter valid numbers "))
def delete():
    entry1.delete(0,'end')
    entry2.delete(0,'end')

button=tk.Button(form,text='+', activeforeground='orange',cursor='tcross', width=6, height=3, bd=4, command=sum)
button.pack(side=tk.BOTTOM, pady=5)
button2=tk.Button(form,text='-', activeforeground='orange', cursor='tcross', width=6, height=3, bd=4,command=extract)
button2.pack(side=tk.BOTTOM, pady=5)
button3=tk.Button(form,text='x', activeforeground='orange',cursor='tcross', width=6, height=3, bd=4, command=multiplication)
button3.pack(side=tk.BOTTOM, pady=5)
button4=tk.Button(form,text='/', activeforeground='orange', cursor='tcross', width=6, height=3, bd=4, command=divide )
button4.pack(side=tk.BOTTOM, pady=5)
button5=tk.Button(form,text='delete', activeforeground='orange', cursor='tcross', width=6, height=3, bd=4, command=delete )
button5.pack(side=tk.BOTTOM, pady=5)

label_result = tk.Label(form,text="Result: ")
label_result.pack()

form.mainloop()
