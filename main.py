from tkinter import *
import check_in_ui
import check_out
import get_info
import customer_info
import os

class Hotel:
    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))
            
        self.bg = PhotoImage(file = "sea.png")
        # Show image using label
        label1 = Label( root, image = self.bg)
        label1.place(x = 0, y = 0)
                
        top = Frame(self.root)
        top.pack(side="top")
        
        # display message
        self.label =Label(top,text="WELCOME TO THE ROYAL SEA RESORT",relief=RAISED,borderwidth=10,height=3,width=40,bg='BLACK',fg='orange',font='algerian 20 bold')
        self.label.grid(row=0, column=3)

        # create check in button
        self.check_in_button = Button( text="CHECK IN", font=('', 20), bg='orange',fg='black',height=2,width=30, relief=RIDGE,
                                      anchor="center",
                                      command=check_in_ui.check_in_ui_fun)  # call check_in_ui_fun from check_in_ui.py file
        self.check_in_button.place(x=100,y=150)

        # create check out button
        self.check_out_button = Button( text="CHECK OUT", font=('', 20), bg='orange', relief=RIDGE, height=2,
                                       width=30, fg="black", anchor="center",
                                       command=check_out.check_out_ui)  # call check_out_ui function from check_out.py file
        self.check_out_button.place(x=700,y=150)

        # create show list button
        self.room_info_button = Button(text="INFORMATION OF ROOMS", font=('', 20), bg='orange', relief=RIDGE,
                                       height=2,
                                       width=30, fg="black", anchor="center",
                                       command=get_info.get_info_ui)  # call get_info_ui function from get_info.py file
        self.room_info_button.place(x=100,y=300)

        # create get information of all the guest
        self.get_info_button = Button(text="INFORMATION OF ALL GUEST", font=('', 20), bg='orange',
                                      relief=RIDGE,
                                      height=2, width=30, fg="black", anchor="center",
                                      command=customer_info.customer_info_ui)
        # call customer_info_ui function from customer_info.py file
        self.get_info_button.place(x=700,y=300)

        # button to exit the program
        self.exit_button = Button( text="EXIT", font=('', 20), bg='orange', relief=RIDGE,height=2, width=50,
                                  fg="black",
                                  anchor="center", command=quit)
        self.exit_button.place(x=250,y=450)

def home_ui():
    root = Tk()
    application = Hotel(root)
    root.mainloop()

if __name__ == '__main__':
    home_ui()
