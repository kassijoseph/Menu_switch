from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import messagebox
import time
import sqlite3
import sys
from Home import Home  # Assurez-vous que le module Home est correctement importé

class Accueil:
    def __init__(self, root):
        self.root = root
        self.root.title("Administration")
        self.root.geometry("1600x830+0+0")
        self.root.config(bg="gray")

        option_frame = Frame(self.root, bg="blue")
        option_frame.pack(side=LEFT)
        option_frame.pack_propagate(False)
        option_frame.config(width=400, height=830)

        ###########les boutons
        menu_btn = Button(option_frame, text="Home", font=("times new roman", 15, "bold"), fg="black", bg="blue", activebackground="blue", command=lambda: self.selection(self.selection_menu, self.open_Home))
        menu_btn.place(x=20, y=0)

        inscription_btn = Button(option_frame, text="Inscription", font=("times new roman", 15, "bold"), fg="black", bg="blue", activebackground="blue", command=lambda: self.selection(self.selection_inscription))
        inscription_btn.place(x=20, y=50)

        connexion_btn = Button(option_frame, text="Connexion", font=("times new roman", 15, "bold"), fg="black", bg="blue", activebackground="blue", command=lambda: self.selection(self.selection_connexion))
        connexion_btn.place(x=20, y=100)

        quitter_btn = Button(option_frame, text="Quitter", font=("times new roman", 15, "bold"), fg="black", bg="blue", activebackground="blue", command=lambda: self.selection(self.selection_quitter))
        quitter_btn.place(x=20, y=150)

        ######les tirait des boutons
        self.selection_menu = Button(option_frame, text="", bg="blue")
        self.selection_menu.place(x=5, y=0, height=40, width=5)

        self.selection_inscription = Button(option_frame, text="", bg="blue")
        self.selection_inscription.place(x=5, y=50, height=40, width=5)

        self.selection_connexion = Button(option_frame, text="", bg="blue")
        self.selection_connexion.place(x=5, y=100, height=40, width=5)

        self.selection_quitter = Button(option_frame, text="", bg="blue")
        self.selection_quitter.place(x=5, y=150, height=40, width=5)

        main_frame = Frame(self.root, bg="gray", highlightbackground="blue", highlightthickness=3)
        main_frame.pack(side=LEFT)
        main_frame.pack_propagate(False)
        main_frame.config(width=1125, height=830)

    def selection(self, lb, func=None):
        self.cacher_selection()
        lb.config(bg="black")
        if func:  # Exécute la fonction si elle est fournie
            func()

    def cacher_selection(self):
        self.selection_menu.config(bg="blue")
        self.selection_inscription.config(bg="blue")  
        self.selection_connexion.config(bg="blue") 
        self.selection_quitter.config(bg="blue")

    def open_Home(self):
        Home_interface = Home(self.root)  # Assurez-vous d'utiliser self.root pour afficher la nouvelle interface
        # Si vous avez besoin de faire d'autres initialisations dans Home, ajoutez-les ici

if __name__ == "__main__":
    root = Tk()
    obj = Accueil(root)
    root.mainloop()
