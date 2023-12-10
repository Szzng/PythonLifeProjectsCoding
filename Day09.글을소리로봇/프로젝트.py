from gtts import gTTS
from playsound import playsound
import time

lang = input('언어 선택 - 영어 또는 한국어를 입력해주세요. :')

while '영어' not in lang and '한국어' not in lang:
    lang = input('잘못 입력하셨습니다. 언어 선택 - 영어 또는 한국어를 입력해주세요. :')

if '영어' in lang:
    text = input("영어 문장을 입력하세요. : ")
    tts = gTTS(text=text, lang='en')

else:
    text = input("한국어 문장을 입력하세요. : ")
    tts = gTTS(text=text, lang='ko')

tts.save('speech.mp3')
time.sleep(5)
playsound('speech.mp3')
