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
        demo_string = soup.get_text(separator=' ').lower().replace(' ', '')
        item_1 = re.search(r'i\s*t\s*e\s*m\s*1[:.][\s]*b\s*u\s*s\s*i\s*n\s*e\s*s\s*s\S*\s+(?=\D)\S', demo_string)
        if item_1 is None:
            print(f"Item 1 not found, printing demo string: {demo_string}")
        demo_string = demo_string[item_1.end()-1:]
        item_2 = re.search(r'i\s*t\s*e\s*m\s*2[:.][\s]*p\s*r\s*o\s*p\s*e\s*r\s*t\s*i\s*e\s*s\S*\s+(?=\D)\S', demo_string)
        if item_2 is None:
            print(f"Item 2 not found, printing demo string: {demo_string}")
        demo_string = demo_string[:item_2.start()]
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