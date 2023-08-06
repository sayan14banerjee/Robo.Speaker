import win32com.client 
speakers = win32com.client.Dispatch("SAPI.SpVoice")

if __name__ == '__main__':
    print("Welcome to robo_speake 1.0. made by sayan ")
    while True:
        x=input("Enter what you want to speake: ")
        if x== "q":
            speakers.speak("Good bye friend.")
            break
        speakers.speak(x)