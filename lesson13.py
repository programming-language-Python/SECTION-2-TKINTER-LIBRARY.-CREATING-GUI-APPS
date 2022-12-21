from tkinter import *

root = Tk()
root.geometry('600x400+1000+300')

main_menu = Menu(root)
root.config(menu=main_menu)


# # одно строчное меню
# main_menu.add_command(label='File')
# main_menu.add_command(label='About')

def about_program():
    print('ADOUT')


# File
# tearoff=1 - появляются линии по нажатию на которые появляется отдельное окошко с меню
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="Открыть")
file_menu.add_command(label="Сохранить")
# разделитель
file_menu.add_separator()
file_menu.add_command(label="Выход")
# add_cascade - кнопка меню, которое раскрывается при клике
main_menu.add_cascade(label='Файл', menu=file_menu)

# About
help_menu = Menu(main_menu, tearoff=0)
help_menu_sub = Menu(help_menu, tearoff=0)
help_menu_sub.add_command(label='Онлайн')
help_menu_sub.add_command(label='Оффлайн')
help_menu.add_cascade(label='Помощь', menu=help_menu_sub)
help_menu.add_command(label='О программе', command=about_program)
main_menu.add_cascade(label='Справка', menu=help_menu)

f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

# wrap - переносы текста
# insertbackground - цвет курсора
# selectbackground - цвет выделенного текста
# spacing3 - отступ между абзацами
t = Text(f_text, bg="#343D46", fg="#C6DEC1", padx=10, pady=10, wrap=WORD, insertbackground="#EDA756",
         selectbackground="#4E5A65", width=30, spacing3=10)
t.pack(fill=BOTH, expand=1, side=LEFT)

# command=t.yview() - связь текста и скроллбара с нужной оси
scroll = Scrollbar(f_text, command=t.yview())
scroll.pack(fill=Y, side=LEFT)
# устанавливаем scrollbar для текста
t.config(yscrollcommand=scroll.set)

root.mainloop()
