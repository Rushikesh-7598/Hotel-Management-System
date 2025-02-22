import sqlite3
from tkinter import *
import main


class CheckOut:
    def __init__(self, root):

        self.root = root
        pad = 3
        self.root.title("CHECK OUT")
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
        

        info_frame = Frame(self.root)
        info_frame.pack(side="top")

        bottom1= Frame(self.root)
        bottom1.pack(side="top")
        

        # display message
        self.label = Label(top,text="CHECK OUT",relief=RAISED,borderwidth=10,height=3,width=30,bg='BLACK',fg='orange',font='algerian 20 bold')
        self.label.grid(row=0, column=3)

        # room no label
        self.room_no_label = Label(bottom,font=('arial', 20, 'bold'), text="ENTER THE ROOM NUMBER :", fg="blue",
                                   anchor="center")
        self.room_no_label.grid(row=2, column=1, padx=10, pady=10)
        #self.room_no_label.place(x=200,y=200)

        # text enter field
        self.room_var = IntVar()
        self.room_no_entry = Entry(bottom, width=20, text=self.room_var,font=('arial', 20, 'bold'))
        self.room_no_entry.grid(row=2, column=3, padx=10, pady=10)

        # text enter field
        self.get_info_entry = Text(info_frame, height=7, width=48,font=('arial', 20))
        self.get_info_entry.grid(row=1, column=1, padx=10, pady=10)

        def check_out():
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
                        cursor.execute("SELECT Name,room_number FROM Hotel")
                        ans = cursor.fetchall()
                        for i in ans:
                            if room_number1 == int(i[1]):
                                self.get_info_entry.insert(INSERT,
                                                           '\n' + str(i[0]) + ' has checked out from Room- ' + str(i[1]) + '\n')
                                with conn:
                                    cursor.execute("""DELETE FROM Hotel where room_number = ?""", [room_number1])

                else:
                    self.get_info_entry.insert(INSERT, "Room-"+str(room_number1)+" is Empty\n")

        

        # create submit button
        self.check_out_button = Button(bottom1, text="SUBMIT", font=('', 15), bg='orange', relief=RIDGE,
                                       height=2,
                                       width=20, fg="black", anchor="center", command=check_out)
        self.check_out_button.grid(row=1, column=1, padx=10, pady=10)
        #self.check_out_button.pack(side='left')
        # create submit button
        self.home_button = Button(bottom1, text="HOME", font=('', 15), bg='orange', relief=RIDGE,
                                       height=2,
                                       width=20, fg="black", anchor="center",command=self.root.destroy)
        self.home_button.grid(row=1, column=3, padx=10, pady=10)
        #self.check_out_button.pack(side='right')

def check_out_ui():
    root = Toplevel()
    application = CheckOut(root)
    root.mainloop()                         