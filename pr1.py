
import tkinter as tk
#import PIL
#from PIL import Image, ImageTk
from tkinter import messagebox
# import mysql.connector as my
import sys
import calendar


w1=tk.Tk()
w1.geometry('1366x720')
w1.title("Login Page")

# Variables to store entered values on login page
uservalue=tk.StringVar()
passwordvalue=tk.StringVar()




# Function to be called if Login btn is clicked

counter=0

def login():
    
    # connection
    import mysql.connector as con
    connection = con.connect(host="localhost", user="root", password="thegreat1", database="irctc")

    cursor = connection.cursor()


    if uservalue.get() == "" or passwordvalue.get() == "":
        messagebox.showerror("Error", "All fields are required", parent=w1)
        sys.exit()




    #         calculating number of rows in the database
    cursor.execute("select count(*) from data")
    afetch=cursor.fetchone()
    bfetch=afetch[0]  #It has the number of rows

    username = uservalue.get()
    password = passwordvalue.get()

#     Checking if username and password are correct and match
    cursor.execute('select username,password from data where username=username and password=password')
    row=cursor.fetchall()

    global counter

    # as declared currently counter=0

    for i in range(0,bfetch):
        if(row[i][0]==username and row[i][1]==password):
            counter=1
    if(counter==1):
        messagebox.showinfo("Found","logging in")
        messagebox.showinfo("Hello", "Please close this window to continue")
        # print("found")
        

    else:
        messagebox.showinfo("Not found","password and uservalue  does not match")

    connection.close()

# Variables for storing entered sign up data
user2value=tk.StringVar()
pass2value=tk.StringVar()
emailvalue=tk.StringVar()
confpassvalue=tk.StringVar()
    # function  to be called if Register button clicked

# If Register btn is clicked

def register():
    if (user2value.get()==""or emailvalue.get()==""or pass2value.get()==""or confpassvalue.get()==""):
         # phonevalue is left
        messagebox.showerror("Error","All Fields Are Required",parent=w1)

    elif pass2value.get()!=confpassvalue.get():
        messagebox.showerror("Error","Password and Confirm Password Should Be Same",parent=w1)
    else:
        printuser=user2value.get()
        printemail=emailvalue.get()
        printpass=pass2value.get()
        # printphone=phonevalue.get()


    # connection
    import mysql.connector as con
    connection = con.connect(host="localhost", user="root", password="thegreat1", database="irctc")

    cursor = connection.cursor()


    '''cursor.execute("INSERT INTO data VALUES(%s,%s,%s)",(printuser,printpass,printemail))
    messagebox.showinfo("Success","Signed Up")
    print(printuser,printpass,printemail)'''

#     trial
    cursor.execute("INSERT INTO data (username,password,email) VALUES (%s, %s , %s)", (printuser, printpass, printemail))
    connection.commit()


    # connnection.commit()

    connection.close()

    messagebox.showinfo("Success", "Register Succesful"

                        , parent=w1)
    messagebox.showinfo("Hello","Please Login to continue" )

        


