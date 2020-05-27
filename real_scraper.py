from bs4 import BeautifulSoup
import requests
import os

URL = "https://real.edu.ee"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

with open(os.path.expanduser("titles.txt"), "r") as text_file:
    
    old_titles = text_file.read().split("\n")

    scrape_results = soup.find_all('h2', class_='home-news__title home-news__title--small')
    titles = [p.text.strip() for p in scrape_results]

    #check if any of them are new
    if old_titles[:3] != titles:
        #run the email script
        from sending_emails import send_confirmation
        send_confirmation(titles)
    
    text_file.close()

    text_file = open(os.path.expanduser("titles.txt"), "w")
    for title in titles:
        text_file.write(title+"\n")
    text_file.close()
