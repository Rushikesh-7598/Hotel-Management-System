import sqlite3
from sre_parse import State
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import random

import main

room_number_taken = []


class CheckIN:

    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.title("CHECK IN")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))

        self.bg = PhotoImage(file = "sea.png")
  
        # Show image using label
        label1 = Label( root, image = self.bg)
        label1.place(x = 0, y = 0)

        self.top = LabelFrame(self.root)
        self.top.pack(side="top")

        self.bottom = Frame(self.root)
        self.bottom.pack(side="top")

        self.checkbox = Frame(self.root)
        self.checkbox.pack(side="top")
        
        self.checkbox1 = Frame(self.root)
        self.checkbox1.pack(side="top")

        # display message
        self.label = Label(self.top,text="CHECK IN",relief=RAISED,borderwidth=10,height=3,width=30,bg='BLACK',fg='orange',font='algerian 20 bold')
        self.label.grid(row=0, column=3)

        # name label
        self.name_label = Label(self.bottom, font=('arial', 20, 'bold'), text="ENTER YOUR NAME :", fg="#0000FF",
                                anchor="w")
        self.name_label.grid(row=0, column=2, padx=10, pady=10)

        self.name_var = StringVar()
        # text enter field
        self.name_entry = Entry(self.bottom, width=50, textvar=self.name_var)
        self.name_entry.grid(row=0, column=3, padx=10, pady=10)

        # address label
        self.address_label = Label(self.bottom, font=('arial', 20, 'bold'), text="ENTER YOUR ADDRESS :", fg="#0000FF",
                                   anchor="w")
        self.address_label.grid(row=1, column=2, padx=10, pady=10)

        # text enter field
        self.address_var = StringVar()
        self.address_entry = Entry(self.bottom, width=50, textvar=self.address_var)
        self.address_entry.grid(row=1, column=3, padx=10, pady=10)

        # mobile label

        self.mobile_label = Label(self.bottom, font=('arial', 20, 'bold'), text="ENTER YOUR MOBILE NUMBER :",
                                  fg="#0000FF",
                                  anchor="w")
        self.mobile_label.grid(row=2, column=2, padx=10, pady=10)

        # text enter field
        self.mobile_var = IntVar()
        self.mobile_entry = Entry(self.bottom, width=50, text=self.mobile_var)
        self.mobile_entry.grid(row=2, column=3, padx=10, pady=10)

        # number of days label
        self.days_label = Label(self.bottom, font=('arial', 20, 'bold'), text="ENTER NUMBER OF DAYS TO STAY :",
                                fg="#0000FF",
                                anchor="w")
        self.days_label.grid(row=3, column=2, padx=10, pady=10)

        # text enter field
        self.days_var = IntVar()
        self.days_entry = Entry(self.bottom, width=50, text=self.days_var)
        self.days_entry.grid(row=3, column=3, padx=10, pady=10)

        

        # mode label
        self.mode_label = Label(self.bottom, font=('arial', 20, 'bold'), text="MODE OF PAYMENT: ",
                                       fg="#0000FF",
                                       anchor="w")
        self.mode_label.grid(row=4, column=2, padx=10, pady=10)
        
        #Mode of payment
        n=StringVar()
        self.mode=ttk.Combobox(self.bottom,width=27,textvariable=n)
        self.mode['values']=('Select',
                    'CASH',
                    'UPI',
                    'DEBIT CARD')
        self.mode.grid(row=4,column=3, padx=10, pady=10)
        self.mode.current(0)

        roomnumber = [101, 102, 103, 104, 301, 302, 303, 304, 401, 402,403,404,201,202,203,204]
        self.room_number_var = random.choice(roomnumber)

        
        
        def submit_info():
            global ans
            name = self.name_entry.get()
            address = self.address_entry.get()
            room = self.room_number_var
            mobile=self.mobile_entry.get()
            days=self.days_entry.get()
            mode=self.mode.get()

            while True:
                self.h = str(self.mobile_entry.get())
                if self.h.isdigit() == True and len(self.h) != 0 and len(self.h) == 10:
                    mobile = self.h
                    ans = TRUE
                    break
                else:
                    ans = False
                    messagebox.showerror("ERROR", "PLEASE ENTER 10 DIGIT MOBILE NUMBER")
                    break

            while True:
                self.h = str(self.days_entry.get())
                if self.h.isdigit():
                    days = self.h
                    ans1 = True
                    break
                else:
                    ans1 = False
                    messagebox.showerror("ERROR", "NUMBER OF DAYS CANNOT BE VARIABLE")
                    break
                
            #Receipt Generation
            if ans == TRUE and ans1 == True:
                print("Reciept Generating")
                def reciept():
                    self.w1=Tk()            
                    self.w1.title("Hotel Management System")
                    l=Label(self.w1,text="RECIEPT",relief=RAISED,borderwidth=10,bg='BLACK',fg='white',font='TIMESNEWROMAN 30 bold')
                    l.pack(side=TOP)
                    f=Frame(self.w1,relief=RAISED,borderwidth=10)
                    f.pack()
                    l1=Label(f,text="Name                        : ",font='calibri 25').grid(row=0,column=0,sticky=W)
                    l2=Label(f,text="Address                    : ",font='calibri 25').grid(row=1,column=0,sticky=W)
                    l3=Label(f,text="Mobile No.              : ",font='calibri 25').grid(row=2,column=0,sticky=W)
                    l4=Label(f,text="No. Of Days             : ",font='calibri 25').grid(row=3,column=0,sticky=W)
                    l5=Label(f,text="Room No. Alotted : ",font='calibri 25').grid(row=4,column=0,sticky=W)
                    l6=Label(f,text="Payed through       : ",font='calibri 25').grid(row=5,column=0,sticky=W)
                    l7=Label(f,text=name,font='calibri 25').grid(row=0,column=1,sticky=W)
                    l8=Label(f,text=address,font='calibri 25').grid(row=1,column=1,sticky=W)
                    l9=Label(f,text=mobile,font='calibri 25').grid(row=2,column=1,sticky=W)
                    l10=Label(f,text=days,font='calibri 25').grid(row=3,column=1,sticky=W)
                    l11=Label(f,text=room,font='calibri 25').grid(row=4,column=1,sticky=W)
                    l12=Label(f,text=mode,font='calibri 25').grid(row=5,column=1,sticky=W)
                    self.w1.mainloop()
                
                
                #DataBase
                conn = sqlite3.connect('Hotel.db')
                print("Connection Extablished ",conn)
                with conn:
                    cursor = conn.cursor()
                print("Cursor ",cursor)
                cursor.execute(
                    'CREATE TABLE IF NOT EXISTS Hotel (Name TEXT,Address TEXT,mobile_number NUMBER,number_days '
                    'NUMBER,room_number NUMBER,mode TEXT)')
                cursor.execute('INSERT INTO Hotel (Name,Address,mobile_number,number_days,room_number,mode) '
                               'VALUES(?,?,?,?,?,?)', (name, address, mobile, days, room,mode))
                conn.commit()
                with conn:
                    cursor.execute("SELECT * FROM Hotel")
                    print(cursor.fetchall())
                reciept()
            room_number()
            self.name_var.set('')
            self.address_var.set('')
            self.days_var.set('')
            self.mobile_var.set('')

        def room_number():
            room_number_taken.append(self.room_number_var)
            print(room_number_taken)

        def reset():
            self.room_number_var = random.choice(roomnumber)
            

            self.name_entry.delete(0, END)
            self.name_entry.insert(0, "")

            self.mobile_entry.delete(0, END)
            self.mobile_entry.insert(0, "")

            self.address_entry.delete(0, END)
            self.address_entry.insert(0, "")

            self.days_entry.delete(0, END)
            self.days_entry.insert(0, "")

        # create submit button
        self.submit_button = Button(self.checkbox1, text="SUBMIT", font=('', 15), bg='orange', relief=RIDGE,
                                       height=2,
                                       width=20, fg="black", anchor="center", command=submit_info)
        self.submit_button.grid(row=6, column=2)

        # back to home page
        self.back_home_button = Button(self.checkbox1, text="HOME", font=('', 15),bg='orange', relief=RIDGE,
                                       height=2,
                                       width=20, fg="black", anchor="center",command=self.root.destroy)
        self.back_home_button.grid(row=6, column=1)

        Button(self.checkbox1, text="RESET", font=('', 15), bg='orange', relief=RIDGE,
                                       height=2,
                                       width=20, fg="black", anchor="center", command=reset).grid(row=6, column=3)


def check_in_ui_fun():
    root = Toplevel()
    application = CheckIN(root)
    root.mainloop()