def Register():
    f = tk.PhotoImage(file='back.png')
    background_label = tk.Label(w1, image=f)
    background_label.place(x=1000, y=1500, relwidth=1, relheight=1)
    frame_input2 = tk.Frame(w1, bg='#6b4f83')

    frame_input2.place(x=320, y=130, height=500, width=630)

    label1 = tk.Label(frame_input2, text="Register Here", font=('impact', 28, 'bold'),

                   fg="blue", bg='white',borderwidth=5, relief=tk.RIDGE)

    label1.place(x=45, y=20)



    # username
    user2 = tk.Label(frame_input2, text="Username", font=("Goudy old style", 20, "bold"),

                   fg='orangered', bg='white')

    user2.place(x=30, y=95)

    uentry2= tk.Entry(frame_input2, font=("times new roman", 15, "bold"),

                       bg='lightgray' ,textvariable=user2value,borderwidth=3, relief=tk.SUNKEN)

    uentry2.place(x=30, y=145, width=270, height=35)
    a1=uservalue.get()
    # Password
    pass2 = tk.Label(frame_input2, text="Password", font=("Goudy old style", 20, "bold"),

                   fg='orangered', bg='white')

    pass2.place(x=30, y=195)

    passentry2 = tk.Entry(frame_input2, font=("times new roman", 15, "bold"),

                        bg='lightgray',textvariable=pass2value,borderwidth=3, relief=tk.SUNKEN)

    passentry2.place(x=30, y=245, width=270, height=35)
    b1=pass2value.get()
    # email
    email= tk.Label(frame_input2, text="Email-id", font=("Goudy old style", 20, "bold"),

                   fg='orangered', bg='white')

    email.place(x=330, y=95)

    emailentry = tk.Entry(frame_input2, font=("times new roman", 15, "bold"),

                        bg='lightgray',textvariable=emailvalue,borderwidth=3, relief=tk.SUNKEN)


    emailentry.place(x=330, y=145, width=270, height=35)
    c1=emailvalue.get()
    # confirm password
    confpass= tk.Label(frame_input2, text="Confirm Password",

                   font=("Goudy old style", 20, "bold"), fg='orangered', bg='white')

    confpass.place(x=330, y=195)

    confpassentry = tk.Entry(frame_input2, font=("times new roman", 15, "bold"),

                        bg='lightgray',textvariable=confpassvalue,borderwidth=3, relief=tk.SUNKEN)
    d1=confpassvalue.get()
    confpassentry.place(x=330, y=245, width=270, height=35)
   
    # sign up btn
    sig = tk.Button(frame_input2, command=register, text="Register"

                    , cursor="hand2", font=("times new roman", 15), fg="white",

                    bg="orangered", bd=0, width=15, height=1,borderwidth=3, relief=tk.RIDGE)

    sig.place(x=50, y=340)
    
    # If already Registered

    rego=tk.Button(frame_input2,command=main, text="Already Registered? Login"

                    , cursor="hand2", font=("times new roman", 15), fg="white",

                    bg="orangered", bd=0, width=30, height=1,borderwidth=3, relief=tk.RIDGE)
    rego.place(x=270,y=340)
    w1.mainloop()

    
    
    

def main(): #This method is responsible for the main login page

# Photo goes here

    f=tk.PhotoImage(file='back.png')
    background_label=tk.Label(w1,image=f)
    background_label.place(x=0,y=0,relwidth=1,relheight=1)

# Photo Ends here

# Creating frame

    frame_input=tk.Frame(w1,bg='#6b4f83')
    frame_input.place(x=320,y=130,height=500,width=400)

#LABELLING AND PACKING

    x=tk.Label(w1,text="IRCTC LOGIN", font=("SF PRO DISPLAY", 30) , fg='Blue',borderwidth=4, relief=tk.RIDGE)

    user=tk.Label(w1,text="Username",font=("Century Gothic",25,"bold"),  fg='orangered',borderwidth=3, relief=tk.SUNKEN)


    password=tk.Label(w1,text="Password", font=("Century Gothic",25,'bold'),fg='orangered',borderwidth=3, relief=tk.SUNKEN)
    x.place(x=400,y=150)
    user.place(x=340,y=230)
    password.place(x=340,y=340)

# using login variables as global
    global uservalue
    global passwordvalue

    userentry=tk.Entry(w1,font=("times new roman",22,"bold"),fg='blue',bg='lightgray',textvariable=uservalue,borderwidth=2,relief=tk.SUNKEN)
    userentry.place(x=340,y=280)

    passwordentry=tk.Entry(w1,font=("times new roman",22,"bold"),fg='blue',bg='lightgray',textvariable=passwordvalue,borderwidth=2,relief=tk.SUNKEN)
    passwordentry.place(x=340,y=390)


    # login button
    btn1=tk.Button(frame_input,text="Login",command=login,

                  font=("times new roman",15),fg="white",bg="orangered",

                  bd=0,width=15,height=1,borderwidth=3, relief=tk.RIDGE)

    btn1.place(x=90,y=340)

# signup button

    btn2=tk.Button(frame_input,command=Register,text="Not Registered? Register",

                font=("calibri",15),bg='orange',fg="white",bd=0,borderwidth=3, relief=tk.RIDGE)

    btn2.place(x=70,y=390)


    w1.mainloop()






main()








# Project2


