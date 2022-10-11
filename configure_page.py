import tkinter as tk
import tkinter.filedialog


class ConfigurePage:
    
    def __init__(self):

        self.root = tk.Tk()
        self.padding = {'padx': 7, 'pady': 7}
        self.root.title("Data Scraping Tool")
        self.root.geometry("500x350")

        self.title_text = tk.Label(self.root, text=" Word List Title")
        self.wordlist_text = tk.Label(self.root, text="Word List (Space Delimited)")

        self.title_bar = tk.Text(self.root, height=2, width=15)
        self.wordlist_bar = tk.Text(self.root, height=2, width=15)

        self.export_text_button = tk.Button(self.root, text="Export to New Text File", command=self.export_text)
        self.return_searchpage_button = tk.Button(self.root, text="Return to Search Page", command=self.root.destroy)

        self.title_text.place(x=(500/2)-150, y=40, width=300, height=30)
        self.wordlist_text.place(x=(500/2)-150, y=105, width=300, height=30)

        self.title_bar.place(x=(500/2)-90, y=70, width=180, height=25)
        self.wordlist_bar.place(x=(500/2)-150, y=135, width=300, height=120)

        self.export_text_button.place(x=(500/2)-100, y=270, width=200, height=25)
        self.return_searchpage_button.place(x=(500/2)-100, y=300, width=200, height=25)

    def export_text(self):
        path = tk.filedialog.askdirectory()
        self.outputDir = path

        self.word_title = self.title_bar.get("1.0","end")
        self.title = str(self.word_title).replace("\n","")

        self.word_list = self.wordlist_bar.get("1.0","end")

        with open(f"{self.title}.txt", "w") as f:
            f.write(str(self.word_list))

    def make_window(self):
        self.root.mainloop()

if __name__ == '__main__':
    application = ConfigurePage()
    application.make_window()