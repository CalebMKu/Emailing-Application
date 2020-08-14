import tkinter as tk
from tkinter import font
from tkinter import *
import re
import smtplib

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


class FirstWindow(object):
    def __init__(self, title, size, color):
        self.root = tk.Tk()

        self.title = title
        self.size = size
        self.color = color

        self.title = self.root.title(self.title)
        self.size = self.root.geometry(self.size)
        self.color = self.root.configure(bg=self.color)

        self.root.resizable(False, False)

    def loop(self):
        self.root.mainloop()

    def head(self):
        header = tk.Label(self.root, text="Sign in -", bg="white", font="Consoles, 20")
        header.grid(row=0, column=0)

    def body(self):
        email_label = tk.Label(self.root, text="Email: ", bg="white", font="Consoles, 13")
        email_label.grid(row=2, column=0)

        self.email = tk.Entry(self.root, width=30, font="Consoles, 13")
        self.email.grid(row=2, column=1)

        password_label = tk.Label(self.root, text="Password: ", bg="white", font="Consoles, 13")
        password_label.grid(row=3, column=0)

        password = tk.Entry(self.root, width=30, font="Consoles, 13")
        password.grid(row=3, column=1)

        def check():  
            person_email = self.email.get()    
            # pass the regular expression 
            # and the string in search() method 
            if(re.search(regex,person_email)):  
                secondwindow = tk.Tk()

                secondwindow.title("Send Mail")
                secondwindow.geometry("600x300")
                secondwindow.configure(bg="white")

                recipient_label = tk.Label(secondwindow, text="RECIEVER", bg="white", font="Consoles, 13")
                recipient_label.pack()

                recipient = tk.Entry(secondwindow, width=50, font="Consoles, 13")
                recipient.pack()

                message_label = tk.Label(secondwindow, text="MESSAGE", bg="white", font="Consoles, 13")
                message_label.pack()

                message = tk.Text(secondwindow, width=50, height=10, font="Consoles, 13")
                message.pack()
                
                def send_mail():
                    # creates SMTP session 
                    s = smtplib.SMTP('smtp.gmail.com', 587) 
  
                    # start TLS for security 
                    s.starttls() 
  
                    # Authentication 
                    s.login(self.email.get(), password.get()) 
  
                    # message to be sent 
                    msg = message.get("1.0", "end-1c")
  
                    # sending the mail 
                    s.sendmail(self.email.get(), recipient.get(), msg) 
  
                    # terminating the session 
                    s.quit() 
                    
                send_button = tk.Button(secondwindow, text="Send", bg="lightgrey", width=5, height=1, command=send_mail)
                send_button.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)

                secondwindow.mainloop()
            else:  
                invalid_email = tk.Label(self.root, bg="white", text="Invalid Email")
                invalid_email.grid(row=3, column=0)

        next_button = tk.Button(self.root, text="Next", bg="lightgrey", width=5, height=1, command=check)
        next_button.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)

if __name__ == "__main__":
    mwindow = FirstWindow("Sign In", "500x100", "white")
    mwindow.head()
    mwindow.body()
    mwindow.loop()