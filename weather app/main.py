from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import requests

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=01b041e64695487780a1506ec7950b55").json()
    w_label1.config(text=data["weather"][0]["main"])
    wd_label1.config(text=data["weather"][0]["description"])
    wt_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    wr_label1.config(text=data["main"]["pressure"])


win = Tk()
win.title("Welcome to Weather App............!")
win.config(bg="black")
win.geometry("1000x1000")

name_label = Label(win, text="Weather App", font=("Time New Roman", 50, "bold italic underline"), background="black", foreground="white")
name_label.place(x=30, y=30, height=100, width=950)

city_name = StringVar()
list_name = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
    "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya",
    "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
    "Uttar Pradesh", "Uttarakhand", "West Bengal"]

com = ttk.Combobox(win, text="Weather App", values=list_name, font=("Time New Roman", 20), foreground="black", textvariable=city_name)
com.place(x=30, y=150, height=50, width=450)

image_path = "C:/Users/admin/Documents/img/vedu.jpg"  # Replace with the actual path to your image file
img = Image.open(image_path)
img = ImageTk.PhotoImage(img)

img_label = Label(win, image=img, width=470, height=300)
img_label.place(x=500, y=150)

w_label = Label(win, text="Weather climate : ", font=("Time New Roman", 15, "bold italic"), foreground="white" , background="black")
w_label.place(x=10, y=300, height=30, width=250)

w_label1 = Label(win, font=("Time New Roman", 15, "bold italic"), foreground="white" , background="black")
w_label1.place(x=280, y=300, height=30, width=120)

wd_label = Label(win, text="Weather Description : ", font=("Time New Roman", 15, "bold italic"), foreground="white" , background="black")
wd_label.place(x=30, y=340, height=30, width=250)

wd_label1 = Label(win, font=("Time New Roman", 15, "bold italic"), foreground="white" , background="black")
wd_label1.place(x=280, y=340, height=20, width=120)

wt_label = Label(win, text="Temperature : ", font=("Time New Roman", 15, "bold italic"), foreground="white" , background="black")
wt_label.place(x=-10, y=380, height=30, width=250)

wt_label1 = Label(win,  font=("Time New Roman", 15, "bold italic"), foreground="white" , background="black")
wt_label1.place(x=280, y=380, height=30, width=120)

wr_label = Label(win, text="Pressure : ", font=("Time New Roman", 15, "bold italic"), foreground="white" , background="black")
wr_label.place(x=-30, y=420, height=30, width=250)

wr_label1 = Label(win,  font=("Time New Roman", 15, "bold italic"), foreground="white" , background="black")
wr_label1.place(x=280, y=420, height=30, width=120)


done_button = Button(win, text="Done", font=("Time New Roman", 15), foreground="black", command=data_get)
done_button.place(x=200, y=210, height=40, width=100)

win.mainloop()
