import export_page as ep
import search_page as sp
from text_parser import Parser

parser = Parser()

home_page = sp.SearchPage()
home_page.make_window()


end_page = ep.ExportPage()
end_page.make_window()

parser.demo_parser()

