import tkinter as tk
import re
class EmailPage:

    def __init__(self):
        """
        This method sets up the GUI with the labels and buttons that make up the visual parts of the application.
        """

        self.root = tk.Tk()
        self.root.grid()
        self.padding = {'padx': 7, 'pady': 7}
        self.root.title("Data Scraping Tool")

        self.user_email = ""

        self.root.geometry("300x120")

        self.export_new_button = tk.Button(self.root, text="Enter", command=self.save_email)
        self.text_bar = tk.Text(self.root, height=2, width=15)
        self.label_email = tk.Label(self.root, text="Please Enter Your Email")

        self.label_email.place(x=(300/2)-70, y=15)
        self.export_new_button.place(x=(300/2)-140, y=80, width=280)
        self.text_bar.place(x=(300/2)-140, y=50, width=280, height=20)

    def save_email(self):
        email = self.text_bar.get('1.0', 'end')
        regex = re.compile(r'^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$')

        valid_email = re.match(regex, email)
        if valid_email:
            print("Valid Email")
            with open(f"useremail.txt", "w") as f:
                f.write(email)
            self.user_email = email
            self.root.quit()
            self.root.destroy()
        else:
            print("Invalid Email")


    def get_user_email(self):
        return self.user_email

    def make_window(self):
        self.root.mainloop()
