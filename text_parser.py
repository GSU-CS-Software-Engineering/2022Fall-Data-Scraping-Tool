from nltk import sent_tokenize
from nltk import word_tokenize
import regex as re
import requests
from bs4 import BeautifulSoup

class Parser():
    # makes usable regex from user-specified patterns
    TOC_count = 0
    NO_FIND = 0
    file_count = 0
    def makelist(self, raw_list):
        return [term.replace('*', '\s*\w*\s*').strip() for term in raw_list]


    def get_item(self, soup):
        self.file_count = self.file_count + 1
        print(self.file_count)
        demo_string = soup.get_text(separator='\n').replace(' ', '').replace('\&#160', '')
        backup = demo_string
        demo_string = re.search(r'(?:.*\n\s*)(item\s*1\s*[:.\-—]*\s*business\.*\s*\D*\n.*)(?:\nitem\s*(1a|2)\s*[:.\-—]*\s*(properties|risk\s*factors)\.*\s*\n.*)', demo_string, flags=re.IGNORECASE | re.DOTALL)
        print(type(demo_string))
        if demo_string is None:
            print("String does not match pattern: " + str(self.NO_FIND))
            with open("troubleshoot.txt", 'a') as file:
                file.write("NO MATCH" + str(self.NO_FIND) + "\n" + backup)
                self.NO_FIND = self.NO_FIND + 1
        elif len(demo_string.group(1)) < 1000:
            print("Parser may have detected TOC instead, writing to file: " + str(self.TOC_count))
            with open("troubleshoot.txt", 'a') as file:
                file.write("TOC ERROR " +str(self.TOC_count) + "\n" + demo_string.group(1))
                self.TOC_count = self.TOC_count + 1
        else:
            demo_string = demo_string.group(1)
            print(re.sub(r"\s+", ' ', demo_string)[:1000])
            print(re.sub(r"\s+", ' ', demo_string)[-1000:])
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