# import project1 as k
import tkinter as tk
import PIL
from PIL import Image,ImageTk
import random
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
import sys
# Variables to store which class is selected
gen,sleep,a1,a2=0,0,0,0
# if booking successful
def final():
    global number_of_passengers
    # print(number_of_passengers)
    global name1
    global age1
    global pnrvalue1
    global name2
    global pnrvalue2
    print(name1.get())
    global gen
    global sleep
    global a1
    global a2
        
    tk.Frame(w2,bg="#49577b").place(x=0, y=0, height=720, width=1366)
    tk.Label(text="BOOKING SUCCESSFUL",fg="GREEN",font=("algerian 30"),borderwidth=3, relief=tk.SUNKEN).place(x=500,y=100)

    

    if number_of_passengers==1:
        tk.Label(text="Passenger :",font=("CENTURY GOTHIC",20,"bold"),fg="orangered",
        borderwidth=3, relief=tk.SUNKEN).place(x=100,y=300)

        tk.Label(text=name1.get(),font=("CENTURY GOTHIC",20,"bold"),fg="orangered",
        borderwidth=3, relief=tk.SUNKEN).place(x=400,y=300)

        tk.Label(text="pnr :",font=("CENTURY GOTHIC",20,"bold"),fg="orangered",
        borderwidth=3, relief=tk.SUNKEN).place(x=100,y=450)

        tk.Label(text=pnrvalue1,font=("CENTURY GOTHIC",20,"bold"),fg="orangered",
        borderwidth=3, relief=tk.SUNKEN).place(x=400,y=450)
        if(gen==1):
            tk.Label(text="YOUR BOOKING IS IN GENERAL",
            font=("CENTURY GOTHIC",20,"bold"),fg="orangered").place(x=200,y=600)
        elif(sleep==1):
            tk.Label(text="YOUR BOOKING IS IN SLEEPER ",
            font=("CENTURY GOTHIC",20,"bold"),fg="orangered").place(x=200,y=600)
        elif(a1==1):
            tk.Label(text="YOUR BOOKING IS IN AC 3rd TIER ",
            font=("CENTURY GOTHIC",20,"bold"),fg="orangered").place(x=200,y=600)
        elif(a2==1):
            tk.Label(text="YOUR BOOKING IS IN AC 2nd TIER",
            font=("CENTURY GOTHIC",20,"bold"),fg="orangered").place(x=200,y=600)
        

    elif(number_of_passengers==2):
        tk.Label(text="Passenger 1 :",font=("CENTURY GOTHIC",20,"bold"), fg="orangered",
        borderwidth=3, relief=tk.SUNKEN).place(x=100,y=200)

        tk.Label(text=name1.get(),font=("CENTURY GOTHIC",20,"bold"),fg="orangered"
        ,borderwidth=3, relief=tk.SUNKEN).place(x=400,y=200)

        tk.Label(text="pnr 1:",font=("CENTURY GOTHIC",20,"bold"),fg="orangered",
        borderwidth=3, relief=tk.SUNKEN).place(x=100,y=250)

        tk.Label(text=pnrvalue1,font=("CENTURY GOTHIC",20,"bold"),fg="orangered",
        borderwidth=3, relief=tk.SUNKEN).place(x=400,y=250)

        tk.Label(text="Passenger 2:",font=("CENTURY GOTHIC",20,"bold"),fg="orangered",
        borderwidth=3, relief=tk.SUNKEN).place(x=100,y=400)

        tk.Label(text=name2.get(),font=("CENTURY GOTHIC",20,"bold"),fg="orangered",
        borderwidth=3, relief=tk.SUNKEN).place(x=400,y=400)

        tk.Label(text="pnr 2:",font=("CENTURY GOTHIC",20,"bold"),fg="orangered",
        borderwidth=3, relief=tk.SUNKEN).place(x=100,y=500)

        tk.Label(text=pnrvalue1,font=("CENTURY GOTHIC",20,"bold"),fg="orangered",
        borderwidth=3, relief=tk.SUNKEN).place(x=400,y=500)

        if(gen==1):
            tk.Label(text="YOUR BOOKING IS IN GENERAL",
            font=("CENTURY GOTHIC",20,"bold"),fg="orangered").place(x=200,y=560)
        elif(sleep==1):
            tk.Label(text="YOUR BOOKING IS IN SLEEPER ",
            font=("CENTURY GOTHIC",20,"bold"),fg="orangered").place(x=200,y=560)
        elif(a1==1):
            tk.Label(text="YOUR BOOKING IS IN AC 3rd TIER ",
            font=("CENTURY GOTHIC",20,"bold"),fg="orangered").place(x=200,y=560)
        elif(a2==1):
            tk.Label(text="YOUR BOOKING IS IN AC 2nd TIER",
            font=("CENTURY GOTHIC",20,"bold"),fg="orangered").place(x=200,y=560)
    tk.Label(text="Your Booking is on:",font=("CENTURY GOTHIC",20,"bold"),fg="orangered").place(x=200,y=650)
    tk.Label(text=str1,font=("CENTURY GOTHIC",20,"bold"),fg="orangered").place(x=450,y=650)


