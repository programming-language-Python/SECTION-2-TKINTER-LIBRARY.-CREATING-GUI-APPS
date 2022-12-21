from tkinter import *
import urllib.request
import json
from tkinter import messagebox
from urllib.error import HTTPError

'''
Приложение должно выводить:
1. Курсы на сегодняшний день (https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5)
2. Поле Entry с значением по умолчанию (1000)
3. Внизу кнопка "обменять"
4. Должен выводить сколько долларов, евро и гривней получим за 1000 рублей
5. Ошибку если не удалось получить валюты
'''

root = Tk()
root.title('Конвертер валют')
root.geometry("200x450+1000+300")
root.resizable(True, False)

sticky = W + E

currency_name = Label(root, text='Наименование курса')
currency_name.grid(row=0, column=0, padx=10, pady=10, sticky=sticky)

course = Label(root, text='Курс')
course.grid(row=0, column=1, padx=10, pady=10, sticky=sticky)

try:
    currency_json_url = "https://www.cbr-xml-daily.ru/daily_json.js"
    with urllib.request.urlopen(currency_json_url) as url:
        read_url = url.read()
        decode_url = read_url.decode()
        data = json.loads(decode_url)
        eur = data['Valute']['EUR']
        usd = data['Valute']['USD']
        uah = data['Valute']['UAH']
        list_of_currencies = [eur, usd, uah]
except HTTPError:
    messagebox.showwarning('Ошибка', 'Не удалось получить данные валют')
    exit()

row = 1
for currency in list_of_currencies:
    currency_name = currency['Name']
    Label(root, text=currency_name).grid(row=row, padx=10, pady=10, sticky=sticky)

    currency_value = round(currency['Value'], 2)
    Label(root, text=currency_value).grid(row=row, column=1, padx=10, pady=10, sticky=sticky)

    row += 1


def validate(value):
    return value == "" or value.isnumeric()


Label(root, text='Обменять рубли').grid(row=row, padx=10, sticky=sticky)
# %P - знаки пунктуации
validate_command = (root.register(validate), '%P')
e = Entry(root, validate='key', validatecommand=validate_command)
row += 1
e.grid(row=row, padx=10, pady=10)
DEFAULT_VALUE = 1000
e.insert(END, DEFAULT_VALUE)


def exchange(currencies):
    ruble = int(e.get())
    row = 7
    for currency_data in currencies:
        currency_name = currency_data['Name']
        currency_value = float(currency_data['Value'])
        currency_value_per_ruble = round(ruble / currency_value, 2)
        Label(root, text=currency_name).grid(row=row, column=0, padx=10, pady=10, sticky=sticky)
        Label(root, text=currency_value_per_ruble).grid(row=row, column=1, padx=10, pady=10, sticky=sticky)
        row += 1


btn_exchange = Button(root, text="Обменять",
                      command=lambda: exchange(list_of_currencies))
btn_exchange.grid(row=row + 1, padx=10, pady=10)

root.mainloop()
