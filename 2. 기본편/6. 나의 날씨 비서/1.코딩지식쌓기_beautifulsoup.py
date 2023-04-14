from bs4 import BeautifulSoup
import requests

gilbut = "https://www.gilbut.co.kr/"
res = requests.get(gilbut)
soup = BeautifulSoup(res.text, "lxml")

site_name = soup.find("h1", "sitename").get_text()

tabs = soup.find("div", "gnb").find_all("li")
tablist = []
for tab in tabs:
    tablist.append(tab.find("a").get_text())

print(f"{site_name}의 탭 목록은 {tablist} 입니다.")
