from wordcloud import WordCloud
from matplotlib import pyplot as plt
import numpy as np  # 불러온 그림을 배열로 나타내어 쉽게 처리할 수 있도록 도와주는 패키지입니다.
from PIL import Image  # 워드클라우드를 원하는 형태로 그리기 위해 그림을 불러오는 패키지

words = {
    '가족': 100,
    '친구': 95,
    '집': 88,
    '심심해': 90,
    '졸리다': 85,
    '파이썬': 80,
    '용돈': 70,
    '게임': 61,
    '코딩': 59,
    '웹툰': 55,
    '자유시간': 57,
    '학교': 54,
    '개그욕심': 68,
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
    '떡볶이': 15,
    '시험': 50,
    '배고파': 67,
    '디저트': 6,
    '꿀잼': 20
}

brainimage = np.array(Image.open('brain.png'))

wordcloud = WordCloud(
    font_path=r"C:\Windows\Fonts\malgun.ttf",
    width=800,
    height=800,
    background_color='white',
    colormap='rainbow',
    mask=brainimage,
    contour_width=5,
    contour_color='steelblue',
).generate_from_frequencies(words)

plt.figure(figsize=(10, 10))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
