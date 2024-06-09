import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import re
import csv

base_url = ""
target_file = ""
all_data = {}
headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

def extract_emails(text, url):
    global all_data
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    for email in emails:
        if email not in all_data:
            all_data[email] = url
    
def get_all_urls(url):
    try:
        response = requests.get(url, headers=headers, timeout=2)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            print(url)
            extract_emails(soup.get_text(), url)
            
            links = soup.find_all('a', href=True)
            base_domain = urlparse(url).scheme + '://' + urlparse(url).netloc
            all_urls = []

            for link in links:
                href = link['href']
                absolute_url = urljoin(base_domain, href)
                all_urls.append(absolute_url)
            
            return all_urls
        else:
            return []
    except:
        pass

def write_to_csv():
    with open(target_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Email', 'URL'])
    
        for key, value in all_data.items():
            csv_writer.writerow([key, value])
    
def url_parser(url, route):
    if route > 0:
        all_urls = get_all_urls(url)
        if all_urls != None:
            for url in all_urls:
                url_parser(url, route - 1)

def main():
    global target_file
    global base_url
    if len(sys.argv) > 1:
        target_file = sys.argv[1]
    else:
        target_file = input("Enter target file: ")
    
    if len(sys.argv) > 2:
        base_url = sys.argv[2]
    else:
        base_url = input("Enter target url: ")
    url_parser(base_url, 2)
    write_to_csv()
    
    

if __name__ == "__main__":
    main()