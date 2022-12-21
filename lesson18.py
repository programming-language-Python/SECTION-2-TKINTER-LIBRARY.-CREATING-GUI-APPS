from tkinter import *
import time

root = Tk()


# https://ru.wikiversity.org/wiki/%D0%9A%D1%83%D1%80%D1%81_%D0%BF%D0%BE_%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B5_Tkinter_%D1%8F%D0%B7%D1%8B%D0%BA%D0%B0_Python


def tick():
    # лучше использовать 200, для точного вывода времени
    watch.after(200, tick)
    watch['text'] = time.strftime('%H:%M:%S')


watch = Label(root, font='Arial 70')
watch.pack()
tick()

root.mainloop()
