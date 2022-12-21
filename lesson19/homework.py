from tkinter import *

root = Tk()

'''По нажатии закрашивать Label по нажатому цвету. Если нажать правой кнопкой мыши на любую кнопку то будет изменён 
на цвет по умолчанию (белый) '''

colors = {
    "#ff0000": "Красный",
    "#ff7d00": "Оранжевый",
    "#ffff00": "Желтый",
    "#00ff00": "Зеленый",
    "#007dff": "Голубой",
    "#0000ff": "Синий",
    "#7d00ff": "Фиолетовый",
}


class MyButtons:

    def __init__(self, master, text_color, hex_color):
        self.text_color = text_color
        self.hex_color = hex_color
        self.b = Button(master, bg=hex_color, command=self.get_color)
        self.b.pack(fill=X)
        self.b.bind("<Button-1>", lambda event: f_event(event, self.hex_color))
        self.b.bind("<Button-3>", lambda event: f_event(event, 'white'))

    def get_color(self):
        l['text'] = self.text_color
        e.delete(0, END)
        e.insert(0, self.hex_color)


def f_event(event, bg):
    e['bg'] = bg


l = Label(root)
e = Entry(root, width=30, justify='center')
l.pack()
e.pack()

for k, v in colors.items():
    MyButtons(root, v, k)

root.mainloop()