pnr=0
pnrvalue1,pnrvalue2='',''
number_of_passengers=0
# if book btn clicked
def booked():

     # if entry boxes are empty show error
   
    '''if(name1.get()=='' or age1.get()=='' or aadhar1.get()==''):
        messagebox.showerror("Error","All fields are Required")
        sys.exit()

    elif(name1.get()=='' or age1.get()=='' or aadhar1.get()=='' or name2.get()=='' or age2.get()=='' or aadhar2.get()==''):
        messagebox.showerror("Error","All fields are Required")
        sys.exit()'''

    
    global number_of_passengers
    m=aadhar1.get()
    n=aadhar2.get()
    if m!='' and n!='':
        number_of_passengers=2
    elif m=='' and n!='':
        number_of_passengers=1
    elif m!='' and n=='':
        number_of_passengers=1
    else:
        number_of_passengers=0

    print(number_of_passengers)



    global pnr
    global pnrvalue1
    global pnrvalue2
    
    '''if number_of_passengers==3:
        pnr=3'''
    if number_of_passengers==2:
        pnr=2
    elif number_of_passengers==1:
        pnr=1
    else:
        pnr=0
    '''if(pnr==3):
        
        pnrvalue1="D"+str(random.randint(1,9))+str(random.randint(0,9))+str(random.randint(1,9))+str(random.randint(1,9))+str(random.randint(1,9))
        
        pnrvalue2='H'+str(random.randint(1,9))+str(random.randint(1,9))+"R"+str(random.randint(1,9))+str(random.randint(1,9))
        pnrvalue3=str(random.randint(1,9))+"G"+str(random.randint(1,9))+str(random.randint(1,9))+str(random.randint(1,9))+str(random.randint(1,9))'''
    if(pnr==2):
        pnrvalue1="D"+str(random.randint(1,9))+str(random.randint(0,9))+str(random.randint(1,9))+str(random.randint(1,9))+str(random.randint(1,9))
        
        pnrvalue2='H'+str(random.randint(1,9))+str(random.randint(1,9))+"R"+str(random.randint(1,9))+str(random.randint(1,9))
    elif(pnr==1):
        pnrvalue1="D"+str(random.randint(1,9))+str(random.randint(0,9))+str(random.randint(1,9))+str(random.randint(1,9))+str(random.randint(1,9))
        
    print(pnrvalue1)
    print(pnrvalue2)
    
    n1=name1.get()
    n2=name2.get()
    a1=age1.get()
    a2=age2.get()
    if number_of_passengers==2:
        import mysql.connector as my
        con=my.connect(host="localhost",user='root',password='thegreat1',db='irctc')
        cursor=con.cursor()
        
        cursor.execute("INSERT INTO passenger values(%s,%s,%s,%s)",(n1,m,a1,pnrvalue1))
        cursor.execute("INSERT INTO passenger values(%s,%s,%s,%s)",(n2,n,a2,pnrvalue2))
        con.commit()

        final()
        # print('here')
    elif number_of_passengers==1:
        import mysql.connector as my
        con=my.connect(host="localhost",user='root',password='thegreat1',db='irctc')
        cursor=con.cursor()
        
        cursor.execute("INSERT INTO passenger values(%s,%s,%s,%s)",(n1,m,a1,pnrvalue1))
        
        con.commit()

        final()
