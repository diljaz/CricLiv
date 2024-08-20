
import lxml
import requests
from bs4 import BeautifulSoup
import re
import time


link = f"https://www.cricbuzz.com/live-cricket-scores/59986"
source = requests.get(link).text
page = BeautifulSoup(source, "lxml")

page = page.find("div", class_="cb-col cb-col-67 cb-scrs-wrp")
matches = page.find_all(
    "div", class_="cb-min-bat-rw")
live_matches = []

for i in range(len(matches)):
    live_matches.append(matches[i].text)

print(live_matches[0])


