import requests 
import pandas as pd 
from bs4 import BeautifulSoup

# base URL for the SEC EDGAR browser
endpoint = r"https://www.sec.gov/cgi-bin/browse-edgar"

# make comma separated string of inputs into a list of CIK's
CIK = input()
CIKList = CIK.split(",")

# define our parameters dictionary
for i in CIKList:
    param_dict = {'action':'getcompany',
                'CIK':i,
                'type':'10-k',
                'owner':'exclude',
                'output':''}

# request the url, and then parse the response
    response = requests.get(url = endpoint, params = param_dict)
    soup = BeautifulSoup(response.content, 'html.parser')

# print urls containing all 10-K filings for each company
    print(i,":")
    print(response.url)