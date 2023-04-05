import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

load_dotenv()
PROXY = os.getenv("PROXY")
proxies = {
    "http": PROXY,
    "https": PROXY
}

headers = {
    'authority': 'searchmysite.net',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'dnt': '1',
    'origin': 'https://searchmysite.net',
    'referer': 'https://searchmysite.net/search/browse/',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

results = []

for pageNumber in range(1,5):
    data = 'sort=date_domain_added+desc&p=' + str(pageNumber)
    response = requests.post('https://searchmysite.net/search/browse/', headers=headers, data=data)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find_all("a", class_="result-link")
    links = [link["href"].replace("/search/?q=domain:", "") for link in links]
    results += links

results = list(set(results))  #remove duplicates
print(results)
print(len(results))