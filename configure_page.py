from os import remove
import tkinter as tk
import tkinter.filedialog
import os.path


class ConfigurePage:
    
    def __init__(self):

        self.root = tk.Tk()
        self.padding = {'padx': 7, 'pady': 7}
        self.root.title("Data Scraping Tool")
        self.root.geometry("500x350")

        self.hint = tk.Label(self.root, text= "Please note that asterisks are wildcard characters")

        self.title_text = tk.Label(self.root, text=" Word List Title")
        self.wordlist_text = tk.Label(self.root, text="Word List (Comma Delimited)")

        self.title_bar = tk.Text(self.root, height=2, width=15)
        self.wordlist_bar = tk.Text(self.root, height=2, width=15)

        self.export_text_button = tk.Button(self.root, text="Save", command=self.export_text)
        self.return_searchpage_button = tk.Button(self.root, text="Return to Search Page", command=self.root.destroy)

        self.hint.place(x=(500/2)-150, y=10, width=300, height=10)

        self.title_text.place(x=(500/2)-150, y=40, width=300, height=30)
        self.wordlist_text.place(x=(500/2)-150, y=105, width=300, height=30)

        self.title_bar.place(x=(500/2)-90, y=70, width=180, height=25)
        self.wordlist_bar.place(x=(500/2)-150, y=135, width=300, height=120)

        self.export_text_button.place(x=(500/2)-100, y=270, width=200, height=25)
        self.return_searchpage_button.place(x=(500/2)-100, y=300, width=200, height=25)

    def export_text(self):

        self.word_title = self.title_bar.get("1.0","end")
        self.title = str(self.word_title).replace("\n","")

        self.word_list = self.wordlist_bar.get("1.0","end").split(',')

        self.remove_space = [self.word_list.strip() for self.word_list in self.word_list]


        file_exists = os.path.exists(f"wordlist.txt")

        if file_exists:
            with open(f"wordlist.txt", "a") as f:
                f.write("\n")
                f.write(str(self.title))
                f.write(str(self.remove_space))

        else:
            with open(f"wordlist.txt", "w") as f:
                f.write(str(self.title))
                f.write(str(self.remove_space))

        self.title_bar.delete("1.0", "end")
        self.wordlist_bar.delete("1.0", "end")

    def make_window(self):
        self.root.mainloop()

if __name__ == '__main__':
    application = ConfigurePage()
    application.make_window()