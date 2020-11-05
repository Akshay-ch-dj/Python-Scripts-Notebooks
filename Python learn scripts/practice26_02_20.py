from tkinter import *
tr_p = Tk()

tr_p.geometry("600x380")
#Label: Enter username
lab_username = Label(tr_p, text="Enter Username").place(x=300,y=150)
#Label: Enter Password
lab_password = Label(tr_p, text="Enter Password").place(x=300,y=175)
#Entry: Username
Ent_username = Entry(tr_p).place(x=400,y=150)
#Entry: password
Ent_passwrd = Entry(tr_p, show="*").place(x=400,y=175)
#Button: Login
butt_login = Button(tr_p, text = "Login").place(x=484,y=200)

tr_p.mainloop()
