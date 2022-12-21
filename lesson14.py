from tkinter import *

root = Tk()
root.geometry('1000x500+800+300')

main_menu = Menu(root)
root.config(menu=main_menu)


def about_program():
    print('ADOUT')


def change_theme(theme):
    t['bg'] = theme_colors[theme]['text_bg']
    t['fg'] = theme_colors[theme]['text_fg']
    t['insertbackground'] = theme_colors[theme]['cursor']
    t['selectbackground'] = theme_colors[theme]['select_bg']


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

# Theme
theme_menu = Menu(main_menu, tearoff=0)
theme_menu_sub = Menu(theme_menu, tearoff=0)
theme_menu_sub.add_command(label="Light Theme", command=lambda: change_theme('light'))
theme_menu_sub.add_command(label="Dark Theme", command=lambda: change_theme('dark'))
theme_menu.add_cascade(label="Оформление", menu=theme_menu_sub)
theme_menu.add_command(label="О программе", command=about_program)
main_menu.add_cascade(label="Разное", menu=theme_menu)

f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

theme_colors = {
    "dark": {
        "text_bg": "#343D46", "text_fg": "#fff", "cursor": "#EDA756", "select_bg": "#4E5A65"
    },
    "light": {
        "text_bg": "#fff", "text_fg": "#000", "cursor": "#8000FF", "select_bg": "#777"
    }
}

# wrap - переносы текста
# insertbackground - цвет курсора
# selectbackground - цвет выделенного текста
# spacing3 - отступ между абзацами
t = Text(f_text, bg=theme_colors['dark']['text_bg'], fg=theme_colors['dark']['text_fg'], padx=10, pady=10, wrap=WORD,
         insertbackground=theme_colors['dark']['cursor'], selectbackground=theme_colors['dark']['select_bg'], width=30,
         spacing3=10, font=("Courier New", 11))
t.pack(fill=BOTH, expand=1, side=LEFT)

# command=t.yview() - связь текста и скроллбара с нужной оси
scroll = Scrollbar(f_text, command=t.yview())
scroll.pack(fill=Y, side=LEFT)
# устанавливаем scrollbar для текста
t.config(yscrollcommand=scroll.set)

root.mainloop()
