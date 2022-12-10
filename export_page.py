import datetime
import tkinter as tk
import tkinter.filedialog
import csv

class ExportPage:

    def __init__(self, frequency_data):
        """
        This method sets up the GUI with the labels and buttons that make up the visual parts of the application.
        """
        self.frequency_data = frequency_data
        self.outputDir = ""

        self.root = tk.Tk()
        self.root.grid()
        self.padding = {'padx': 7, 'pady': 7}
        self.start_over = False

        self.root.title("Data Scraping Tool")

        self.root.geometry("300x120")

        self.export_new_button = tk.Button(self.root, text="Export to new file", command=self.export_new)
        self.export_existing_button = tk.Button(self.root, text="Export to existing file", command=self.export_existing)
        self.return_to_search_button = tk.Button(self.root, text = "Return to Search Page (Don't save results of query)", command=self.return_to_start)

        self.label_finish = tk.Label(self.root, text="Query and Analysis Complete")

        self.label_finish.place(x=(200/2)-30, y=5)
        self.return_to_search_button.place(x=(200/2)-90, y=25, width=280)
        self.export_new_button.place(x=(200/2)-90, y=55, width=280)
        self.export_existing_button.place(x=(200/2)-90, y=85, width=280)

    def return_to_start(self):
        self.start_over = True
        self.root.destroy()

    def export_new(self):
        current_time = datetime.datetime.now()
        self.path = tkinter.filedialog.askdirectory()
        self.outputDir = self.path + f"/{current_time.month}-{current_time.day}-{current_time.year}-WordFrequencyData.csv"
        if self.path != "":
            f = open(self.outputDir, 'w')
            writer = csv.writer(f, lineterminator='\n')
            headers = ["cik", "form", "filed", "reporting for",  "word count section 1",	"word count from list"]
            writer.writerow(headers)
            for row in self.frequency_data:
                writer.writerow(row)
            self.root.destroy()

    def export_existing(self):
        self.path = tkinter.filedialog.askopenfilenames(title="Open File")
        if self.path != "":
            f = open(self.path[0], "a")
            writer = csv.writer(f, lineterminator='\n')
            for row in self.frequency_data:
                writer.writerow(row)

            self.root.destroy()

    def get_start_over(self):
        return self.start_over

    def make_window(self):
        self.root.mainloop()



if __name__ == '__main__':
    application = ExportPage()
    application.make_window()