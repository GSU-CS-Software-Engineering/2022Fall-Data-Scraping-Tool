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
continue_check = True
user_email = ""
while continue_check:

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

    parser = Parser()

    home_page = sp.SearchPage(user_email)
    home_page.make_window()


    end_page = ep.ExportPage()
    end_page.make_window()
    print(end_page.get_start_over())
    parser.demo_parser()
    if (not end_page.get_start_over()):
        continue_check = False

