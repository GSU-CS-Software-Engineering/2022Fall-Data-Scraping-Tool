import export_page as ep
import search_page as sp
from text_parser import Parser
'''
These lines may need to be added the first time the program is ran on a new machine in order to get the parser to run.
import nltk
pltk.download('punkt')
'''

parser = Parser()

home_page = sp.SearchPage()
home_page.make_window()


end_page = ep.ExportPage()
end_page.make_window()

parser.demo_parser()

