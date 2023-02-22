from bs4 import BeautifulSoup
import requests


def create_soup(url):
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/86.0.4240.183 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup


gilbut_url = "https://www.gilbut.co.kr/"
soup = create_soup(gilbut_url)

site_name = soup.find("h1", "sitename").get_text()

tabs = soup.find("div", "gnb").find_all("li")
tablist = []
for tab in tabs:
    tablist.append(tab.find("a").get_text())

print(f"{site_name}의 탭 목록은 {tablist} 입니다.")
