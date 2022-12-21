from tkinter import *
from tkinter import filedialog
import os
import shutil
from datetime import datetime

'''
Программа, которая сортирует фотографии по папкам.
Папки имеют названия сопоставимые с датой создания файла.
Формат наименования 2022.12.30 (год месяц день)
Путь по которой ищет программа должна удалить файлы, которые там находились.
'''

root = Tk()


def get_path(entry):
    folder = filedialog.askdirectory(title='Выбор папки для сортировки')
    entry.delete(0, END)
    entry.insert(0, folder)


def get_file_creation_date(path_to_file):
    file_creation_time = os.path.getmtime(path_to_file)
    file_creation_date = datetime.fromtimestamp(file_creation_time)
    return file_creation_date.strftime("%Y-%m-%d")


def get_new_path_to_file(photo_sorting_path, file_creation_date, path_to_file):
    new_path_to_folder = os.path.join(photo_sorting_path, file_creation_date)
    is_dir = os.path.isdir(new_path_to_folder)
    if not is_dir:
        os.mkdir(new_path_to_folder)
    file = os.path.basename(path_to_file)
    return os.path.join(new_path_to_folder, file)


def create_photo_folders(photo_sorting_path, path_to_file):
    file_creation_date = get_file_creation_date(path_to_file)
    new_path_to_file = get_new_path_to_file(photo_sorting_path, file_creation_date, path_to_file)
    shutil.move(path_to_file, new_path_to_file)


def sort_photos(path_to_photos, photo_sorting_path):
    for dirname, dirnames, filenames in os.walk(path_to_photos):
        if filenames:
            for file in filenames:
                path_to_file = os.path.join(dirname, file)
                create_photo_folders(photo_sorting_path, path_to_file)
        if dirnames:
            for sub_dirname in dirnames:
                sort_photos(sub_dirname, photo_sorting_path)


# path_with_photos
label_path_with_photos = Label(root, text='В какой папке лежат фотографии?')
label_path_with_photos.pack(padx=10, pady=10)

entry_path_with_photos = Entry(root)
entry_path_with_photos.pack(fill=X, padx=10)

btn_path_with_photos = Button(root, text='Выбрать путь', command=lambda: get_path(entry_path_with_photos))
btn_path_with_photos.pack(fill=X, padx=10, pady=10)

# photo_sorting_path
label_photo_sorting_path = Label(root, text='Куда отправить отсортированные фотографии?')
label_photo_sorting_path.pack(padx=10)

entry_photo_sorting_path = Entry(root)
entry_photo_sorting_path.pack(fill=X, padx=10, pady=10)

btn_photo_sorting_path = Button(root, text='Выбрать путь',
                                command=lambda: get_path(entry_photo_sorting_path))
btn_photo_sorting_path.pack(fill=X, padx=10)

# sorted_photos
btn_sorted_photos = Button(root, text='Сортировать фотографии',
                           command=lambda: sort_photos(entry_path_with_photos.get(), entry_photo_sorting_path.get()))
btn_sorted_photos.pack(fill=X, padx=10, pady=10)

root.mainloop()
