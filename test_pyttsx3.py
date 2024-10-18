import pyttsx3
import threading

engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_response(message):
    response = ollama.chat(model='tinyllama', messages=[
      {
        'role': 'user',
        'content': message,
      },
    ])

    resp = response['message']['content']
    print(resp)
    speak(response['message']['content'])


def listen_for_input():
    while True:
        message = input("Type a message: ")
        speak(message)
        # get_response(message)
threading.Thread(target=listen_for_input).start()
