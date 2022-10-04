import tkinter as tk
import tkinter.filedialog

class ExportPage:

    def __init__(self):
        """
        This method sets up the GUI with the labels and buttons that make up the visual parts of the application.
        """

        self.root = tk.Tk()
        self.root.grid()
        self.padding = {'padx': 7, 'pady': 7}

        self.root.title("Data Scraping Tool")

        self.root.geometry("300x120")

        self.export_new_button = tk.Button(self.root, text="Export to new file", command=self.export_new)
        self.export_existing_button = tk.Button(self.root, text="Export to existing file", command=self.export_existing)

        self.label_finish = tk.Label(self.root, text="Query and Analysis Complete")

        self.label_finish.place(x=(200/2)-30, y=10)
        self.export_new_button.place(x=(200/2)-50, y=50, width=200)
        self.export_existing_button.place(x=(200/2)-50, y=80, width=200)

    def export_new(self):
        path = tkinter.filedialog.askdirectory()
        self.outputDir = path

    def export_existing(self):
        self.path = tkinter.filedialog.askopenfilenames(title="Open File")
        for i in self.path:
            print(i)
        self.all_files = self.path

    def make_window(self):
        self.root.mainloop()


if __name__ == '__main__':
    application = ExportPage()
    application.make_window()