from wordcloud import WordCloud  # 이 패키지는 말그대로 워드클라우드를 생성에 필요한 기본 모듈입니다.
import matplotlib.pyplot as plt  # 생성한 워드클라우드 데이터를 시각화하여 그리기 위해 불러옵니다.

words = {
    '가족': 10,
    '친구': 9,
    '집': 8,
    '아이유': 7,
    '방탄소년단': 6,
    '파이썬': 5,
}

wordcloud = WordCloud(
    font_path='/Library/Fonts/AppleGothic.ttf',  # 한글 글씨체 설정
    width=800,
    height=800,
    colormap='rainbow',  # 단어색
).generate_from_frequencies(words)

# 사이즈 설정 및 출력
plt.figure(figsize=(10, 10))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
# plt.savefig('test.png')
