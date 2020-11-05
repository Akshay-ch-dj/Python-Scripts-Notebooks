from tkinter import *

from tkinter import messagebox
my_window = Tk()



#MY WINDOW TILTLE = MY PROJECT
my_window.title("MY PROJECT")

def LOGIN_INFO():
    messegebox.showinfo("ThankYou")

#Adding image
'''
my_photo = PhotoImage(file = "my_tkinder.jpg")
Label(my_window,image=my_photo,bg="black").grid(row=0,column=0,sticky=E)
'''
my_window.geometry("600x380")
#Label: Enter username
lab_username = Label(my_window, text="Enter Username").place(x=300,y=150)
#Label: Enter Password
lab_password = Label(my_window, text="Enter Password").place(x=300,y=175)
#Entry: Username
Ent_username = Entry(my_window).place(x=400,y=150)
#Entry: password
Ent_passwrd = Entry(my_window, show="*").place(x=400,y=175)
#Button: Login
butt_login = Button(my_window, text = "Login", command="LOGIN_INFO").place(x=484,y=200)

my_window.mainloop()
