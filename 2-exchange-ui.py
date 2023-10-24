import requests
from requests.exceptions import HTTPError
import tkinter
from tkinter import messagebox

# UI
# Window
win = tkinter.Tk()
win.title("Exchange Office")
win.config(padx=45, pady=45)

FONT = ("Arial", 12, "bold")

# Bozulacak Para
bozulacak_para = tkinter.Label(text="Bozulacak döviz türü", font=FONT, pady=8)
bozulacak_para.pack()

bozulacak_para_entry = tkinter.Entry(width=15)
bozulacak_para_entry.focus()
bozulacak_para_entry.pack()

# Alinacak Para
alinacak_para = tkinter.Label(text="Alınacak döviz türü", font=FONT, pady=8)
alinacak_para.pack()

alinacak_para_entry = tkinter.Entry(width=15)
alinacak_para_entry.pack()

# Bozulacak Miktar
bozulacak_miktar = tkinter.Label(text="Bozulacak döviz tutarı", font=FONT, pady=8)
bozulacak_miktar.pack()

bozulacak_miktar_entry = tkinter.Entry(width=15)
bozulacak_miktar_entry.pack()

# Bosluk
empty_label = tkinter.Label(pady=8)
empty_label.pack()


# API (old api)
api_url = "https://api.exchangeratesapi.io/latest?base="    

def exchange_currency():
    bozulacak_doviz = bozulacak_para_entry.get().strip().upper()
    alinacak_doviz = alinacak_para_entry.get().strip().upper()
    miktar = bozulacak_miktar_entry.get().strip()

    try:
        miktar = float(miktar)
    except ValueError:
        messagebox.showerror(title="Geçersiz Tutar", message="Lütfen doğru tutar giriniz!")
        bozulacak_para_entry.delete(0, tkinter.END)
        alinacak_para_entry.delete(0, tkinter.END)
        bozulacak_miktar_entry.delete(0, tkinter.END)
    else:
        calculate_currency(bozulacak_doviz, alinacak_doviz, miktar)



def calculate_currency(bozulacak, alinacak, miktar):
    try:
        response = requests.get(api_url + bozulacak)
        response_json = response.json()
    except HTTPError as http_err:
        messagebox.showerror(title="BAĞLANTI HATASI", message=f"HTTP Hatası {http_err}")
    except Exception as err:
        messagebox.showerror(title="HATA", message=f"Hata {err}")

    print(f"1 {0} = {1} {2}".format(bozulacak, response_json["rates"][alinacak], alinacak))
    print("{0} {1} = {2} {3}".format(miktar, bozulacak, miktar * response_json["rates"][alinacak], alinacak))



exchange_btn = tkinter.Button(text="Exchange", font=FONT, command=exchange_currency,pady=8)
exchange_btn.pack()


win.mainloop()