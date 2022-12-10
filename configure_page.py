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
        self.word_list = ["Select a Word List"]
        if os.path.exists(f"wordlist.txt"):
            with open("wordlist.txt", "r") as file:
                for f in file.readlines():
                    f = f.split("[")[0]
                    self.word_list.append(f)
        self.word_list_start_variable = tk.StringVar(self.root)
        self.word_list_start_variable.set(self.word_list[0])
        self.word_list_menu = tk.OptionMenu(self.root, self.word_list_start_variable, *self.word_list, command=self.set_fields)

        self.hint = tk.Label(self.root, text= "Please note that asterisks are wildcard characters")

        self.title_text = tk.Label(self.root, text=" Word List Title")
        self.wordlist_text = tk.Label(self.root, text="Word List (Comma Delimited)")

        self.title_bar = tk.Text(self.root, height=2, width=15)
        self.wordlist_bar = tk.Text(self.root, height=2, width=15)

        self.delete_button = tk.Button(self.root, text="Delete", command=self.remove_wordlist)
        self.export_text_button = tk.Button(self.root, text="Save", command=self.export_text)
        self.return_searchpage_button = tk.Button(self.root, text="Return to Search Page", command=self.exit)

        self.word_list_menu.place(x=(500/2)-70, y = 10, width = 150)

        self.title_text.place(x=(500/2)-150, y=40, width=300, height=30)
        self.wordlist_text.place(x=(500/2)-150, y=90, width=300, height=30)

        self.title_bar.place(x=(500/2)-90, y=70, width=180, height=25)
        self.wordlist_bar.place(x=(500/2)-150, y=135, width=300, height=120)

        self.delete_button.place(x=(500/2)-100, y=260, width=220, height=25)
        self.export_text_button.place(x=(500/2)-100, y=290, width=220, height=25)
        self.return_searchpage_button.place(x=(500/2)-90, y=320, width=200, height=25)

        self.hint.place(x=(500/2)-150, y=120, width=300, height=10)

    def set_fields(self, var):
        word_list_title = self.word_list_start_variable.get()
        file_exists = os.path.exists(f"wordlist.txt")

        if file_exists:
            with open(f"wordlist.txt", "r") as f:
                for list in f.readlines():
                    list = list.split("[")
                    if word_list_title == list[0]:
                        word_list = list[1].replace(']', '').replace("'", "").split(',')

                        word_list = [x.strip() for x in word_list]
                        self.title_bar.delete(1.0,"end")
                        self.title_bar.insert(1.0, word_list_title)
                        self.wordlist_bar.delete(1.0, "end")
                        for word in word_list:
                            self.wordlist_bar.insert("end", word + ",")

                        self.wordlist_bar.delete("end-2c", "end")


    def remove_wordlist(self):
        word_list_title = self.title_bar.get(1.0, "end")
        file_exists = os.path.exists(f"wordlist.txt")
        new_file_text = ""
        if file_exists:
            with open(f"wordlist.txt", "r") as f:
                for list in f.readlines():
                    list_title = list.split("[")[0]
                    print(list_title.strip() + "=" + word_list_title.strip())
                    print(not list_title.strip() == word_list_title.strip())
                    if not list_title.strip() == word_list_title.strip():
                        print("List: " + list)
                        new_file_text = new_file_text + list

            with open(f"wordlist.txt", "w") as f:
                f.write(new_file_text)

        self.title_bar.delete(1.0,"end")
        self.wordlist_bar.delete(1.0, "end")





    def exit(self):
        self.root.quit()
        self.root.destroy()

    def export_text(self):

        self.word_title = self.title_bar.get("1.0","end")
        self.title = str(self.word_title).replace("\n","")

        self.word_list = self.wordlist_bar.get("1.0","end").split(',')

        self.remove_space = [self.word_list.strip() for self.word_list in self.word_list]


        file_exists = os.path.exists(f"wordlist.txt")

        if file_exists:
            list_exists = False
            new_file_text = ""
            line_number = 0
            with open(f"wordlist.txt", "r") as f:
                for line in f.readlines():
                    line_title = line.split("[")[0]
                    if line_title.strip() == self.title_bar.get(1.0, "end").strip():
                        if line_number != 0:
                            new_file_text = new_file_text + "\n" + str(self.title) + str(self.remove_space)
                        else:
                            new_file_text = new_file_text + str(self.title) + str(self.remove_space)
                        list_exists = True
                    else:
                        new_file_text = new_file_text + line

                    if not list_exists:
                        new_file_text = new_file_text + "\n" + str(self.title) + str(self.remove_space)
                    line_number = line_number + 1

            with open(f"wordlist.txt", "w") as f:
                f.write(new_file_text)


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