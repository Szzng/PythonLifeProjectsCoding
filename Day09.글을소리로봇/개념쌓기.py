from gtts import gTTS
from playsound import playsound
import time

text = "안녕하세요, 횡단보도에 녹색불이 켜졌습니다. 건너가도 좋습니다."
tts = gTTS(text=text, lang='ko')
tts.save('trafficlight.mp3')
time.sleep(5)
playsound('trafficlight.mp3')
