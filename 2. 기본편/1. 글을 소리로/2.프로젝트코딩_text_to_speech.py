from gtts import gTTS
from playsound import playsound
import time

lang = input('언어 선택 - 영어 또는 한국어를 입력해주세요. :')
condition = '영어' in lang or '한국어' in lang

while not condition:
    lang = input('잘못 입력하셨습니다. 언어 선택 - 영어 또는 한국어를 입력해주세요. :')
    condition = '영어' in lang or '한국어' in lang

if '영어' in lang:
    text = input("영어 문장을 입력하세요. : ")
    tts = gTTS(text=text, lang='en')

else:
    text = input("한국어 문장을 입력하세요. : ")
    tts = gTTS(text=text, lang='ko')

tts.save('read_text.mp3')
time.sleep(3)
playsound('read_text.mp3')
