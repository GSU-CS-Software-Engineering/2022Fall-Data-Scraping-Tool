import requests 
import pandas as pd 
from bs4 import BeautifulSoup

class WebScraper:
    def company_URL(self, cik, head):
        endpoint = r"https://www.sec.gov/cgi-bin/browse-edgar"
    
        param_dict = {'action':'getcompany',
                    'CIK':cik,
                    'type':'10-k',
                    'owner':'exclude',
                    'output':''}

        response = requests.get(url = endpoint, params = param_dict, headers = head)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    
    def yearly_filings(self, soup, head):
        doc_table = soup.find_all('table', class_='tableFile2')
        base_url_sec = r"https://www.sec.gov"
        ten_k_soup = []
        for row in doc_table[0].find_all('tr')[0:]:
            cols = row.find_all('td')
            
            if len(cols) != 0:                  
                filing_date = cols[3].text.strip()
                filing_doc_href = cols[1].find('a', {'href':True, 'id':'documentsbutton'})       

                if filing_doc_href != None:
                    filing_doc_link = base_url_sec + filing_doc_href['href'] 

                    response = requests.get(filing_doc_link, headers = head)
                    soup = BeautifulSoup(response.content, "html.parser")
                    
                    doc_table_two = soup.find('table', class_="tableFile")
                    ten_k_row = doc_table_two.find_all('tr')[1]
                    ten_k_cols = ten_k_row.find_all('td')
                    ten_k_doc_href = ten_k_cols[2].find('a', {'href':True})
                    
                    if ten_k_doc_href != None:
                        ten_k_doc_link = base_url_sec + ten_k_doc_href['href']
                        ten_k_doc_link = ten_k_doc_link.replace('/ix?doc=', '')
                        response = requests.get(ten_k_doc_link, headers=head)
                        ten_k_soup.append(BeautifulSoup(response.content, 'html.parser'))

                    else:
                        ten_k_doc_link = 'no link'
                
                else:
                    ten_k_doc_link = 'no link'

                print(filing_date)
                print(ten_k_doc_link)
        return ten_k_soup

    if __name__ == "__main__":
        print("Enter cik:")
        cik = input().split(",")
        print("Enter your school email:")
        email = input()
        head = {'User-Agent': 'Georgia Southern University AdminContact@{email}'}
        soup = company_URL(cik, head)
        for x in yearly_filings(soup, head):
            print(x.text)
            