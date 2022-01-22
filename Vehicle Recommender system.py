#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="*******",
  database="k19ky",
  use_pure=True
)

mycursor = mydb.cursor()
specification={} #dictionary to store selected values from the options

root= Tk()
f={} #f is the dictionary used for frame
for i in range(10):
    f[i]= Frame(root)

f[0].pack()

#next function is used for going to the next frame
def next(x):
    f[x].pack_forget()
    f[x+1].pack()

#first function is used for going to the first frame to try again all the steps    
def first():
    f[9].pack_forget()
    f[0].pack()


#submit function is used for going to the final frame and giving the required output
def submit(x):
    f[x].pack_forget()
    f[x+1].pack()
    Label(f[9], text="Recommended vehicle according to your choice are shown below",height="5", font="Times 20 bold").pack()
    specification[1]=int(v1.get())
    specification[2]=int(v2.get())
    specification[3]=int(v3.get())
    specification[4]=int(v4.get())
    specification[5]=int(v5.get())
    specification[6]=v6.get()
    specification[7]=v7.get()
    specification[8]=int(v8.get())
    sql="SELECT Name, Price FROM vehicles WHERE wheels=%s and space>=%s and Look>=%s and Seats=%s and FuelEfficiency>=%s and FuelEfficiency<=%s and TransmissionSystem=%s and FuelType=%s and Price<%s" 
    value=(specification[1],specification[2],specification[3],specification[4],specification[5],specification[5]+10,specification[6],specification[7],specification[8])
    mycursor.execute(sql, value)
    myresult=mycursor.fetchall()
    for name in myresult:
        Label(f[9], text=name[0], fg="red", font="Times 20 bold").pack()
        Label(f[9], text="Rs.", font="50").pack()
        Label(f[9], text=name[1], font="50").pack()
    l18 = Label(f[9], text ='Note: you can use try again button to use the system again.', font="Times 20 bold", height="5", fg="green")  
    l18.pack()#l0 is the variable for label
    button1 = Button(f[9], text ="Try Again", fg ="blue",font="150",pady="5", command=lambda:first() )
    button1.pack()

root.geometry("350x150")
l0 = Label(f[0], text ='VEHICLE RECOMMENDER SYSTEM', font="Times 30 bold", height="5")  
l0.pack()#l0 is the variable for label

img = PhotoImage(file = r"C:\Users\HP\Pictures\car.png") 
img1 = img.subsample(1, 1) 
  
Label(f[0], image = img1).pack()

l1 = Label(f[0], text ='Note: This system has the information of only two wheeler and four wheeler vehicles', font="Times 20 bold", height="5", fg="green")  
l1.pack()#l1 is the variable for label

button1 = Button(f[0], text ="I am ready to find a new vehicle", fg ="red",font="150", command=lambda:next(0) )
button1.pack()

l2 = Label(f[1], text = 'What type of vehicle you are looking for?', font="Times 20 bold", height="5")
l2.pack(side="top")#l2 is the variable for label

#Below r1,r2 are the variable for the radiobuttons of the type of vehicle and v1 is the variable for selected wheels in the vehicle
v1= IntVar()          
r1= Radiobutton(f[1], text = "Two wheeler",font="50",value=2, variable = v1).pack()
r2= Radiobutton(f[1], text = "Four wheeler",font="50",value=4, variable = v1).pack()

l3 = Label(f[1], text ='Note*: It is mandatory to select any one of the above field.', font="20", height="5", fg="green")  
l3.pack()#l3 is the variable for label

button2 = Button(f[1], text ="Next", fg ="red",font="150", command=lambda:next(1) )
button2.pack()

l4 = Label(f[2], text = 'Rate the space u require in vehicle on 10 ', font="Times 20 bold", height="5")
l4.pack(side="top")#l4 is the variable for label

#Below sp1,sp2,sp3,sp4,sp5,sp6,sp7,sp8,sp9,sp10 are the variables for the radiobuttons of space and v2 is the variable for the selected space in the vehicle
v2=IntVar()
sp1= Radiobutton(f[2], text = "More than 1",font="50",value=1, variable = v2).pack()
sp2= Radiobutton(f[2], text = "More than 2",font="50",value=2, variable = v2).pack()
sp3= Radiobutton(f[2], text = "More than 3",font="50",value=3, variable = v2).pack()
sp4= Radiobutton(f[2], text = "More than 4",font="50",value=4, variable = v2).pack()
sp5= Radiobutton(f[2], text = "More than 5",font="50",value=5, variable = v2).pack()
sp6= Radiobutton(f[2], text = "More than 6",font="50",value=6, variable = v2).pack()
sp7= Radiobutton(f[2], text = "More than 7",font="50",value=7, variable = v2).pack()
sp8= Radiobutton(f[2], text = "More than 8",font="50",value=8, variable = v2).pack()
sp9= Radiobutton(f[2], text = "More than 9",font="50",value=9, variable = v2).pack()
sp10= Radiobutton(f[2], text = "More than 10",font="50",value=10, variable = v2).pack()

