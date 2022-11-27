import tkinter as tk

class WarningPage:
    def __init__(self, message):
        """
        This method sets up the GUI with the labels and buttons that make up the visual parts of the application.
        """

        self.root = tk.Tk()

        self.root.title("Data Scraping Tool")

        self.root.geometry("300x120")

        self.export_new_button = tk.Button(self.root, text="Close", command=self.root.destroy)

        self.label_finish = tk.Label(self.root, text=message, wraplength=270, justify=tk.CENTER)

        self.label_finish.place(x=(200/2)-75, y=10)
        self.export_new_button.place(x=(200/2)-90, y=90, width=280)