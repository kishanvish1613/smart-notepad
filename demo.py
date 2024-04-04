import speech_recognition as s


def take_query():
    sr = s.Recognizer()
    print("Say Something...")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            sr.adjust_for_ambient_noise(m, duration=5)
            text = sr.recognize_google(audio, language='hi-IN')
            return text
        except:
            print("Exception occurred")


print("you said:", take_query())
