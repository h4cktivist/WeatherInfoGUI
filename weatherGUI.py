from tkinter import *
from tkinter import messagebox
import pyowm

owm = pyowm.OWM('5b307cb345d3bef73b070c9b38e5ca4a')

root = Tk()
root.title("WeatherInfo Pro Max XS")
root.geometry("350x300")

def Weather():
	place = message.get()
	observation = owm.weather_at_place(place)
	w = observation.get_weather()
	temp = w.get_temperature('celsius')["temp"]
	wind = w.get_wind()["speed"]

	labelinfo1 = Label(text="Current Weather in ", fg="#0000CD")
	labelinfo1.pack()
	placelabel = Label(text=place, fg="#0000CD")
	placelabel.place(x=240, y=96)

	labelinfo2 = Label(text=w.get_detailed_status(), fg="#FF0000")
	labelinfo2.pack()
	labelinfo3 = Label(text=float(temp), fg="#FF0000")
	labelinfo3.pack()
	labelinfo4 = Label(text=wind, fg="#FF0000")
	labelinfo4.pack()

	laleltext1 = Label(text="Temperature (℃):", fg="#FF0000")
	laleltext1.place(x=10, y=138)
	laleltext2 = Label(text="Wind (m/s):", fg="#FF0000")
	laleltext2.place(x=10, y=160)
	laleltext3 = Label(text="Status: ", fg="#FF0000")
	laleltext3.place(x=10, y=120)



label1 = Label(text="Weather Info Pro", fg="#0000CD")
label1.pack()
label2 = Label(text="Enter your city name", fg="#0000CD")
label2.pack()

message = StringVar()

message_entry = Entry(textvariable=message)
message_entry.pack()

message_button = Button(text="Show Weather", command=Weather)
message_button.pack()

root.mainloop()



# created by h4cktivist