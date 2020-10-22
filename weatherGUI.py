from tkinter import *
from tkinter import messagebox
import pyowm

owm = pyowm.OWM('5b307cb345d3bef73b070c9b38e5ca4a')

root = Tk()
root.title("WeatherInfo Pro Max XS")
root.geometry("350x300")

def Weather():
	place = message.get()
	mgr = owm.weather_manager()
	observation = mgr.weather_at_place(place)
	w = observation.weather
	temp = w.temperature('celsius')["temp"]
	wind = w.wind()["speed"]
	humidity = w.humidity
	clouds = w.clouds

	weather_in_label = "Current Weather in " + place
	status_label = "Status:  " + w.detailed_status
	temp_label = "Temperature:  " + str(temp) + " ℃"
	wind_label = "Wind:  " + str(wind) + " m/s"
	humidity_label = "Humidity:  " + str(humidity) + " %"
	clouds_label = "Clouds  " + str(clouds) + " %"

	Label(text=weather_in_label, fg="#0000CD").pack()
	Label(text=status_label, fg="#FF0000").pack()
	Label(text=temp_label, fg="#FF0000").pack()
	Label(text=wind_label, fg="#FF0000").pack()
	Label(text=humidity_label, fg="#FF0000").pack()
	Label(text=clouds_label, fg="#FF0000").pack()


Label(text="Enter your city name", fg="#0000CD").pack()

message = StringVar()

message_entry = Entry(textvariable=message)
message_entry.pack()

message_button = Button(text="Show Weather", command=Weather)
message_button.pack()
Label(text=" ").pack()

root.mainloop()



# created by h4cktivist