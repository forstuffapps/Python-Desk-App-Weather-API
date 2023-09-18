'''
C_Number = C0869346
Name : Vishal Reddy Guda

'''


import requests
from datetime import *
from PIL import ImageTk, Image
from urllib.request import urlopen
import requests
from tkinter import *
import os
from data_methods import Weather


Weather_Object = Weather()


Weather_Data = Weather_Object.get_api_data()


base_color = "#01213f"
second_color = '#acf0d1'
Highlight_color = '#D7263D'




def Search_City(Weather_Data):
	if Field_Text.get()=='':
		Weather_Data = Weather_Object.get_api_data()
	else:
		Weather_Data = Weather_Object.get_api_data(Field_Text.get())
	update_label_data(Weather_Data)


def Search_City_1():
	Search_City(Weather_Data)
	

TK_instance = Tk()
TK_instance.title("Weather Widget")
TK_instance.geometry("750x800")
TK_instance.configure(bg=base_color)

Label_7_Heading = Label(TK_instance, text="Weather", font=('Eras Bold ITC', 40), background=base_color, fg=second_color)
Label_7_Heading.pack()

Label_9_head_line = Label(TK_instance, text="We Will be showing todays Weather to the respective city", 
font=('Eras Bold ITC', 10), background=base_color, fg=second_color, anchor=CENTER)
Label_9_head_line.pack()

Label_8_city_heading = Label(TK_instance, text="City : ", font=('Eras Bold ITC', 20), 
background=base_color, fg=second_color)
Label_8_city_heading.pack()
Label_8_city_heading.place(x=100, y=130)

Field_Text = StringVar()
Entry_Field = Entry(TK_instance, textvariable=Field_Text, bd=3)
Entry_Field.pack()
Entry_Field.place(x=200, y=140)
Entry_Field.insert(0, 'Sarnia')
Button = Button(TK_instance, text="Search Weather", width=12, command=Search_City_1, bd=4)
Button.pack()
Button.place(x=200, y=180)


Label_9_Loc_Heading = Label(TK_instance, text="Location : ", font=('Eras Bold ITC', 20), 
background=base_color, fg=second_color)
Label_9_Loc_Heading.pack()
Label_9_Loc_Heading.place(x=35, y=240)

Label_1_Location = Label(TK_instance, text="", font=('Eras Bold ITC', 20), background=base_color, fg=second_color)
Label_1_Location.pack()
Label_1_Location.place(x=200, y=240)

Label_10_Temp_Heading = Label(TK_instance, text="Temperature : ", font=('Eras Bold ITC', 20), 
background=base_color, fg=second_color)
Label_10_Temp_Heading.pack()
Label_10_Temp_Heading.place(x=35, y=280)

Label_2_Temperature = Label(TK_instance, text="", font=('Eras Bold ITC', 20), 
background=base_color, fg=Highlight_color)
Label_2_Temperature.pack()
Label_2_Temperature.place(x=260, y=280)


Label_11_W_cond = Label(TK_instance, text="Weather Condition : ", font=('Eras Bold ITC', 20), 
background=base_color, fg=second_color)
Label_11_W_cond.pack()
Label_11_W_cond.place(x=35, y=350)
\
Label_3_Weather = Label(TK_instance, text="", font=('Eras Bold ITC', 20), 
background=base_color, fg=Highlight_color)
Label_3_Weather.pack()
Label_3_Weather.place(x=330, y=350)


def convert_to_Fahrenheit(Celcius):
	Celcius *= 9
	Celcius /= 5
	Celcius+=32
	return round(Celcius,2)

def update_label_data(Weather_Data):
	Label_1_Location['text'] = Weather_Data['City']
	print(Label_1_Location['text'], Weather_Data['City'])
	Weather_Data['Temperature'] = round(Weather_Data['Temperature'],2)
	Temperature = str(Weather_Data['Temperature'])+ ' ' +u"\u00b0C" + " \n "
	Temperature += str(convert_to_Fahrenheit(Weather_Data['Temperature'])) +  ' ' + u"\u00b0F"
	Label_2_Temperature['text'] =  Temperature
	Label_3_Weather['text'] = Weather_Data["Weather"]
	Image_Raw_Data = Weather_Object.get_image_raw_data(Weather_Data['Image_ID'])
	image_data = ImageTk.PhotoImage(data=Image_Raw_Data)
	Label_4_Image['image']=image_data
	Label_4_Image.image = image_data


Image_Raw_Data = Weather_Object.get_image_raw_data(Weather_Data['Image_ID'])
image_data = ImageTk.PhotoImage(data=Image_Raw_Data)
Label_4_Image = Label(TK_instance, image=image_data, background=second_color)
Label_4_Image.image = image_data
Label_4_Image.pack()
Label_4_Image.place(x=330,y=400)


Search_City(Weather_Data)




var_date = str(datetime.now()).split()[0]
var_time = datetime.now().strftime("%H:%M:%S")
date_and_time = 'Date : ' + var_date + '\t\t' + 'Time : ' +var_time

Label_5_Date = Label(TK_instance, text=date_and_time, font=('Eras Bold ITC', 20), 
background=base_color, fg=second_color)
Label_5_Date.pack()
Label_5_Date.place(x=45, y=540)


info = Weather_Data['Info']
info = 'Visibility : {}  \t  Wind Speed : {}\n\nHumidity : {}  \t  Pressure : {}'.format(*info)

Label_12_info = Label(TK_instance, text=info, font=('Eras Bold ITC', 20), 
background=base_color, fg=second_color)
Label_12_info.pack()
Label_12_info.place(x=35, y=600)


def date_n_time():
	var_date = str(datetime.now()).split()[0]
	var_time = datetime.now().strftime("%H:%M:%S")
	Label_5_Date['text']='Date : ' + var_date + '\t\t' + 'Time : ' +var_time
	TK_instance.after(1000,date_n_time)

TK_instance.after(1000,date_n_time)

Count_down_string_format = '\nThe Weather data gets auto updated in\t  seconds'


Label_13_Time = Label(TK_instance, text=Count_down_string_format, font=('Eras Bold ITC', 20), 
background=base_color, fg=second_color)
Label_13_Time.pack()
Label_13_Time.place(x=35, y=700)





Label_6_Timer = Label(TK_instance,text='', font=('Eras Bold ITC', 20), 
background=base_color, fg=Highlight_color)
Label_6_Timer.pack()
Label_6_Timer.place(x=583, y=700)



Label_14_my = Label(TK_instance,text='c0869346\nVishal Reddy', font=('Eras Bold ITC', 20), 
background=base_color, fg=Highlight_color)
Label_14_my.pack()
Label_14_my.place(x=500, y=130)




def Count_down_Timer(time_remaining):	
	if time_remaining<=0:
		print('inside')
		Search_City(Weather_Data)
		TK_instance.after(1000, Count_down_Timer, 30)
	else:
		Label_6_Timer["text"] = '\n' + str(time_remaining)
		TK_instance.after(1000, Count_down_Timer, time_remaining-1)

interval_minutes = Weather_Object.interval()
	
Count_down_Timer(interval_minutes * 60)

TK_instance.mainloop()


