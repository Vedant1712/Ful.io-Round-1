import requests
from bs4 import BeautifulSoup
import re

url = input("Enter the url\n")
res = requests.get(url)
mails = []
social_links = []
contact = []

soup = BeautifulSoup(res.content, 'html.parser')
links = soup.find_all('a', href=True)
phone_pattern = re.compile(r'^.*?[+(\s.\-/\d)]{5,30}$')
email_pattern = re.compile(r'^.*?([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4}))')

for link in links:
    if link["href"].find('facebook') != -1 or link["href"].find('linkedin') != -1 or link["href"].find(
            'twitter') != -1 or link["href"].find('instagram') != -1:
        social_links.append(link["href"])
    elif email_pattern.match(link["href"]):
        mails.append(link["href"].split(':')[1])
    elif phone_pattern.match(link["href"]):
        contact.append(link["href"].split(':')[1])

print("Social Links-")
for link in social_links:
    print(link)
print("Email/s-")
for link in mails:
    print(link)
print("Contact:")
for link in contact:
    print(link)
