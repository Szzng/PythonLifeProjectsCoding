from bs4 import BeautifulSoup
import requests
from gtts import gTTS
from playsound import playsound
import time


def create_soup(url):
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/86.0.4240.183 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup


# 미래에 주소나 태그, 클래스 이름 등이 변할 수 있으나, 방법을 안다면 전혀 걱정없음.
weather_url = "https://weather.naver.com/"
soup = create_soup(weather_url)

current_temp = soup.find("div", "weather_now").find("strong").get_text()
rainfall = soup.find_all("span", "rainfall", limit=2)
morning_rain = rainfall[0].get_text()
afternoon_rain = rainfall[1].get_text()

current_temp = float(current_temp.replace("현재 온도", "").replace("°", ""))
morning_rain = float(morning_rain.replace("강수확률", "").replace("%", ""))
afternoon_rain = float(afternoon_rain.replace("강수확률", "").replace("%", ""))

result = f"[오늘의 날씨]\n현재 온도 : {current_temp}˚, 강수확률 : 오전 {morning_rain}%, 오후 {afternoon_rain}%"
text = result + ' 입니다.'

if current_temp < -5:
    text += '오늘 날씨가 정말 추워요! 옷을 두껍게 입으세요!'
elif current_temp > 30:
    text += '오늘 날씨가 정말 더워요! 물을 많이 마시고, 햇빛에 많이 노출되지 않도록 주의하세요!'

if (morning_rain > 60) or (afternoon_rain > 60):
    text += '오늘은 비가 올 확률이 높아요! 우산을 챙기세요!'

text += ' 오늘 하루도 행복하세요!'
print(text)
tts = gTTS(text=text, lang='ko')
tts.save('weathercaster.mp3')
time.sleep(3)
playsound('weathercaster.mp3')