# If user wants to add more details
def detail2():
    background_label.place(x=1000, y=1500, relwidth=1, relheight=1)
    frame_input2 = tk.Frame(w2, bg='#4a7491')

    frame_input2.place(x=30, y=15, height=690, width=1300)

    label1 = tk.Label(frame_input2, text="ENTER THE DETAILS", font=('impact', 32, 'bold'),

                   fg="blue", bg='white',borderwidth=3, relief=tk.SUNKEN)

    label1.place(x=400, y=90)


    global name1
    global aadhar1
    global age1
    global name2
    global age2
    global aadhar2

#    first name
    tk.Label(frame_input2, text="NAME", font=("Goudy old style", 20, "bold"),

                   fg='orangered', bg='lightgray',borderwidth=3, relief=tk.SUNKEN).place(x=50,y=250)

    tk.Entry(frame_input2, font=("times new roman", 15, "bold"),

                       bg='lightgray' ,textvariable=name1,borderwidth=3, relief=tk.SUNKEN).place(x=250,y=250)

    # second name

    tk.Label(frame_input2, text="NAME", font=("Goudy old style", 20, "bold"),

                   fg='orangered', bg='LIGHTGRAY',borderwidth=3, relief=tk.SUNKEN).place(x=700,y=250)

    tk.Entry(frame_input2, font=("times new roman", 15, "bold"),

                       bg='lightgray' ,textvariable=name2,borderwidth=3, relief=tk.SUNKEN).place(x=1000,y=250)
    
    # first age
    tk.Label(frame_input2, text="AGE", font=("Goudy old style", 20, "bold"),

                   fg='orangered', bg='lightgray',borderwidth=3, relief=tk.SUNKEN).place(x=50,y=350)

   

    tk.Entry(frame_input2, font=("times new roman", 15, "bold"),

                        bg='lightgray',textvariable=age1,borderwidth=3, relief=tk.SUNKEN).place(x=250,y=350)

    # second age

    tk.Label(frame_input2, text="AGE", font=("Goudy old style", 20, "bold"),

                   fg='orangered', bg='lightgray',borderwidth=3, relief=tk.SUNKEN).place(x=700,y=350)

   

    tk.Entry(frame_input2, font=("times new roman", 15, "bold"),

                        bg='lightgray',textvariable=age2,borderwidth=3, relief=tk.SUNKEN).place(x=1000,y=350)


    # aadhar1
    tk.Label(frame_input2, text="AADHAR NO.", font=("Goudy old style", 20, "bold"),

                   fg='orangered', bg='lightgray',borderwidth=3, relief=tk.SUNKEN).place(x=50,y=450)

   

    tk.Entry(frame_input2, font=("times new roman", 15, "bold"),

                        bg='lightgray',textvariable=aadhar1,borderwidth=3, relief=tk.SUNKEN).place(x=250,y=450)
    

    # aadhar2
    tk.Label(frame_input2, text="AADHAR NO.", font=("Goudy old style", 20, "bold"),

                   fg='orangered', bg='lightgray',borderwidth=3, relief=tk.SUNKEN).place(x=700,y=450)

   

    tk.Entry(frame_input2, font=("times new roman", 15, "bold"),

                        bg='lightgray',textvariable=aadhar2,borderwidth=3, relief=tk.SUNKEN).place(x=1000,y=450)
    
   
    # sign up btn
    sig = tk.Button(frame_input2, command=booked, text="BOOK"

                    , cursor="hand2", font=("times new roman", 19), fg="white",

                    bg="orangered", bd=0, width=15, height=1,borderwidth=3, relief=tk.RIDGE)

    sig.place(x=400, y=600)
    
    
    
    w2.mainloop()
    

# If any coach is selected for passenger details to be entered

def detail1():
    #LABELLING AND PACKING

    tk.Label(w2,text="PASSENGER DETAILS", font=("SF PRO DISPLAY", 30) , fg='Blue',borderwidth=4, relief=tk.RIDGE).place(x=500,y=50)

    tk.Label(w2,text="NAME",font=("Century Gothic",25,"bold"),  fg='orangered',borderwidth=3, relief=tk.SUNKEN).place(x=200,y=200)


    tk.Label(w2,text="AGE", font=("Century Gothic",25,'bold'),fg='orangered',borderwidth=3, relief=tk.SUNKEN).place(x=200,y=300)

    tk.Label(w2,text="AADHAR NUMBER", font=("Century Gothic",25,'bold'),fg='orangered',borderwidth=3, relief=tk.SUNKEN).place(x=135,y=400)


