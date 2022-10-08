import tkinter as tk
import datetime

class HomePage:

    def __init__(self):
        """
        This method sets up the GUI with the labels and buttons that make up the visual parts of the application.
        """

        self.root = tk.Tk()
        self.root.grid()
        self.padding = {'padx': 7, 'pady': 7}

        self.root.title("Data Scraping Tool")

        self.root.geometry("500x350")

        current_time = datetime.datetime.now()
        years = []
        for year in range(2001, current_time.year+1):
            years.append(year)

        self.word_list_button = tk.Button(self.root, text="Configure Word List", command=self.configure)
        self.analyze_button = tk.Button(self.root, text="Submit Query", command=self.analyze)
        self.search_bar = tk.Text(self.root, height=2, width=15)
        self.label_search = tk.Label(self.root, text="Search For 10-K Results")
        self.label_cik = tk.Label(self.root, text='CIK List (Comma Delimited)')
        self.label_date_start = tk.Label(self.root, text='Start Date')


        self.date_start_variable = tk.StringVar(self.root)

        self.date_start_variable.set(years[0])


        self.date_start_menu = tk.OptionMenu(self.root, self.date_start_variable, *years)


        self.hours_worked_text = tk.Text(self.root, height=1, width=5)

        self.label_search.place(x=(500/2)-60, y=10)
        self.label_cik.place(x=(500/2)-70, y=60)
        self.label_date_start.place(x=(500/2)-30, y=150)

        self.date_start_menu.place(x=(500/2)-30, y=170)

        self.analyze_button.place(x=(500/2)-90, y=310, width=200)
        self.search_bar.place(x=(500/2)-150, y=90, width=300, height=50)
        self.word_list_button.place(x=(500/2)-90, y=280, width=200)

        print(years)

    def analyze(self):
        pass

    def configure(self):
        pass

    def make_window(self):
        self.root.mainloop()


if __name__ == '__main__':
    application = HomePage()
    application.make_window()