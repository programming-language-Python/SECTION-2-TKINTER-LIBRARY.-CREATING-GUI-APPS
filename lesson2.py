from tkinter import *
# from tkinter import ttk

root = Tk()
root.geometry('600x400+1000+300')


def clicked():
    print('Clicked')


# btn = Button(root, text='Кнопка', command=clicked, font='Arial 20 italic', width=10)
# btn = Button(root, text='Кнопка', command=clicked, font=('Comic Sans MS', 20, 'italic'), width=10)
# justify=LEFT or justify='left'
btn = Button(root, text='Кнопка 1\n22', justify=LEFT)
# btn.configure(width=20, height=5)
# btn['font'] = 'Arial 15'

btn.pack()

# # оформление кнопки под ОС
# btn2 = ttk.Button(root, text='Кнопка')
# btn2.pack()

# обработчик событий окна
root.mainloop()
