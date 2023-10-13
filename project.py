import requests
from bs4 import BeautifulSoup

url = 'https://statelibrary.kerala.gov.in/en/new-arrivals/'

response = requests.get(url) # connection set
response_cnt = response.content  # got the html code of that site

# print(response_cnt)

new_arrivals = ''

def extract_books(url):
    print("Extracting new arrivals... ")
    temp = ''
    response = requests.get(url)
    response_cnt = response.content
    soup = BeautifulSoup(response_cnt,'html.parser')

    td = soup.find_all('td')

    for i in td:
        text = i.text.strip()  # .text - text part of the html code print , .strip() - white space, extra space delete
        if text:
            temp += str(text) + '\n'

    return temp

new_arrivals= extract_books(url)
print(new_arrivals)