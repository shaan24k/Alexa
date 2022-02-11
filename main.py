import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')  # Get all the voices
engine.setProperty('voice', voices[1].id)  # set it to second voice


def speak(text):
    engine.say(text)  # ask it to say the command
    print(text)
    engine.runAndWait()


def get_command():
    command = ''
    try:
        with sr.Microphone() as source:  # Use microphone
            print('Listening...')
            voice = listener.listen(source)  # listen to the source
            command = listener.recognize_google(voice)
            command = command.lower()  # convert to lower case
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)

    except:
        pass

    return command  # return command that we are saying


def run_alexa():  # To start alexa

    command = get_command()  # Get command
    if 'play' in command:  # To play music
        song = command.replace('play', '')
        speak('playing' + song)
        pywhatkit.playonyt(song)  # play it in youtube

    elif 'time' in command:  # To get the time
        time = datetime.datetime.now().strftime(
            '%I:%M %p')  # %H:%M for 24 hr format
        speak('Current time is ' + time)
        print(time)

    elif 'who is' in command:  # To use word wikipedia in command
        person = command.replace('who the hell is', '')
        try:
            info = wikipedia.summary(person, 1)
            speak(info)  # speak the information
            print(info)

        except:
            speak('Couldn\'t find ' + person)

    elif 'drink' in command:
        speak('sorry, I have a headache ')

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        speak(joke)
        print(joke)

    elif 'what is your name' in command:
        speak('My name is alexa')


if __name__=='__main__':
    speak('Hello, How can I help you? ')
    while True:
        try:
            run_alexa()  # Run it continuously

        except sr.UnknownValueError():
            listener = sr.Recognizer()
            continue