# using login variables as global
    global name1
    global age1
    global aadhar1

    tk.Entry(w2,font=("times new roman",22,"bold"),fg='blue',bg='lightgray',textvariable=name1,borderwidth=2,relief=tk.SUNKEN).place(x=450,y=200)
   
    tk.Entry(w2,font=("times new roman",22,"bold"),fg='blue',bg='lightgray',textvariable=age1,borderwidth=2,relief=tk.SUNKEN).place(x=450,y=300)
    

    tk.Entry(w2,font=("times new roman",22,"bold"),fg='blue',bg='lightgray',textvariable=aadhar1,borderwidth=2,relief=tk.SUNKEN).place(x=450,y=400)

    checkbtn=tk.IntVar()

    tk.Checkbutton(w2, text = "DO YOU AGREE TO THE T&C ?",
                      variable = checkbtn,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,bg="light blue",fg='orangered'
                      ).place(x=350,y=610)
    # login button
    btn1=tk.Button(text="BOOK YOUR TICKET",command=booked,

                  font=("times new roman",15),fg="white",bg="orangered",

                  bd=0,width=22,height=1,borderwidth=3, relief=tk.RIDGE)

    btn1.place(x=250,y=550)

# signup button

    btn2=tk.Button(command=detail2,text="MORE PASSANGERS?",

                font=("calibri",15),bg='orange',fg="white",bd=0,borderwidth=3, relief=tk.RIDGE)

    btn2.place(x=560,y=550)

            
        

  
    # print(checkbtn.get())
    
    w2.mainloop()




# functions if different coaches are selected
def general():
    background_label.place(x=1000, y=1500, relwidth=1, relheight=1)
    frame_input2 = tk.Frame(w2, bg='#4a7491')

    frame_input2.place(x=30, y=15, height=690, width=1300)
    global gen
    gen=1
    detail1()

    


def sleeper():
    background_label.place(x=1000, y=1500, relwidth=1, relheight=1)
    frame_input2 = tk.Frame(w2, bg='#4a7491')

    frame_input2.place(x=30, y=15, height=690, width=1300)
    global sleep
    sleep=1
    detail1()

def ac1():
    background_label.place(x=1000, y=1500, relwidth=1, relheight=1)
    frame_input2 = tk.Frame(w2, bg='#4a7491')

    frame_input2.place(x=30, y=15, height=690, width=1300)
    global a1
    a1=1
    #for ac3rd
    detail1()

def ac2():
    background_label.place(x=1000, y=1500, relwidth=1, relheight=1)
    frame_input2 = tk.Frame(w2, bg='#4a7491')

    frame_input2.place(x=30, y=15, height=690, width=1300)
    global a2
    a2=1
    #for ac2nd
    detail1()







# variables storing train names and distance
t1,t2,t3,distance='','','',''
def train():
    source=fromvalue.get()
    destination=tovalue.get()
    source=source.upper()
    destination=destination.upper()
    import mysql.connector as connection
    con=connection.connect(host="localhost",user="root",password="thegreat1",db="irctc")
    cursor=con.cursor()
    cursor.execute("select count(*) from detail")
    afetch=cursor.fetchone()
    bfetch=afetch[0]  #It has the number of rows

    c=0
    global distance
    global t1
    global t2
    global t3
    
#     Checking if source and destination  match the database
    cursor.execute('select * from detail where source=source AND destination=destination')
    row=cursor.fetchall()
    # print(row[1])
