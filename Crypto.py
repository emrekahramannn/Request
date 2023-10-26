import requests
from requests.exceptions import HTTPError, ConnectionError
import tkinter
from tkinter import messagebox, PhotoImage


# UI
win = tkinter.Tk()
win.title("Crypto App")
win.config(padx=50, pady=30)
win.minsize(350, 450)
win.maxsize(350, 450)


FONT = ("Times New Roman", 14, "bold")


crypto_currency = tkinter.Label(text="Crypto Currency")
crypto_currency.config(font=FONT, pady=8)
crypto_currency.pack()

img = PhotoImage(file="crypto.png")
img_label = tkinter.Label(image=img)
img_label.pack()

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
        except ConnectionError as cnnct_err:
            messagebox.showerror(title="CONNECTION ERROR", message=f"Connection Error Has Occured: {cnnct_err}")
        except Exception as err:
            # if another error occur
            messagebox.showerror(title="ERROR", message=f"An Error Has Occured: {err}")
        else:
            # if request successful
            currency, price = check_status(response, currency)
            inform_user(currency, price)


def check_status(response, currency):
    """
    This function check the status of get request
    and returns necessary informations about data

    param1 -> response  : response object
    param2 -> currency  : str
    return -> tuple(str, str)
    """
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
                
    return crypto_currency, crypto_price


def inform_user(crypto_currency, crypto_price):
    """
    This function informs the user about the
    crypto of interest

    param1 -> crypto_currency : str
    param2 -> crypto_price : str
    """
    try:
        crypto_price = float(crypto_price)
    except ValueError as v_err:
        messagebox.showerror(title="Invalid Input", message=f"The Information About {crypto_currency} Is Not Valid")
    else:
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