l5 = Label(f[2], text ='Note*: It is mandatory to select any one of the above field.', font="20", height="5", fg="green")  
l5.pack()#l5 is the variable for label

button3 = Button(f[2], text ="Next", fg ="red",font="150", command=lambda:next(2) )
button3.pack()

l6 = Label(f[3], text = 'Rate the look u require in vehicle on 10 ', font="Times 20 bold", height="5")
l6.pack(side="top")#l6 is the variable for label

#Below L1,L2,L3,L4,L5,L6,L7,L8,L9,L10 are the variables for the radiobuttons and v3 is the variable for the selected look of the vehicle 
v3=IntVar()
L1= Radiobutton(f[3], text = "More than 1",font="50",value=1, variable = v3).pack()
L2= Radiobutton(f[3], text = "More than 2",font="50",value=2, variable = v3).pack()
L3= Radiobutton(f[3], text = "More than 3",font="50",value=3, variable = v3).pack()
L4= Radiobutton(f[3], text = "More than 4",font="50",value=4, variable = v3).pack()
L5= Radiobutton(f[3], text = "More than 5",font="50",value=5, variable = v3).pack()
L6= Radiobutton(f[3], text = "More than 6",font="50",value=6, variable = v3).pack()
L7= Radiobutton(f[3], text = "More than 7",font="50",value=7, variable = v3).pack()
L8= Radiobutton(f[3], text = "More than 8",font="50",value=8, variable = v3).pack()
L9= Radiobutton(f[3], text = "More than 9",font="50",value=9, variable = v3).pack()
L10= Radiobutton(f[3], text = "More than 10",font="50",value=10, variable = v3).pack()

l7 = Label(f[3], text ='Note*: It is mandatory to select any one of the above field.', font="20", height="5", fg="green")  
l7.pack()#l7 is the variable for label

button4 = Button(f[3], text ="Next", fg ="red",font="150", command=lambda:next(3) )
button4.pack()

l8 = Label(f[4], text = 'Select the seats you require in your vehicle ', font="Times 20 bold", height="5")
l8.pack(side="top")#l8 is the variable for label

#Below st1,st2,st3,st4 are the variables for radiobuttons for the number of seats in the vehicle and v4 is the variable for selected seats
v4=IntVar()
st1= Radiobutton(f[4], text ="2",font="50",value=2, variable = v4).pack()
st2= Radiobutton(f[4], text ="4",font="50",value=4, variable = v4).pack()
st3= Radiobutton(f[4], text ="5",font="50",value=5, variable = v4).pack()
st4= Radiobutton(f[4], text ="6",font="50",value=6, variable = v4).pack()

l9 = Label(f[4], text = 'Note*: It is mandatory to select any one of the above field (For two wheeler vehicle select two seats).', font="50", height="5", fg='green')
l9.pack()#l9 is the variable for label

button5 = Button(f[4], text ="Next", fg ="red",font="150", command=lambda:next(4) )
button5.pack()

l10 = Label(f[5], text = 'Select the fuel efficiency you require in your vehicle ', font="Times 20 bold", height="5")
l10.pack(side="top")#l10 is the variable for label

#Below F1,F2,F3,F4,F5,F6,F7,F8,F9,F10 are variables for radiobutton for fuel efficiency and v5 is the variable for selected fuel eficiency option of the vehicle
v5=IntVar()
F1= Radiobutton(f[5], text = "0kh/L to 10km/L",font="50",value=0, variable = v5).pack()
F2= Radiobutton(f[5], text = "10km/L to 20km/L",font="50",value=10, variable = v5).pack()
F3= Radiobutton(f[5], text = "20km/L to 30km/L",font="50",value=20, variable = v5).pack()
F4= Radiobutton(f[5], text = "30km/L to 40km/L",font="50",value=30, variable = v5).pack()
F5= Radiobutton(f[5], text = "40km/L to 50km/L",font="50",value=40, variable = v5).pack()
F6= Radiobutton(f[5], text = "50km/L to 60km/L",font="50",value=50, variable = v5).pack()
F7= Radiobutton(f[5], text = "60km/L to 70km/L",font="50",value=60, variable = v5).pack()
F8= Radiobutton(f[5], text = "70km/L to 80km/L",font="50",value=70, variable = v5).pack()
F9= Radiobutton(f[5], text = "80km/L to 90km/L",font="50",value=80, variable = v5).pack()
F10= Radiobutton(f[5], text = "90km/L to 100km/L",font="50",value=90, variable = v5).pack()

l11 = Label(f[5], text ='Note*: It is mandatory to select any one of the above field.', font="50", height="5", fg="green")  
l11.pack() #l11 is the variable for label

button6 = Button(f[5], text ="Next", fg ="red",font="150", command=lambda:next(5) )
button6.pack()

l12 = Label(f[6], text = 'Select the transmission system you require in your vehicle ', font="Times 20 bold", height="5")
l12.pack(side="top") #l12 is the variable for label

