# 네이버 날씨 사이트가 바뀌며 현재는 작동하지 않는 코드: 프로젝트(NEW).py로 대체

# from bs4 import BeautifulSoup
# import requests
#
# url = "https://weather.naver.com/"
# res = requests.get(url)
# soup = BeautifulSoup(res.text, "lxml")
#
# current_temp = soup.find("strong", "current").get_text()
# rainfall = soup.find_all("span", "rainfall", limit=2)
# morning_rain = rainfall[0].get_text()
# afternoon_rain = rainfall[1].get_text()
#
# result = '[오늘의 날씨]\n' + current_temp + '\n오전 ' + morning_rain + '\n오후 ' + afternoon_rain + '\n\n오늘 하루도 행복하세요. 화이팅!'
# print(result)