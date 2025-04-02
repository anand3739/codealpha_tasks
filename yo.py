import tkinter as tk
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
from threading import Thread

class VoiceAssistantGUI:
    def __init__(self, master):
        self.master = master
        master.title("Python Voice Assistant")
        
        # Conversation display
        self.conversation = tk.Text(master, height=15, width=50)
        self.conversation.pack(pady=10)
        
        # Start/Stop Listening button
        self.btn_listen = tk.Button(master, text="Start Listening", command=self.toggle_listening)
        self.btn_listen.pack(pady=5)
        
        # Initialize speech engine and recognizer
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        self.is_listening = False

        # Greet the user initially
        self.speak("Hi, I am Buji gadu, made in Chennai")

    def speak(self, text):
        """Speak the given text and display it in the conversation window."""
        self.conversation.insert('end', f"Assistant: {text}\n")
        self.engine.say(text)
        self.engine.runAndWait()

    def toggle_listening(self):
        """Toggle listening on/off."""
        if not self.is_listening:
            self.is_listening = True
            self.btn_listen.config(text="Stop Listening")
            Thread(target=self.listen).start()
        else:
            self.is_listening = False
            self.btn_listen.config(text="Start Listening")

    def listen(self):
        """Continuously listen for commands."""
        with sr.Microphone() as source:
            while self.is_listening:
                try:
                    audio = self.recognizer.listen(source, phrase_time_limit=5)
                    command = self.recognizer.recognize_google(audio).lower()
                    self.conversation.insert('end', f"You: {command}\n")
                    self.handle_command(command)
                except sr.UnknownValueError:
                    self.speak("Sorry, I didn't catch that.")
                except sr.RequestError:
                    self.speak("Speech service unavailable.")

    def handle_command(self, command):
        """Handle the recognized command."""
        response = ""
        if "time" in command:
            response = f"The time is {datetime.datetime.now().strftime('%H:%M')}"
        elif "date" in command:
            response = f"Today's date is {datetime.datetime.now().strftime('%Y-%m-%d')}"
        elif "open" in command:
            website = command.replace("open", "").strip()
            response = self.open_website(website)
        elif "exit" in command:
            response = "Goodbye!"
            self.is_listening = False
            self.btn_listen.config(text="Start Listening")
        else:
            response = "Command not recognized"
        
        self.speak(response)

    def open_website(self, website):
        """Open the requested website in the default browser."""
        websites = {
            "youtube": "https://www.youtube.com",
            "google": "https://www.google.com",
            "github": "https://www.github.com",
            "wikipedia": "https://www.wikipedia.org",
            "define aura": "https://www.youtube.com/watch?v=In0DGTBQYu4",
            "arise": "https://youtu.be/3SH3I4lZIQE?si=JwgltnWKoQEsDUIb&t=79",
        }
        if website in websites:
            webbrowser.open(websites[website])
            return f"Opening {website}"
        else:
            return f"Sorry, I don't know how to open {website}"

# Main application
root = tk.Tk()
assistant_gui = VoiceAssistantGUI(root)
root.mainloop()