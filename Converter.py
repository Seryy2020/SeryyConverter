from tkinter import *
from tkinter import ttk
import urllib.request
import json
from tkinter import messagebox

root=Tk()
root.title("Конвертер валют")
root.geometry("300x250+1000+300")
root.resizable(False,False)

START_AMAUNT = 1000

def exchange():
    e_usd.delete(0, END)
    e_eur.delete(0, END)
    try:
        e_usd.insert(0, round(float(e_uah.get()) / float(JSON_object[1]['sale']), 2))
        e_eur.insert(0, round(float(e_uah.get()) / float(JSON_object[0]['sale']), 2))

    except:
        messagebox.showwarning('Warning', 'Чет не так!')


try:
    html = urllib.request.urlopen('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
    data = html.read()
    JSON_object = json.loads(data)
except:
    messagebox.showerror("Error", 'Ошибка получения')



header_frame = Frame(root)
header_frame.pack(fill=X)
header_frame.grid_columnconfigure(0, weight=1)
header_frame.grid_columnconfigure(1, weight=1)
header_frame.grid_columnconfigure(2, weight=1)


h_currancy = Label(header_frame, text="Валюта", bg="#ccc", font="Areal 12 bold")
h_currancy.grid(row=0, column=0, sticky=EW)
h_byu = Label(header_frame, text="Покупка", bg="#ccc", font="Areal 12 bold" )
h_byu.grid(row=0, column=1, sticky=EW)
h_sale = Label(header_frame, text="Продажа", bg="#ccc", font="Areal 12 bold")
h_sale.grid(row=0, column=2, sticky=EW)

usd_currancy = Label(header_frame, text="USD", font="Areal 10")
usd_currancy.grid(row=1, column=0, sticky=EW)
usd_byu = Label(header_frame, text=JSON_object[1]['buy'], font="Areal 10")
usd_byu.grid(row=1, column=1, sticky=EW)
usd_sale = Label(header_frame, text=JSON_object[1]['sale'], font="Areal 10")
usd_sale.grid(row=1, column=2, sticky=EW)

eur_currancy = Label(header_frame, text="EUR", font="Areal 10")
eur_currancy.grid(row=2, column=0, sticky=EW)
eur_byu = Label(header_frame, text=JSON_object[0]['buy'], font="Areal 10")
eur_byu.grid(row=2, column=1, sticky=EW)
eur_sale = Label(header_frame, text=JSON_object[0]['sale'], font="Areal 10")
eur_sale.grid(row=2, column=2, sticky=EW)

calc_frame = Frame(root, bg="#fff")
calc_frame.pack(expand=1, fill=BOTH)
calc_frame.grid_columnconfigure(1,weight=1)


r_uah = Label(calc_frame, text="Гривня", bg="#fff", font="Areal 10 bold")
r_uah.grid(row=0, column=0, padx=10)
e_uah = ttk.Entry(calc_frame, justify=CENTER, font="Areal 10")
e_uah.grid(row=0, column=1, columnspan=2, pady=10, padx=10, sticky=EW)
e_uah.insert(0, START_AMAUNT)

btn_calc = ttk.Button(calc_frame, text="Обмен", command=exchange)
btn_calc.grid(row=1, column=1, columnspan=2, sticky=EW, padx=10)

res_frame = Frame(root)
res_frame.pack(expand=1, fill=BOTH, pady=5)
res_frame.grid_columnconfigure(1, weight=1)

r_usd = Label(res_frame, text="USD", font="Areal 10 bold")
r_usd.grid(row=2, column=0)
e_usd = ttk.Entry(res_frame, justify=CENTER, font="Areal 10")
e_usd.grid(row=2, column=1, columnspan=2, padx=10, sticky=EW)
e_usd.insert(0, round(START_AMAUNT / float(JSON_object[1]['sale']), 2))


r_eur = Label(res_frame, text="EUR", font="Areal 10 bold")
r_eur.grid(row=3, column=0)
e_eur = ttk.Entry(res_frame, justify=CENTER, font="Areal 10")
e_eur.grid(row=3, column=1, columnspan=2, padx=10, sticky=EW)
e_eur.insert(0, round(START_AMAUNT / float(JSON_object[0]['sale']), 2))






root.mainloop()