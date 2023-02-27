from urllib.request import urlopen

from bs4 import BeautifulSoup

url="https://www.meetup.com/denver-metal-music-meetup/events/"

page=urlopen(url)
html_data = page.read().decode("utf-8")
soup = BeautifulSoup(html_data, "html.parser")
for show in soup.find_all('div', class_='eventCardHead'):
    bands = show.find('a', class_='eventCardHead--title')
    print(bands.text)
    for date_and_time in show.find('div', class_='text--labelSecondary'):
        date_and_time_text = date_and_time.text
        date_and_time_text = date_and_time_text.replace('UTC', 'MST')
        print(date_and_time_text)
        break
