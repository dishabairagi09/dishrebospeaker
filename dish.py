import pyttsx3

if __name__ == "__main__":
    engine = pyttsx3.init()
    print("welcome to myspeaker created by disha")
    while True:
        text = input("Enter what you want to speak (or type 'exit' to stop): ")

        if text.lower() == "exit":
            print("exiting the speaker. bye bye")
            break
        engine.say(text)
        engine.runAndWait()