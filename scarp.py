import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.cricbuzz.com/cricket-match/live-scores")

soup = BeautifulSoup(req.content, "html.parser")
# res = soup.LiveScores
score_card = soup.find()
# print(soup.get_text())
print(score_card)
