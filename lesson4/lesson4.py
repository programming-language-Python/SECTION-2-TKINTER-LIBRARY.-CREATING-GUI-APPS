from tkinter import *

root = Tk()
root.geometry('600x400+1000+300')

# # anchor=W or anchor='w'
# l = Label(root, text='Текст в сроке1\nСтрока 2\nСтрока 3\nСтрока 4\nСтрока 5', bg='red', fg='#fff',
#           font=('Comic Sans MS', 10, 'bold'), justify=RIGHT, width=50, height=10, anchor=SE)
# l.pack()

img = PhotoImage(file='python-logo.png')
l_logo = Label(root, image=img)
l_logo.pack()

# обработчик событий окна
root.mainloop()
