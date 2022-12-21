from tkinter import *

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


class ColorsOfRainbow:
    def __init__(self):
        self.colors = {
            '#ff0000': 'Красный',
            '#ff7d00': 'Оранжевый',
            '#ffff00': 'Желтый',
            '#00ff00': 'Зеленый',
            '#007dff': 'Голубой',
            '#0000ff': 'Синий',
            '#7d00ff': 'Фиолетовый',
        }

    def run(self):
        self.get_buttons()

    def get_buttons(self):
        colors = self.colors.items()
        for hex_color, color_name in colors:
            self.get_button(hex_color, color_name)

    def get_button(self, hex_color, color_name):
        btn = Button(root, bg=hex_color,
                     command=lambda: self.get_color(hex_color, color_name))
        return btn.pack(fill=X)

    def get_color(self, hex_color, color_name):
        label['text'] = hex_color
        entry.delete(0, END)
        entry.insert(0, color_name)


root = Tk()
root.geometry('600x400+1000+300')

label = Label(root, text='Поле ввода')
label.pack()

entry = Entry(root)
entry.pack()

colors_of_rainbow = ColorsOfRainbow()
colors_of_rainbow.run()

# обработчик событий окна
root.mainloop()
