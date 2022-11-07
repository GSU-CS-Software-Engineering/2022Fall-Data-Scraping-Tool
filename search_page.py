import tkinter as tk
import datetime
import os
from configure_page import ConfigurePage
from webscraper import WebScraper
from text_parser import Parser
from threading import Thread
from submit_page import SubmitPage

class SearchPage:

    def __init__(self, email):
        """
        This method sets up the GUI with the labels and buttons that make up the visual parts of the application.
        """

        self.root = tk.Tk()
        self.padding = {'padx': 7, 'pady': 7}
        self.root.title("Data Scraping Tool")
        self.root.geometry("500x350")

        self.email = email
        self.webscraper = WebScraper()
        self.parser = Parser()
        current_time = datetime.datetime.now()
        years = []
        self.word_list = []
        self.word_list.append("Select a Word List")
        for year in range(2001, current_time.year+1):
            years.append(year)

        self.word_list_button = tk.Button(self.root, text="Configure Word List", command=self.configure)
        self.analyze_button = tk.Button(self.root, text="Submit Query", command=self.analyze)
        self.search_bar = tk.Text(self.root, height=2, width=15)
        self.label_search = tk.Label(self.root, text="Search For 10-K Results")
        self.label_cik = tk.Label(self.root, text='CIK List (Comma Delimited)')
        self.label_date_start = tk.Label(self.root, text='Start Date')
        self.label_date_end = tk.Label(self.root, text='End Date')

        self.date_start_variable = tk.StringVar(self.root)
        self.date_end_variable = tk.StringVar(self.root)
        self.date_start_variable.set(years[0])
        self.date_end_variable.set(years[-1])
        self.word_list_start_variable = tk.StringVar(self.root)
        self.word_list_start_variable.set(self.word_list[0])
        self.date_start_menu = tk.OptionMenu(self.root, self.date_start_variable, *years)
        self.date_end_menu = tk.OptionMenu(self.root, self.date_end_variable, *years)
        self.word_list_menu = tk.OptionMenu(self.root, self.word_list_start_variable, *self.word_list)
        self.update_word_list()
        self.hours_worked_text = tk.Text(self.root, height=1, width=5)

        self.label_search.place(x=(500/2)-60, y=10)
        self.label_cik.place(x=(500/2)-70, y=60)
        self.label_date_start.place(x=(500/2)-30, y=140)
        self.label_date_end.place(x=(500/2)-30, y=190)
        self.date_start_menu.place(x=(500/2)-30, y=160)
        self.date_end_menu.place(x=(500/2)-30, y=210)
        self.analyze_button.place(x=(500/2)-90, y=310, width=200)
        self.search_bar.place(x=(500/2)-150, y=90, width=300, height=50)
        self.word_list_button.place(x=(500/2)-90, y=280, width=200)
        self.word_list_menu.place(x=(500/2)-30, y=245)

    def update_word_list(self):
        print("updating word list")
        file_exists = os.path.exists(f"wordlist.txt")

        if file_exists:
            with open(f"wordlist.txt", "r") as f:
                list_title = f.readline().split("[")[0]
                if list_title not in self.word_list:
                    self.word_list.append(list_title)
                    self.word_list_menu['menu'].add_command(label=list_title, command=tk._setit(self.word_list_start_variable, list_title))

            self.word_list_start_variable.set(self.word_list[0])

    def analyze(self):
        valid = True
        cik_numbers = self.search_bar.get('1.0', 'end').split(',')
        cik_numbers = [cik.strip() for cik in cik_numbers]
        head = {'User-Agent': 'Georgia Southern University AdminContact@{self.email}'}
        self.set_wordlist()
        print(self.word_list)
        for ciks in cik_numbers:
            try:
                int(ciks)
                soup = self.webscraper.company_URL(ciks, head)
                for x in self.webscraper.yearly_filings(soup, head):
                    if 'Directory List of /Archives/edgar/data/' not in x.text:
                        print(x.text.strip()[:3000])
            except Exception as ex:
                print(ex.with_traceback())
                print(ciks + " is not a valid integer value")
                valid = False
            finally:
                if len(ciks) != 10:
                    valid = False
                    print(ciks + " is not length 10")

        if valid:
            self.root.destroy()


        print(cik_numbers)
        x = SubmitPage()
        x.display_query(cik_numbers)
        x.make_window()

    def set_wordlist(self):
        try:
            word_list_title = self.word_list_start_variable.get()
            file_exists = os.path.exists(f"wordlist.txt")

            if file_exists:
                with open(f"wordlist.txt", "r") as f:
                    list = f.readline().split("[")
                    if word_list_title == list[0]:
                        self.word_list = list[1].replace(']', '').replace("'", "").split(',')
                        self.word_list = [x.strip() for x in self.word_list]

        except:
            print("You Must have a Word List Selected")


    def configure(self):
        configure_page = ConfigurePage()
        configure_page.make_window()
        self.update_word_list()


    def make_window(self):
        self.root.mainloop()

if __name__ == '__main__':
    application = SearchPage()
    application.make_window()

