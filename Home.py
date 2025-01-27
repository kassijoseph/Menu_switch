from tkinter import *
from tkinter import Frame, Label, Entry, Button

class Home:
    def __init__(self, master_frame):
        self.master_frame = master_frame
        self.frame = Frame(self.master_frame, bg="gray")
        self.frame.pack(fill=BOTH, expand=True)
    

    
        Label(self.frame, text="Welcome to the Home Page", font=("Arial", 24), bg="gray").pack(pady=20)
