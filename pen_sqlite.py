# создание таблицы
# db.create_table(Pen)
from pen_sqlite_models import *
import tkinter as tk


# прочитать базу
def get_base():
    resultat = []
    for i in Pen.select():
        resultat.append((i.id, i.brand, i.color))

    b = 4
    for i in resultat:
        tk.Label(win, text=b - 3, bg='#b5c5c9').grid(row=b, column=0, padx=5, pady=5)  # номер по списку
        tk.Label(win, text=i).grid(row=b, column=1, columnspan=3, stick='we', padx=5, pady=5)  # значение списка
        b += 1

    for i in range(b, 12):
        tk.Label(win, bg='#b5c5c9').grid(row=b, column=0, padx=5, pady=5)  # закрашивание номер по списку
        tk.Label(win, bg='#b5c5c9').grid(row=b, column=1, columnspan=3, stick='we', padx=5,
                                         pady=5)  # закрашивание значение списка


# Удалить запись
def delete_id():
    for i in Pen.select().where(Pen.id == entr3.get()):
        i.delete_instance()
    get_base()


# добавить значение
def get_entry():
    Pen.create(brand=entr1.get(), color=entr2.get())
    get_base()


# Заменить значение
def updatee():
    for i in Pen.select().where(Pen.id == entr4.get()):
        i.brand = entr5.get()
        i.save()
        i.color = entr6.get()
        i.save()
    get_base()
    print('done')


win = tk.Tk()
win.title('PEN2')
photo = tk.PhotoImage(file='PEN.png')
win.iconphoto(False, photo)
win.config(bg='#b5c5c9')
win.geometry('870x500+520+450')
win.resizable(False, False)

label_1 = tk.Label(text='Pen', bg='#b5c5c9').grid(row=1, column=0, padx=5, pady=5, stick='e')
label_2 = tk.Label(win, text='Brend', bg='#b5c5c9').grid(row=0, column=1, padx=5, pady=5, stick='we')
label_3 = tk.Label(win, text='Color', bg='#b5c5c9').grid(row=0, column=2, padx=5, pady=5)
label_4 = tk.Label(win, text='Delete ID', bg='#b5c5c9').grid(row=2, column=0, padx=5, pady=5, stick='e')
label_5 = tk.Label(win, text='№', bg='#b5c5c9').grid(row=3, column=0, padx=5, pady=5, stick='we')
label_6 = tk.Label(win, text='Update ID', bg='#b5c5c9').grid(row=0, column=4, padx=5, pady=5, stick='we')
label_7 = tk.Label(win, text='Update Brand', bg='#b5c5c9').grid(row=0, column=5, padx=5, pady=5, stick='we')
label_8 = tk.Label(win, text='Update Color', bg='#b5c5c9').grid(row=0, column=6, padx=5, pady=5, stick='we')

bt1 = tk.Button(win, text='Download', command=get_entry).grid(row=1, column=3, padx=5, pady=5, stick='we')
bt2 = tk.Button(win, text='Print DataBase', command=get_base).grid(row=3, column=1, padx=5, pady=5, columnspan=3,
                                                                   stick='we')
bt3 = tk.Button(win, text='Delete', command=delete_id).grid(row=2, column=3, padx=5, pady=5, stick='we')
bt4 = tk.Button(win, text='Update', command=updatee).grid(row=1, column=7, padx=5, pady=5, stick='we')

entr1 = tk.Entry(win)  # Brand
entr1.grid(row=1, column=1, padx=5, pady=5)
entr2 = tk.Entry(win)  # Color
entr2.grid(row=1, column=2, padx=5, pady=5)
entr3 = tk.Entry(win)  # Delete ID
entr3.grid(row=2, column=1, padx=5, pady=5)
entr4 = tk.Entry(win)  # Update ID
entr4.grid(row=1, column=4, padx=5, pady=5)
entr5 = tk.Entry(win)  # Update Brand
entr5.grid(row=1, column=5, padx=5, pady=5)
entr6 = tk.Entry(win)  # Update Color
entr6.grid(row=1, column=6, padx=5, pady=5)

for i in range(0, 20):
    win.grid_rowconfigure(i, minsize=15)  # задать высоту колонки
    win.grid_columnconfigure(i, minsize=60)  # задать ширину колонки

win.mainloop()
