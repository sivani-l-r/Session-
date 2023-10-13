import requests
from bs4 import BeautifulSoup

url = 'https://ktu.edu.in/eu/core/announcements.htm'

response = requests.get(url)
response_cnt = response.content

# print(response_cnt)

notifications = []
soup = BeautifulSoup(response_cnt,'html.parser')
def extract_notifications(soup):
    print("Extracting KTU Notifications... ")
    notifications = []

    # Find all <li> elements
    li_elements = soup.find_all('li')

    for li in li_elements:
        notification_text = ""
        b_element = li.find('b')

        if b_element:
            notification_text = b_element.text.strip()

        if notification_text:
            notifications.append(notification_text)

    return notifications

notifications = extract_notifications(soup)

for idx, notification in enumerate(notifications, start=1):
    print(f"{idx}. {notification}")