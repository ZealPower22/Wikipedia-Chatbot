import speech_recognition as sr
import wikipedia
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set speech rate (optional)
engine.setProperty('rate', 150)

# Function to speak the response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech and convert to text
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for a command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing speech...")
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return None
    except sr.RequestError:
        print("Sorry, the service is unavailable.")
        return None

# Function to fetch information from Wikipedia
def get_wikipedia_info(query):
    try:
        summary = wikipedia.summary(query, sentences=3)  # Fetch a short summary
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Your query is ambiguous. Please be more specific. Possible options: {e.options}"
    except wikipedia.exceptions.HTTPTimeoutError:
        return "Sorry, Wikipedia service is taking too long. Please try again later."
    except wikipedia.exceptions.RedirectError:
        return "Sorry, the Wikipedia page redirects to another topic."
    except Exception as e:
        return f"Sorry, I couldn't fetch the information. Error: {e}"

# Main function
def chatbot():
    speak("Hello, how can I assist you today?")
    
    while True:
        command = listen()
        if command:
            command = command.lower()
            
            if "stop" in command or "exit" in command:
                speak("Goodbye! Have a great day!")
                break
            
            speak("Fetching information for you...")
            response = get_wikipedia_info(command)
            speak(response)
        else:
            speak("Please say something again.")

if __name__ == "__main__":
    chatbot()
