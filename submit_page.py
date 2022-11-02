import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import datetime
import os
from configure_page import ConfigurePage
from threading import Thread

class SubmitPage:

    def __init__(self):
        self.root = tk.Tk()
        self.padding = {'padx': 7, 'pady': 7}
        self.root.title("Data Scraping Tool")
        self.root.geometry("500x350")

        self.title_text = tk.Label(self.root, text="Query Submit Results")
        # self.title_bar = tk.Text(self.root, height=2, width=15)

        self.title_text.place(x=(500/2)-150, y=40, width=300, height=30)
        # self.title_bar.place(x=(500/2)-120, y=90, width=250, height=150)
        self.p = Progressbar(self.root, orient="horizontal", length=250, mode="determinate")
        self.p.place(x=125, y=350-270)

    def display_query(self, text:list=["Default text"], x:int=500/2- 10, y:int=350/2-20):
        # self.title_bar = tk.Text(self.root, height=2, width=15)
        for i in text:
            self.p["value"] = len(text) * 10
            self.root.update_idletasks()
            self.t = tk.Label(self.root, text=i) #creates tk label and sets text to be method parameter
            self.t.place(x=x-20, y=y) # places new tk label according to method parameters
            y += 20  # increments the y value for the next iteration so next item isn't placed on previous

        self.num_total = tk.Label(self.root, text=f"{len(text)} clk numbers found")
        self.num_total.place(x=193, y=350-230)

    def make_window(self):
        self.root.mainloop()

if __name__ == '__main__':
    application = SubmitPage()
    application.make_window()