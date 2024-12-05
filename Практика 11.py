from tkinter import *
from tkinter import ttk, messagebox
from tkinter.ttk import Combobox, Radiobutton
from tkinter import filedialog

window = Tk()
window.geometry('480x480')
all_tab = ttk.Notebook(window)
all_tab.pack(expand=True, fill='both')

tab1 = ttk.Frame(all_tab)
all_tab.add(tab1, text='1 вкладка')

tab2 = ttk.Frame(all_tab)
all_tab.add(tab2, text='2 вкладка')

tab3 = ttk.Frame(all_tab)
all_tab.add(tab3, text='3 вкладка')


#1
c1 = Entry(tab1)
c2 = Entry(tab1)
res = Label(tab1, text='')
sign = Combobox(tab1)
sign['values'] = ('*', '/', '+', '-')
c1.grid(column=0, row=1)
c2.grid(column=2, row=1)
sign.grid(column=1, row=1)
res.grid(column=4, row=1)

def count():
    global res
    if sign.get() == '*':
        n = int(c1.get()) * int(c2.get())
        res.configure(text=f'= {n}')
    elif sign.get() == '+':
        n = int(c1.get()) + int(c2.get())
        res.configure(text=f'= {n}')
    elif sign.get() == '-':
        n = int(c1.get()) - int(c2.get())
        res.configure(text=f'= {n}')
    elif sign.get() == '/':
            n = int(c1.get()) / int(c2.get())
            res.configure(text=f'= {n}')


but_to_count = Button(tab1, text='total', command=count, font=5)
but_to_count.grid(column=1, row=2)



#2

def chose():
    messagebox.showinfo('', f'Вы выбрали {check.get()} вариант')


check = StringVar()
check1 = Radiobutton(tab2, text='1', value='первый', variable=check, command=chose)
check2 = Radiobutton(tab2, text='2', value='второй', variable=check, command=chose)
check3 = Radiobutton(tab2, text='3', value='третий', variable=check, command=chose)
check1.place(x=30, y=50)
check2.place(x=30, y=80)
check3.place(x=30, y=110)

#3

def from_file():
    text_in = open(filedialog.askopenfilename()).read()
    text.delete('1.0', END)
    text.insert('1.0', text_in)



btn1 = Button(tab3, text='text', font=30, command=from_file)
btn1.grid(column=2, row=0)
text = Text(tab3, width=50, height=25,  padx=30, pady=40, wrap=WORD)
text.grid(column=2, row=1)

window.mainloop()
