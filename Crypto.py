import requests
from requests.exceptions import HTTPError
import tkinter
from tkinter import messagebox


# UI
win = tkinter.Tk()
win.title("Crypto App")
win.config(padx=50, pady=30)
win.minsize(350, 250)
win.maxsize(350,250)


FONT = ("Times New Roman", 14, "bold")


crypto_currency = tkinter.Label(text="Crypto Currency")
crypto_currency.config(font=FONT, pady=8)
crypto_currency.pack()

crypto_entry = tkinter.Entry(width=20)
crypto_entry.pack()


empty_label = tkinter.Label(pady=8)
empty_label.pack()



def show_crypto_info():
    currency = crypto_entry.get().strip().upper()

    if currency == "":
        messagebox.showerror(title="Invalid Input",message="Please Enter Currency!")
    else:
        try:
            # make a request to the website
            response = requests.get("https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json")
        except HTTPError as http_err:
            # if connection error occur
            messagebox.showerror(title="HTTP ERROR", message=f"HTTP Error Has Occured: {http_err}")
        except Exception as err:
            # if another error occur
            messagebox.showerror(title="ERROR", message=f"An Error Has Occured: {err}")

    # check if connection OK
    if response.status_code == 200:
        # retrieve data in json format
        for crypto in response.json():
            # check if input is in data as a key
            if currency == crypto["currency"]:
                # get necessary infos
                crypto_currency = crypto["currency"]
                crypto_price = crypto["price"]
                # exit loop
                break

    try:
        crypto_price = float(crypto_price)
    except ValueError as v_err:
        messagebox.showerror(title="Invalid Input", message=f"The Information About {crypto_currency} Is Not Valid")
            
    result_label.config(text=f"{crypto_currency} is ${round(crypto_price,2)}")
    crypto_entry.delete(0, tkinter.END)


calculate_btn = tkinter.Button(text="Price", command=show_crypto_info)
calculate_btn.config(width=15)
calculate_btn.pack()


empty_label2 = tkinter.Label(pady=3)
empty_label2.pack()

result_label = tkinter.Label(pady=8)
result_label.config(font=FONT)
result_label.pack()


win.mainloop()