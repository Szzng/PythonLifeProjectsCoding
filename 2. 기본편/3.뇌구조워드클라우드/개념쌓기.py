from wordcloud import WordCloud
from matplotlib import pyplot as plt

words = {
    '가족': 10,
    '친구': 9,
    '뭐먹지': 8,
    '코딩': 7,
    '파이썬': 6,
    '놀궁리': 5,
    '졸리다': 4,
    '배고파': 1,
}

wordcloud = WordCloud(
    font_path=r"C:\Windows\Fonts\malgun.ttf",
    width=800,
    height=800,
    colormap='rainbow',
).generate_from_frequencies(words)

plt.figure(figsize=(10, 10))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
