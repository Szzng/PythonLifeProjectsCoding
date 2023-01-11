from wordcloud import WordCloud  # 이 패키지는 말그대로 워드클라우드를 생성에 필요한 기본 모듈입니다.
import matplotlib.pyplot as plt  # 생성한 워드클라우드 데이터를 시각화하여 그리기 위해 불러옵니다.
import numpy as np  # 불러온 그림을 배열로 나타내어 쉽게 처리할 수 있도록 도와주는 패키지입니다.
from PIL import Image  # 워드클라우드를 원하는 형태로 그리기 위해 그림을 불러오는 패키지

words = {
    '가족': 100,
    '친구': 95,
    '집': 88,
    '아이유': 90,
    '방탄소년단': 85,
    '파이썬': 80,
    '용돈': 70,
    '게임': 61,
    '코딩': 59,
    '웹툰': 55,
    '자유시간': 57,
    '학교': 54,
    '개그 욕심': 68,
    '꿈': 60,
    '돈': 59,
    '여행': 21,
    '먹고싶다': 19,
    '카카오톡': 48,
    '인스타그램': 41,
    '공부': 40,
    '스마트폰': 39,
    '디즈니': 35,
    '지브리': 35,
    '핫초코': 30,
    '과자': 28,
    '졸림': 25,
    '스트레스': 23,
    '놀궁리': 17,
    '자바스크립트': 15,
    '시험': 10,
    '배고파': 7,
    '디저트': 6,
    '꿀잼': 20
}
brainImage = np.array(Image.open('brain.png'))

wordcloud = WordCloud(
    font_path='/Library/Fonts/AppleGothic.ttf',  # 한글 글씨체 설정
    width=800,
    height=800,
    background_color='white',  # 배경색 (기본은 black)
    colormap='rainbow',  # 단어색
    mask=brainImage,
    contour_width=5,  # contour 윤곽
    contour_color='steelblue',
).generate_from_frequencies(words)

# 사이즈 설정 및 출력
plt.figure(figsize=(10, 10))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
# plt.savefig('test.png')
