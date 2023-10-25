import requests
import tkinter
from requests.exceptions import HTTPError, ConnectionError
from tkinter import PhotoImage

# UI
win = tkinter.Tk()
win.title("WEATHER APPLICATION")
win.config(padx=50, pady=50)
win.minsize(500,575)
win.maxsize(500,575)

FONT = ("TİMES NEW ROMAN", 14, "bold")

img = PhotoImage(file="weather.png")
img_label = tkinter.Label(image=img)
img_label.config(pady=8)
img_label.pack()

city_label = tkinter.Label(text="CITY")
city_label.config(pady=5, font=FONT)
city_label.pack()

city_entry = tkinter.Entry(width=25)
city_entry.pack()


empty_label = tkinter.Label(pady=10)
empty_label.pack()




def get_info():
    city = city_entry.get().strip().capitalize()
    with open("api_key.txt", mode="r", encoding="utf-8") as fhandle:
        api_key = fhandle.readline().strip()
    
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']

        try:
            temp = temp - 273.15
        except:
            pass

        result_label.config(text=f"{city.upper()}\nTemperature: {round(temp,1)} Celcius\nDescription: {desc}")
        city_entry.delete(0, tkinter.END)
    else:
        print('Error fetching weather data')


weather_btn = tkinter.Button(text="WEATHER", font=FONT, command=get_info)
weather_btn.pack()


empty_label2 = tkinter.Label(pady=5)
empty_label2.pack()


result_label = tkinter.Label()
result_label.config(font=FONT)
result_label.pack()

win.mainloop()