# global counter

    # as declared currently counter=0

    for i in range(0,bfetch):
        if(row[i][0]==source and row[i][1]==destination):
                c=1
                distance=row[i][2]
                t1=row[i][3]
                t2=row[i][4]
                t3=row[i][5]


    if(c==1):
       
        print(distance,t1,t2,t3)
    


    # DISPLAYING AVAILABLE TRAINS WITH COST

    if ( fromvalue.get() == "" or tovalue.get() == "" ):
        messagebox.showerror("Error", "All Fields Are Required", parent=w2)

    else:
        f = tk.PhotoImage(file='train.png')
        background_label = tk.Label(w2, image=f)
        background_label.place(x=1000, y=1500, relwidth=1, relheight=1)
        frame_input2 = tk.Frame(w2, bg='#6e6394')

        frame_input2.place(x=183, y=75, height=590, width=960)

        tk.Label(text="Select Your Train And Class",font=("ALGERIAN",26),bg="#2a365c",fg="WHITE",borderwidth=3, relief=tk.SUNKEN).place(x=420,y=100)

        tk.Label(text="Available Trains",font=("Century Gothic",24),bg="#2a365c",fg="white",borderwidth=3, relief=tk.SUNKEN).place(x=210,y=180)
        #train label 1

        tlabel1=tk.Label(text=t1,font=("Century Gothic",18),bg='#2a365c',fg="white",borderwidth=3, relief=tk.SUNKEN).place(x=230,y=260)
        tlabel2=tk.Label(text=t2,font=("CENTURY GOTHIC",18),bg='#2a365c',fg="white",borderwidth=3, relief=tk.SUNKEN).place(x=530,y=260)
        tlabel3=tk.Label(text=t3,font=("CENTURY GOTHIC",18),bg='#2a365c',fg="white",borderwidth=3, relief=tk.SUNKEN).place(x=850,y=260)

        d=int(distance)
        # Labelling coaches and their costs

        t1ag="GENERAL : "+str(random.randint(10,1000))+"\nCOST: "+str(d*1.5)
        t2ag="GENERAL : "+str(random.randint(10,1000))+"\nCOST: "+str(d*1.5)
        t3ag="GENERAL : "+str(random.randint(10,1000))+"\nCOST: "+str(d*1.5)
        
        t1as="SLEEPER : "+str(random.randint(10,700))+"\nCOST: "+str(d*2)
        t2as="SLEEPER : "+str(random.randint(10,700))+"\nCOST: "+str(d*2)
        t3as="SLEEPER : "+str(random.randint(10,700))+"\nCOST: "+str(d*2)

        t1aa1="AC 3 : "+str(random.randint(10,200))+"\nCOST: "+str(d*3)
        t2aa1="AC 3 : "+str(random.randint(10,200))+"\nCOST: "+str(d*3)
        t3aa1="AC 3 : "+str(random.randint(10,200))+"\nCOST: "+str(d*3)

        t1aa2="AC 2 : "+str(random.randint(10,150))+"\nCOST: "+str(d*3.5)
        t2aa2="AC 2 : "+str(random.randint(10,150))+"\nCOST: "+str(d*3.5)
        t3aa2="AC 2 : "+str(random.randint(10,150))+"\nCOST: "+str(d*3.5)  


        
        b1t1=tk.Button(text=t1ag,font=("Century Gothic bold",10),
        bg='#4a7491',fg="#eb3305",width=20,command=general,borderwidth=3, relief=tk.RIDGE).place(x=240,y=310)

        b2t1=tk.Button(text=t1as,font=("Century Gothic bold",10),bg='#4a7491',
        fg="#eb3305",width=20,command=sleeper,borderwidth=3, relief=tk.RIDGE).place(x=240,y=360)

        b3t1=tk.Button(text=t1aa1,font=("Century Gothic bold",10),
        bg='#4a7491',fg="#eb3305",width=20,command=ac1,borderwidth=3, relief=tk.RIDGE).place(x=240,y=410)

        b4t1=tk.Button(text=t1aa2,font=("Century Gothic bold",10)
        ,bg='#4a7491',fg="#eb3305",width=20,command=ac2,borderwidth=3, relief=tk.RIDGE).place(x=240,y=460)

        b1t2=tk.Button(text=t2ag,font=("Century Gothic bold",10),
        bg='#4a7491',fg="#eb3305",width=20,command=general,borderwidth=3, relief=tk.RIDGE).place(x=550,y=310)

        b2t2=tk.Button(text=t2as,font=("Century Gothic bold",10),
        bg='#4a7491',fg="#eb3305",width=20,command=sleeper,borderwidth=3, relief=tk.RIDGE).place(x=550,y=360)

        b3t2=tk.Button(text=t2aa1,font=("Century Gothic bold",10),
        bg='#4a7491',fg="#eb3305",width=20,command=ac1,borderwidth=3, relief=tk.RIDGE).place(x=550,y=410)

        b4t2=tk.Button(text=t2aa2,font=("Century Gothic bold",10),
        bg='#4a7491',fg="#eb3305",width=20,command=ac2,borderwidth=3, relief=tk.RIDGE).place(x=550,y=460)

        b1t3=tk.Button(text=t3ag,font=("Century Gothic bold",10),
        bg='#4a7491',fg="#eb3305",width=20,command=general,borderwidth=3, relief=tk.RIDGE).place(x=910,y=310)

        b2t3=tk.Button(text=t3as,font=("Century Gothic bold",10),
        bg='#4a7491',fg="#eb3305",width=20,command=sleeper,borderwidth=3, relief=tk.RIDGE).place(x=910,y=360)

        b3t3=tk.Button(text=t3aa1,font=("Century Gothic bold",10),
        bg='#4a7491',fg="#eb3305",width=20,command=ac1,borderwidth=3, relief=tk.RIDGE).place(x=910,y=410)

        b4t3=tk.Button(text=t3aa2,font=("Century Gothic bold",10),
        bg='#4a7491',fg="#eb3305",width=20,command=ac2,borderwidth=3, relief=tk.RIDGE).place(x=910,y=460)




