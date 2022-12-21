from tkinter import *

root = Tk()

'''
Напишите программу, состоящую из семи кнопок, цвета которых соответствуют цветам радуги. При нажатии на ту или иную кнопку в текстовое поле должен вставляться код цвета, а в метку – название цвета.
#ff0000: Красный
#ff7d00: Оранжевый
#ffff00: Желтый
#00ff00: Зеленый
#007dff: Голубой
#0000ff: Синий
#7d00ff: Фиолетовый
'''


def get_color(text_color, hex_color):
    l['text'] = text_color
    e.delete(0, END)
    e.insert(0, hex_color)


l = Label(root)
e = Entry(root, width=30, justify='center')
l.pack()
e.pack()

btn_red = Button(root, bg="#ff0000", command=lambda: get_color('Красный', '#ff0000')).pack(fill=X)
btn_orange = Button(root, bg="#ff7d00", command=lambda: get_color('Оранжевый', '#ff7d00')).pack(fill=X)
btn_yellow = Button(root, bg="#ffff00", command=lambda: get_color('Желтый', '#ffff00')).pack(fill=X)
btn_green = Button(root, bg="#00ff00", command=lambda: get_color('Зеленый', '#00ff00')).pack(fill='x')
btn_blue = Button(root, bg="#007dff", command=lambda: get_color('Голубой', '#007dff')).pack(fill='x')
btn_dark_blue = Button(root, bg="#0000ff", command=lambda: get_color('Синий', '#0000ff')).pack(fill='x')
btn_violet = Button(root, bg="#7d00ff", command=lambda: get_color('Фиолетовый', '#7d00ff')).pack(fill='x')

root.mainloop()
