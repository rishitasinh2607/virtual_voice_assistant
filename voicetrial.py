#gtts -->Google TexttoSpeech
import gtts
from gtts import gTTS
speech = gTTS("hello everyone how are you")
a = speech.save("greet.mp3")
