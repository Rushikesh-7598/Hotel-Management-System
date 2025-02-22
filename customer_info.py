import sqlite3
from tkinter import *
import main


class CustomerInfo:
    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.title("CUSTOMER INFO")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))
        
        self.bg = PhotoImage(file = "sea.png")
  
        # Show image using label
        label1 = Label( root, image = self.bg)
        label1.place(x = 0, y = 0)

        # create mainframe to add message
        top = Frame(self.root)
        top.pack(side="top")

        top1 = Frame(self.root)
        top1.pack(side="top")

        bottom = Frame(self.root)
        bottom.pack(side="top")

        left = Frame(self.root, relief="solid")
        left.pack(side="left")

        right = Frame(self.root, relief="solid")
        right.pack(side="right")

        # display message
        self.label = Label(top,text="CUSTOMER-ROOM INFO",relief=RAISED,borderwidth=10,height=3,width=30,bg='BLACK',fg='orange',font='algerian 20 bold',anchor='center')
        self.label.grid(row=0, column=2)

        # display message name
        self.name_label = Label(left, font=('arial', 20, 'bold'), text="NAME OF CUSTOMER", fg="#0000FF", anchor="center")
        self.name_label.grid(row=0, column=1, padx=10, pady=10)

        # text enter field LEFT
        self.name_customer_entry = Text(left, height=10, width=30,font=('arial', 20))
        self.name_customer_entry.grid(row=1, column=1, padx=10, pady=10)

        # display message
        self.room_no_label = Label(right, font=('arial', 20, 'bold'), text="ROOM NO. ALOTTED", fg="#0000FF", anchor="center")
        self.room_no_label.grid(row=0, column=1, padx=10, pady=10)

        # text enter field RIGHT
        self.room_no_customer_entry = Text(right, height=10, width=30,font=('arial', 20))
        self.room_no_customer_entry.grid(row=1, column=1, padx=10, pady=10)

        # create home button
        self.home_button = Button(top1, text="HOME", font=('', 15), bg='orange', relief=RIDGE,
                                       height=2,
                                       width=20, fg="black", anchor="center",command=self.root.destroy)
        self.home_button.grid(row=1, column=1)

        def display_info():
            self.room_no_customer_entry.delete("1.0", "end")
            self.name_customer_entry.delete("1.0", "end")
            conn = sqlite3.connect('Hotel.db')
            with conn:
                cursor = conn.cursor()
            cursor.execute(
                    'CREATE TABLE IF NOT EXISTS Hotel (Name TEXT,Address TEXT,mobile_number NUMBER,number_days '
                    'NUMBER,room_number NUMBER,mode TEXT)')
            conn.commit()
            with conn:
                cursor.execute("SELECT Name FROM Hotel")
                ans = cursor.fetchall()
                for i in ans:
                    self.name_customer_entry.insert(INSERT, i[0] + '\n')

            with conn:
                cursor.execute("SELECT room_number FROM Hotel")
                ans = cursor.fetchall()
                for i in ans:
                    self.room_no_customer_entry.insert(INSERT, str(i[0]) + '\n')
        # create display button
        self.display_button = Button(top1, text="DISPLAY", font=('', 15), bg='orange', relief=RIDGE,
                                       height=2,
                                       width=20, fg="black", anchor="center",command=display_info)
        self.display_button.grid(row=1, column=3)


def customer_info_ui():
    root = Toplevel()
    application = CustomerInfo(root)
    root.mainloop()
