import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import datetime
import os
from configure_page import ConfigurePage
from threading import Thread
from text_parser import Parser
from webscraper import WebScraper
import time
import datetime as dt


class SubmitPage:

    def __init__(self, cik_nums, start_date, end_date, word_list, email):
        self.root = tk.Tk()
        self.padding = {'padx': 7, 'pady': 7}
        self.root.title("Data Scraping Tool")
        self.root.geometry("500x350")

        self.output_data = []
        self.cik_nums = cik_nums
        self.start_date = start_date
        self.end_date = end_date
        self.word_list = word_list
        self.email = email


        self.title_text = tk.Label(self.root, text="Querying EDGAR....")
        self.progress = tk.Label(self.root, text="Estimated Finish Time: ")
        self.query_button = tk.Button(self.root, text="", command=self.query)
        # self.title_bar = tk.Text(self.root, height=2, width=15)

        self.title_text.place(x=(500/2)-150, y=40, width=300, height=30)
        self.progress.place(x=(500/2)-160, y=150)
        # self.title_bar.place(x=(500/2)-120, y=90, width=250, height=150)
        self.p = Progressbar(self.root, orient="horizontal", length=250, mode="determinate")
        self.p.place(x=125, y=350-270)
        self.make_window()


    def calcRemainingTime(self, start, current, max):
        elapsed = time.time() - start
        estimated = (elapsed/current) * max
        finish = start + estimated
        finish = dt.datetime.fromtimestamp(finish)
        return finish

    def query(self):
        self.output_data = []
        webscraper = WebScraper()
        parser = Parser()
        valid = True
        cik_numbers = self.cik_nums
        cik_numbers = [cik.strip() for cik in cik_numbers]
        head = {'User-Agent': 'Georgia Southern University AdminContact@{self.email}'}
        print(self.word_list)
        print(cik_numbers)
        for ciks in cik_numbers:
            try:
                start = time.time()
                self.title_text.config(text=f"Now querying CIK: {ciks}")
                int(ciks)
                soup = webscraper.company_URL(ciks, head)
                self.p['value'] = 0
                self.root.update_idletasks()
                self.p.update()
                self.root.update()
                list_filings = webscraper.yearly_filings(soup)
                print(f"Length of list_filings: {len(list_filings)}")
                increments = 0
                for x in list_filings:
                    increments += 1
                    filings, dates = webscraper.scrape_filing(head, x, self.end_date, self.start_date)
                    times = self.calcRemainingTime(start, increments, len(list_filings))
                    now = dt.datetime.fromtimestamp(time.time())
                    delta = str(times - now)
                    hours, minutes, seconds = delta.split(":")
                    remaining_time = f"{hours} hour(s), {minutes} minute(s), {seconds[:2]} second(s)"



                    if filings == 0:
                        self.progress.config(text=f"Estimated Finish Time: {remaining_time}")
                        self.p['value'] += 100/len(list_filings)
                        self.root.update_idletasks()
                        self.p.update()
                        self.root.update()
                        continue
                    elif increments == len(list_filings):
                        self.p['value'] = 100
                        self.root.update_idletasks()
                        self.p.update()
                        self.root.update()
                    else:
                        self.p['value'] += 100/len(list_filings)
                        self.root.update_idletasks()
                        self.p.update()
                        self.root.update()

                    self.progress.config(text=f"Estimated Finish Time: {remaining_time}")
                    item = parser.get_item(filings)
                    if item == None:
                        print("Could not locate item, continuing to next document")
                        continue
                    total_word_count, matches = parser.get_term_frequency(item, self.word_list)
                    temp_date = dates.split('-')
                    reporting_date = f"12/31/{int(temp_date[0])-1}"
                    y = f"{temp_date[1]}/{temp_date[2]}/{temp_date[0]}"
                    self.output_data.append([ciks, "10-K (Annual report)", y, reporting_date, total_word_count, matches])

            except Exception as ex:
                #print(ex.with_traceback())
                pass

            finally:
                print(f"cik:{ciks} finished processing")

        try:
            self.root.destroy()
            self.root.quit()
        except:
            pass


    def get_output_data(self):
        return self.output_data

    def make_window(self):
        self.root.after(1000, self.query_button.invoke)
        self.root.mainloop()


if __name__ == '__main__':
    application = SubmitPage()
    application.make_window()