import speech_recognition as sr
# from your_ai_model import YourAIModel 

def recognize_speech_and_interact_with_model():
    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()

    # Reading Microphone as source
    # listening the speech and store in audio_text variable
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print("Time over, thanks")

    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    try:
        # using google speech recognition
        print("Text: "+r.recognize_google(audio_text))
        text = r.recognize_google(audio_text)
    except:
         print("Sorry, I did not get that")
         return

    # Here you would interact with your AI model
    # model = YourAIModel()
    # result = model.predict(text)

    # And then you would display the result in VS Code
    # print(result)

if __name__ == "__main__":
    recognize_speech_and_interact_with_model()