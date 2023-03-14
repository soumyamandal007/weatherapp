from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

root = Tk()
root.title("Weather App")
root.geometry("890x470+300+200")
root.configure(bg="lightblue")
root.resizable(False,False)

def getWeather():
   city = textfield.get()
   try:
      geolocator = Nominatim(user_agent="geopiExcercises")
      location = geolocator.geocode(city)
      obj = TimezoneFinder()
      result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
      #print(result)
      home = pytz.timezone(result)
      local_time = datetime.now(home)
      curreny_time = local_time.strftime("%I:%M %p")
      clock.config(text=curreny_time)
      name.config(text="CURRENT WEATHER")
   
      #wetaher
      url = "http://api.openweathermap.org/data/2.5/weather"
      params = {
         "q": city, # replace with the city you want to get weather for
         "appid": "{API_KEY}", # replace with your API key from OpenWeatherMap
         "units": "metric" # units for temperature (metric for Celsius, imperial for Fahrenheit)
         }
   
      json_data = requests.get(url,params=params).json()
      temperature = json_data['main']["temp"]
      # print(json_data)
      # print(f"The current temperature is {temperature} degrees Celsius.")
      condition = json_data['weather'][0]['main']
      description = json_data['weather'][0]['main']
      temp = int(json_data['main']['temp'])
      pressure = json_data['main']['pressure']
      humidity = json_data['main']['humidity']
      wind = json_data['wind']['speed']
   
      t.config(text=(temp))
      c.config(text=(condition,"|","Feels","Like",temp))
   
      w.config(text=wind)
      h.config(text=humidity)
      d.config(text=description)
      p.config(text=pressure)
   except Exception as e:
      messagebox.showerror("Weather App","Invalid Entry")

   
   
   
    

##searchbox
Search_image = PhotoImage(file="Rounded Rectangle 3.png")
myImage = Label(image=Search_image,bg="lightblue")
myImage.place(x=20,y=30)
textfield = tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#203243", borderwidth=0.5,fg="white")
textfield.place(x=50,y=40)
textfield.focus()
searchicon = PhotoImage(file="Layer 6.png")
searchbutton = Button(image = searchicon, borderwidth=0,cursor="hand2",bg="#203243",command=getWeather)
searchbutton.place(x=375,y=35)


#logo
logoimage = PhotoImage(file="logo.png")
logolabel = Label(image=logoimage,bg="lightblue")
logolabel.place(x=160,y=100)


#bottom box

#time
name = Label(root,font=("arial",15,"bold"),bg="lightblue")
name.place(x=30,y=100)
clock = Label(root,font=("Helvetica",20),bg="lightblue")
clock.place(x=30,y=130)


#labels
label1 = Label(root,text="WIND",font=("Helvetica",15,"bold"),fg="black",bg="lightblue")
label1.place(x=110,y=350)

label2 = Label(root,text="HUMIDITY",font=("Helvetica",15,"bold"),fg="black",bg="lightblue")
label2.place(x=230,y=350)

label3 = Label(root,text="DESCRIPTION",font=("Helvetica",15,"bold"),fg="black",bg="lightblue")
label3.place(x=400,y=350)

label4 = Label(root,text="PRESSURE",font=("Helvetica",15,"bold"),fg="black",bg="lightblue")
label4.place(x=625,y=350)

t = Label(font=("arial",70,"bold"),fg="black",bg="lightblue")
t.place(x=400,y=150)
c = Label(font=("arial",15,"bold"),fg="black",bg = "lightblue")
c.place(x=400,y=250)



w = Label(text="...",font=("arial",20,"bold"),bg="lightblue")
w.place(x=110,y=380)
h = Label(text="...",font=("arial",20,"bold"),bg="lightblue")
h.place(x=230,y=380)
d = Label(text="...",font=("arial",20,"bold"),bg="lightblue")
d.place(x=400,y=380)
p = Label(text="...",font=("arial",20,"bold"),bg="lightblue")
p.place(x=625,y=380)

root.mainloop()