#TS1, TS2 and TS3 is the variable for radiobuttons for different transmission system of the vehicle  and v6 is the variable for selected transmission system
v6=StringVar()  
TS1= Radiobutton(f[6], text = "Manual",font="50",value="Manual", variable = v6).pack()
TS2= Radiobutton(f[6], text = "Automatic",font="50",value="Automatic", variable = v6).pack()
TS3= Radiobutton(f[6], text = "Automatic & Manual",font="50",value="Automatic and Manual", variable = v6).pack()

l13 = Label(f[6], text ='Note*: It is mandatory to select any one of the above field. For two wheeler vehicle select manual option', font="20", height="5", fg="green")  
l13.pack() #l13 is the variable for label

button7 = Button(f[6], text ="Next", fg ="red",font="150", command=lambda:next(6) )
button7.pack()

l14 = Label(f[7], text = 'Select the fuel type you require in your vehicle ', font="Times 20 bold", height="5")
l14.pack(side="top") #l14 is the variable for label

v7=StringVar()#v7 is the variable for selected fuel type
FT1= Radiobutton(f[7], text = "Petrol",font="50",value="Petrol", variable = v7).pack()#FT1=fueltype1
FT2= Radiobutton(f[7], text = "Diesel",font="50",value="Diesel", variable = v7).pack()#FT2=fueltype2
FT3= Radiobutton(f[7], text = "LPG",font="50",value="LPG", variable = v7).pack()#FT3=fueltype3
FT2= Radiobutton(f[7], text = "Biofuel",font="50",value="Biofuel", variable = v7).pack()#FT4=fueltype4
FT3= Radiobutton(f[7], text = "Electric",font="50",value="Electric", variable = v7).pack()#FT5=fueltype5

l15 = Label(f[7], text ='Note*: It is mandatory to select any one of the above field. For two wheeler vehicle select manual option', font="20", height="5", fg="green")  
l15.pack()  #l15 is the variable for label

button8 = Button(f[7], text ="Next", fg ="red",font="150", command=lambda:next(7) )
button8.pack()

l16 = Label(f[8], text = 'The ideal budget you have envisioned for buying a new vehicle amounts to? ', font="Times 20 bold", height="5")
l16.pack(side="top")  #l16 is the variable for label

#Below s1,s2,s3,s4,s5,s6,s7,s8,s9,s10 are variables for radiobutton for the budget and v8 is the variable for selected budget of the vehicle
v8=IntVar() 
s1= Radiobutton(f[8], text = "Upto 1 lakh",font="50",value=100000, variable = v8).pack(side=TOP) 
s2= Radiobutton(f[8], text = "upto 2 Lakh",font="50",value=200000, variable = v8).pack(side=TOP)
s3= Radiobutton(f[8], text = "Upto 3 Lakh",font="50",value=300000, variable = v8).pack(side=TOP)
s4= Radiobutton(f[8], text = "Upto 4 Lakh",font="50",value=400000, variable = v8).pack(side=TOP)
s5= Radiobutton(f[8], text = "Upto 5 Lakh",font="50",value=500000, variable = v8).pack(side=TOP)
s6= Radiobutton(f[8], text = "Upto 6 Lakh",font="50",value=600000, variable = v8).pack(side=TOP)
s7= Radiobutton(f[8], text = "Upto 7 Lakh",font="50",value=700000, variable = v8).pack(side=TOP)
s8= Radiobutton(f[8], text = "Upto 8 Lakh",font="50",value=800000, variable = v8).pack(side=TOP)
s9= Radiobutton(f[8], text = "Upto 9 Lakh",font="50",value=900000, variable = v8).pack(side=TOP)
s10= Radiobutton(f[8], text = "Upto 10 Lakh",font="50",value=1000000, variable = v8).pack(side=TOP)

l17 = Label(f[8], text ='Note*: It is mandatory to select any one of the above field.', font="20", height="5", fg="green")  
l17.pack() #l17 is the variable for label

button9 = Button(f[8], text ="Next", fg ="red",font="150", command=lambda:submit(8) )
button9.pack()


root.mainloop()


# In[2]:


from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="******",
  database="k19ky"
)
mycursor = mydb.cursor()
sql = "INSERT INTO vehicles(Name, wheels, Space, Look, Seats, FuelEfficiency, TransmissionSystem, HorsePower, FuelType, Price, yearofRelease) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val =[
    ("Activa 6G", 2, 7, 8, 2, 62, "Manual", 70, "Petrol", 67800, 2019 ),
    ("Wagon R", 4, 8, 6, 5, 22, "Manual", 85, "Petrol", 600000, 2019 ),
    ("Hyundai Elite i20", 4, 8, 8, 5, 23, "Manual", 95, "Diesel", 761000, 2019 ),
    ("Hyundai Grand i10 NIOS", 4, 8, 9, 5, 21, "Manual", 110, "Petrol", 768000, 2019),
    ("TVS Jupiter Grande", 2, 7, 7, 2, 61, "Manual", 80, "Petrol", 61000,2019)
    
]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount, "record(s) inserted")




# In[ ]:


from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="*****",
  database="k19ky"
)
mycursor = mydb.cursor()


# In[ ]:




