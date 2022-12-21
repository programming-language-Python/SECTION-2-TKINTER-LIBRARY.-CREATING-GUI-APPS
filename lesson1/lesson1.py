# https://www.tutorialspoint.com/python3/python_gui_programming.htm

from tkinter import *

root = Tk()
root.title('Мое первое GUI приложение')
root.iconbitmap('python.ico')
root.geometry('600x400+1000+300')
root.resizable(False, False)
# root.config(bg='#000')
# root['bg'] = 'red'

# обработчик событий окна
root.mainloop()
