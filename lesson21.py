from tkinter import *

root = Tk()
root.geometry("400x300+1000+300")


def open_win():
    win = Toplevel()
    win.geometry('200x100+1200+450')
    # убирает края (скрыть, открыть на весь экран, закрыть)
    win.overrideredirect(1)
    # устанавливает фокус на окно, даже при наличии открытых других окон
    win.grab_set()
    l = Label(win, text='Hello from TopLevel', bg='#000', fg='#fff').pack(expand=1, fill=BOTH)
    win.after(3000, lambda: win.destroy())


Button(root, text="Open", command=open_win, padx=40, pady=5).place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
