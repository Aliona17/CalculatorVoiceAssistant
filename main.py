import pyttsx3
import speech_recognition as sr
import re


def speak(text):   #This function is responsible for converting the given text into speech
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def listen():   #This function listens to the user's speech input using the microphone
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("say now!")
        audio = r.listen(source)

    try:
        print("Please waite...")
        query = r.recognize_google(audio)
        print("You said:", query)
        return query

    except sr.UnknownValueError:
        print("Sorry, I didn't understand.")
        return ""


def calculate(expression):  #This function takes a mathematical expression as input and evaluates it
    expression = re.sub('[^0-9+\-*/]', '', expression)
    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except:
        return "Error: Invalid expression"


def voice_calculator(): # This function represents the main logic of the voice assistant calculator
    started = False

    while True:
        if not started:
            query = listen()

            if "start" in query.lower():
                speak("Voice calculator started. How can I assist you?")
                started = True

        else:
            query = listen()

            if "calculate" in query.lower():
                expression = re.search(r'calculate (.+)', query.lower())
                if expression:
                    expression = expression.group(1)
                    result = calculate(expression)
                    speak("The result is: " + str(result))
                else:
                    speak("Please say again")

            elif "stop" in query.lower():
                speak("Voice calculator stopped. Goodbye!")
                break

            else:
                speak("Sorry, I can't help with that.")


voice_calculator()