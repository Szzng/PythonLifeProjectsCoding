# terminal을 열고, 필요한 라이브러리를 설치합니다.
# pip install selenium webdriver_manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

# 크롬 드라이버 설정
options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # 네이버 날씨 페이지 열기
    driver.get('https://weather.naver.com/')
    time.sleep(5)  # 페이지 로드를 기다립니다.

    # 현재 온도 가져오기
    current_temp = driver.find_element(By.CSS_SELECTOR, "strong.current").text

    # 오전, 오후 강수량 가져오기
    rainfall = driver.find_elements(By.CSS_SELECTOR, "span.rainfall")
    morning_rain = rainfall[0].text
    afternoon_rain = rainfall[1].text

    # 결과 출력
    result = '[오늘의 날씨]\n' + current_temp + '\n오전 ' + morning_rain + '\n오후 ' + afternoon_rain + '\n\n오늘 하루도 행복하세요. 화이팅!'
    print(result)
finally:
    driver.quit()  # 브라우저 종료
