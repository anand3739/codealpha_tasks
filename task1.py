import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech and type (print) the response
def speak_and_type(text):
    print(text)  # This will type the response in the console
    engine.say(text)  # This converts text to speech
    engine.runAndWait()

# Function to listen to the user's voice input
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-US')
            print(f"User said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return ""

# Function to handle commands
def handle_command(command):
    if 'time' in command:
        current_time = datetime.datetime.now().strftime('%H:%M')
        speak_and_type(f"The current time is {current_time}")
    elif 'date' in command:
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
        speak_and_type(f"Today's date is {current_date}")
    elif 'hello' in command:
        speak_and_type("Hello! How can I assist you today?")
    elif 'exit' in command or 'quit' in command:
        speak_and_type("Goodbye!")
    elif 'instagram' in command:
        speak_and_type("Opening Instagram")
        webbrowser.open("https://www.instagram.com/")
    elif 'youtube' in command:
        speak_and_type("Opening YouTube")
        webbrowser.open("https://www.youtube.com/")
    elif 'google' in command:
        speak_and_type("Opening Google")
        webbrowser.open("https://www.google.co.in/")
    elif 'linkedin' in command:
        speak_and_type("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com/")
    elif 'salaar fights' in command:
        speak_and_type("Opening YouTube")
        webbrowser.open("https://www.youtube.com/results?search_query=salaar+fight+scene")
    else:
        speak_and_type("I'm sorry, I don't understand that command.")
    return False

# Main function to run the voice assistant
def main():
    speak_and_type("I am Aura, how can I help you?")
    while True:
        command = listen()
        if command:
            if handle_command(command):
                break

if __name__ == "__main__":
    main()