if(counter==1):
    w2=tk.Tk()
    w2.geometry('1366x720')
    w2.title("Select train and date")
    f=tk.PhotoImage(file='train.png')
    background_label=tk.Label(w2,image=f)
    background_label.place(x=0,y=0,relwidth=1,relheight=1)

    name1=tk.StringVar()
    age1=tk.StringVar()
    aadhar1=tk.StringVar()
    name2=tk.StringVar()
    age2=tk.StringVar()
    aadhar2=tk.StringVar()

        










    frame=tk.Frame(w2,bg='#6e6394')
    frame.place(x=220,y=130,height=500,width=880)

    datevalue=tk.StringVar()
    fromvalue=tk.StringVar()
    tovalue=tk.StringVar()

    datelabel=tk.Label(w2,text="Enter Date of Travel",font=("Goudy old style", 20, "bold"),bg="lightgray", fg='orangered',borderwidth=3, relief=tk.SUNKEN).place(x=350,y=170)
    fromlabel=tk.Label(w2,text="FROM",font=("Goudy old style", 20, "bold"), fg='orangered',bg="lightgray", relief=tk.SUNKEN).place(x=350,y=320)
    tolabel=tk.Label(w2,text="TO",font=("Goudy old style", 20, "bold"), fg='orangered',bg="lightgray",borderwidth=3, relief=tk.SUNKEN).place(x=350,y=420)

    # dateentry=tk.Entry(w2,font=("century gothic",20),textvariable=datevalue).place(x=700,y=170)
    fromentry=tk.Entry(w2,font=("century gothic",20),bg="lightgray",textvariable=fromvalue,borderwidth=3, relief=tk.SUNKEN).place(x=700,y=320)
    toentry=tk.Entry(w2,font=("century gothic",20),bg="lightgray",textvariable=tovalue,borderwidth=3, relief=tk.SUNKEN).place(x=700,y=420)

    btn=tk.Button(text="Search Trains",command=train,font=("GOUDY OLD STYLE",14,"bold"),borderwidth=3,fg='white',bg='orangered', relief=tk.SUNKEN).place(x=500,y=520)
    
    def getdate():
        # print(cal.get_date())
        y=cal.get_date()
        global str1
        str1=y.strftime("%d-%B-%y")

        print(str1)

    cal = DateEntry(w2, width= 10,font=("century gothic",20), background= "magenta3",
     foreground= "white",bd=5,borderwidth=3, relief=tk.SUNKEN)

    cal.place(x=700,y=170)
    

    btnc=tk.Button(w2,text="OK",font=("ALGERIAN",15),command=getdate,background="#3cc0c3",borderwidth=3, relief=tk.SUNKEN)
    btnc.place(x=760,y=220)
    w2.mainloop()