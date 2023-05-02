from wordcloud import WordCloud
from matplotlib import pyplot as plt

words = {
    '파이썬': 10,
    '가족': 8,
    '뭐먹지': 8,
    '코딩': 7,
    '친구': 6,
    '놀궁리': 5,
    '졸리다': 4,
    '배고파': 2,
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
