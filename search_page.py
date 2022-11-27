import tkinter as tk
import datetime
import os
import requests
from configure_page import ConfigurePage
from webscraper import WebScraper
from text_parser import Parser
from threading import Thread
from warning_page import WarningPage
from submit_page import SubmitPage
import traceback

class SearchPage:

    def __init__(self, email):
        """
        This method sets up the GUI with the labels and buttons that make up the visual parts of the application.
        """

        self.root = tk.Tk()
        self.padding = {'padx': 7, 'pady': 7}
        self.root.title("Data Scraping Tool")
        self.root.geometry("500x350")
        self.word_list_selected = False


        self.email = email
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
                for list_title in f.readlines():
                    list_title = list_title.split("[")[0]
                    print(list_title)
                    if list_title not in self.word_list:
                        self.word_list.append(list_title)
                        self.word_list_menu['menu'].add_command(label=list_title, command=tk._setit(self.word_list_start_variable, list_title))

            self.word_list_start_variable.set(self.word_list[0])

    def analyze(self):

        head = {'User-Agent': self.email.strip()}
        analyze = True
        error_given = False
        self.set_wordlist()
        ciks = self.search_bar.get('1.0', 'end').split(',')
        cik_page = requests.get(url='https://www.sec.gov/Archives/edgar/cik-lookup-data.txt', headers=head)
        all_ciks = cik_page.content
        invalid_ciks = ""

        for cik in ciks:
            cik = cik.strip()
            try:
                int(cik)
                if cik not in str(all_ciks):
                    invalid_ciks = invalid_ciks + cik + " "
                    analyze = False
            except:
                wp = WarningPage(cik + " is not a valid integer value. Try again.")
                error_given = True
                analyze = False
            finally:
                if len(cik) != 10:
                    wp = WarningPage(cik + " is not a 10 digit CIK number. Try again.")
                    error_given = True
                    analyze = False
        if analyze:
            print("Word list: ")
            print(self.word_list)
            if self.word_list_selected:
                x = SubmitPage(ciks, self.date_start_variable.get(), self.date_end_variable.get(), self.word_list, self.email)
                self.output_data = x.get_output_data()
                self.root.destroy()
                self.root.quit()

        elif error_given:
            pass

        else:
            wp = WarningPage("Invalid CIK(s): " + invalid_ciks + " Please try again.")

    def get_output_data(self):
        return self.output_data

    def set_wordlist(self):
        word_list = False
        try:
            word_list_title = self.word_list_start_variable.get()
            file_exists = os.path.exists(f"wordlist.txt")

            if file_exists:
                with open(f"wordlist.txt", "r") as f:
                    for list in f.readlines():
                        list = list.split("[")
                        if word_list_title == list[0]:
                            self.word_list = list[1].replace(']', '').replace("'", "").split(',')
                            self.word_list = [x.strip() for x in self.word_list]
                            print("setting wordlist")
                            print(self.word_list)
                            word_list = True
                            self.word_list_selected = True

        except:
            traceback.print_exc()
            wp = WarningPage("You must have a word list selected.")
            word_list = True
            self.word_list_selected = False

        if not word_list:
            wp = WarningPage("You must have a word list selected.")
            self.word_list_selected = False



    def configure(self):
        configure_page = ConfigurePage()
        configure_page.make_window()
        self.update_word_list()



    def make_window(self):
        self.root.mainloop()

if __name__ == '__main__':
    application = SearchPage()
    application.make_window()

