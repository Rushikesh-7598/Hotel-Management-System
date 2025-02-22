import sqlite3
from tkinter import *
import main


class GetInfo:
    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.title("GET INFO")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))

        self.bg = PhotoImage(file = "sea.png")
  
        # Show image using label
        label1 = Label( root, image = self.bg)
        label1.place(x = 0, y = 0)

        # create mainframe to add message
        top = Frame(self.root)
        top.pack(side="top")

        bottom = Frame(self.root)
        bottom.pack(side="top")

        info_frame = Frame(self.root, width=454, height=20)
        info_frame.pack(side="top")

        button_frame = Frame(self.root)
        button_frame.pack(side="top")


        # display message
        self.label = Label(top,text="INFORMATION OF CUSTOMER",relief=RAISED,borderwidth=10,height=3,width=30,bg='BLACK',fg='orange',font='algerian 20 bold')
        self.label.grid(row=0, column=3)

        # room no label
        self.room_no_label = Label(bottom,font=('arial', 20, 'bold'), text="ENTER THE ROOM NUMBER :", fg="#0000FF",
                                   anchor="center")
        self.room_no_label.grid(row=2, column=1, padx=10, pady=10)

        # text enter field
        self.room_var = IntVar()
        self.room_no_entry = Entry(bottom, width=20, text=self.room_var,font=('arial', 20, 'bold'))
        self.room_no_entry.grid(row=2, column=3, padx=10, pady=10)

        # text enter field
        self.get_info_entry = Text(info_frame, height=7, width=48,font=('arial', 20))
        self.get_info_entry.grid(row=1, column=1, padx=10, pady=10)
        self.get_info_entry.insert(INSERT,"INFO WILL BE DISPLAYED HERE.")




        def get_info():
            room_number1 = int(self.room_no_entry.get())
            self.get_info_entry.delete("1.0", "end")
            conn = sqlite3.connect('Hotel.db')
            with conn:
                cursor = conn.cursor()
            cursor.execute(
                    'CREATE TABLE IF NOT EXISTS Hotel (Name TEXT,Address TEXT,mobile_number NUMBER,number_days '
                    'NUMBER,room_number NUMBER,mode TEXT)')
            conn.commit()
            with conn:
                cursor.execute("SELECT room_number FROM Hotel")
                ans = cursor.fetchall()
                room = []
                for i in ans:
                    room.append(i[0])
                if room_number1 in room:
                    with conn:
                        cursor.execute("SELECT * FROM Hotel")
                        ans = cursor.fetchall()
                        
                        for i in ans:
                            if room_number1 == int(i[4]):
                                self.get_info_entry.insert(INSERT,
                                                           'NAME: ' + str(i[0]) + '\nADDRESS: ' + str(i[1]) + '\nMOBILE NUMBER:  ' + str(i[2]) + '\nNUMBER OF DAYS: ' + str(i[3]) + '\nROOM NUMBER: ' + str(i[4]) + '\n')
                else:
                    self.get_info_entry.insert(INSERT, "\nPLEASE ENTER VALID ROOM NUMBER")

        # create submit button
        self.submit_button = Button(button_frame, text="SUBMIT", font=('', 15), bg='orange', relief=RIDGE,
                                       height=2,
                                       width=20, fg="black", anchor="center", command=get_info)
        self.submit_button.grid(row=8, column=2, padx=10, pady=10)

        # create home button
        self.home_button = Button(button_frame, text="HOME", font=('', 15), bg='orange', relief=RIDGE,
                                       height=2,
                                       width=20, fg="black", anchor="center",command=self.root.destroy)
        self.home_button.grid(row=8, column=3, padx=10, pady=10)


def get_info_ui():
    root = Toplevel()
    application = GetInfo(root)
    root.mainloop()
