from nltk import sent_tokenize
from nltk import word_tokenize
import regex as re
import requests
from bs4 import BeautifulSoup

class Parser():
    # makes usable regex from user-specified patterns
    def makelist(self, raw_list):
        return [term.replace('*', '\s*\w*\s*').strip() for term in raw_list]


    def get_item(self, soup):
        demo_string = soup.get_text().lower().replace(' ', '')
        #print(demo_string[500:8000])
        match_num = len(re.findall(r'item\s*1\s*[:.\-—]*\s*business\S*\s+(?=\D)\S', demo_string))
        iter_search = re.finditer(r'item\s*1\s*[:.\-—]*\s*business\S*\s+(?=\D)\S', demo_string)
        select = 0
        if match_num == 0:
            print("Could not find start of item 1")
        if match_num > 1:
            select = 1
        index = 0
        item_1 = None
        for match in iter_search:
            if index == select:
                item_1 = match
                break
            index = index + 1
        if item_1 is None:
            return None
        demo_string = demo_string[item_1.end()-1:]
        item_1a = re.search(r'item\s*1a\s*[\-:.—]*', demo_string)
        if item_1a is None:
            item_2 = re.search(r'i\s*t\s*e\s*m\s*2\s*[:.\-—]*[\s]*p\s*r\s*o\s*p\s*e\s*r\s*t\s*i\s*e\s*s\S*\s+(?=\D)\S', demo_string)
            if item_2 is None:
                print(f"End of Item 1 not found.")
                return None
            else:
                demo_string = demo_string[:item_2.start()]
                print(len(re.sub(r"\s+", ' ', demo_string)))
                print(demo_string[-500:])
                if len(demo_string) == 0:
                    print("Item located is empty")
                    return None
        else:
            demo_string = demo_string[:item_1a.start()]
            print(len(re.sub(r"\s+", ' ', demo_string)))
            print(re.sub(r"\s+", ' ', demo_string)[-500:])
            if len(re.sub(r"\s+", ' ', demo_string)) == 0:
                print("Item located is empty")
                return None
        return re.sub(r"\s+", ' ', demo_string)

    def get_term_frequency(self, text, term_list):
        # split into sentences for troubleshooting
        sentences = sent_tokenize(text)
        total_word_count = len(text.split())
        term_list = self.makelist(term_list)
        word_counts = self.getcount(regex_list=term_list, sentences=sentences)
        return total_word_count, word_counts


    def getcount(self, regex_list, sentences):
        count = 0
        for regex in regex_list:
            for sentence in sentences:
                if len(re.findall(regex, sentence)) != 0:
                    count = count + len(re.findall(regex, sentence))
        return count