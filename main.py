import export_page as ep
import search_page as sp
import email_page as mp
from text_parser import Parser
import os
'''
These lines may need to be added the first time the program is ran on a new machine in order to get the parser to run.
import nltk
pltk.download('punkt')
'''

user_email = ""
while True:

    file_exists = os.path.exists(f"useremail.txt")
    if file_exists:
         with open(f"useremail.txt", "r") as f:
            user_email = f.readline()
    else:
        email_page = mp.EmailPage()
        email_page.make_window()
        user_email = email_page.get_user_email()

    if user_email == "":
        break

    home_page = sp.SearchPage(user_email)
    home_page.make_window()

    export_data = home_page.get_output_data()

    print(export_data)

    end_page = ep.ExportPage(export_data)
    end_page.make_window()

