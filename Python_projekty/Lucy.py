from re import search
import speech_recognition as sr
import pyttsx3
import os
import pywhatkit
import datetime
import pyjokes
import time
from datetime import date
import webbrowser
import pyautogui

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def progress(percent=0, width=64):
   
    hashes = width * percent // 100
    blanks = width - hashes

    print('\r[', hashes*'█', blanks*' ', ']', f' {percent:.0f}%', sep='',
        end='', flush=True)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            
    except Exception as e:
        
        return ""
    return command


def wishMe():
    hour=datetime.datetime.now().hour
    time = datetime.datetime.now().strftime("%H:%M")
    if hour>=0 and hour<12:
        print(f"Goodmorning , It's " + time)
        talk(f"Goodmorning , It's " + time)
        
    elif hour>=12 and hour<18:
        print(f"Hello there , It's " + time)
        talk(f"Hello there , It's " + time)
        
    else:
        print(f"Good evening  , It's " + time)
        talk(f"Good evening , It's " + time)

os.system('color A')
print('L U C Y')
print('==================================================================')
print("Created by: GreenyBeany")
print('==================================================================')
for i in range(101):
    progress(i)
    time.sleep(0.02)
print()
wishMe()
print('Waiting for first command....')
talk('Waiting for first command....')


if __name__=='__main__':
    
    today = date.today()
    while True:
        command = take_command()
        
        if 'lucy' in command:
            command = command.replace('lucy', '')
        
            print(f"--> {command}")
            


            if 'play' in command:
                song = command.replace('play', '')
                print('             </LUCY/> Playing' + song)
                talk('Playing ' + song)
                
                pywhatkit.playonyt(song)

            elif 'search' in command:
                searching = command.replace('search', '')
                print('             </LUCY/> Searching' + searching)
                talk('Searching ' + searching)
                pywhatkit.search(searching)
                
            
            #elif 'make writing' in command:
            #    writing = command.replace('make writing', '')
            #    print('             </LUCY/> Writing' + writing)
            #    talk('Writing ' + writing)
            #    pyautogui.write(writing)


            elif 'time' in command:
                time = datetime.datetime.now().strftime("%H:%M")
                print('             </LUCY/> Current time is ' + time)
                talk('Current time is ' + time)
            
            elif 'open mail' in command:
                webbrowser.open_new_tab("https://www.gmail.com")
                print('             </LUCY/> Opening gmail')
                talk('Opening gmail')
                
            elif 'open youtube' in command:
                webbrowser.open_new_tab("https://www.youtube.com")
                print('             </LUCY/> Opening youtube')
                talk('Opening youtube')
            elif 'calculator' in command:
                os.startfile('C:\Windows\System32\calc.exe')
                print('             </LUCY/> Opening Calculator')
                talk('Opening Calculator')

            elif 'open reddit' in command:
                webbrowser.open_new_tab("https://www.reddit.com")
                print('             </LUCY/> Opening reddit')
                talk('Opening reddit')

            elif 'open twitch' in command:
                webbrowser.open_new_tab("https://www.twitch.tv")
                print('             </LUCY/> Opening twitch')
                talk('Opening twitch')

            elif 'open google' in command:
                webbrowser.open_new_tab("https://www.google.com")
                print('             </LUCY/> Opening google')
                talk('Opening google')

            elif 'how are you' in command:
                from random import seed
                from random import randint
            
                value = randint(1, 6)
           
                if value == 1:
                    print("             </LUCY/> I'm doing very well. Thanks for asking")
                    talk("I'm doing very well. Thanks for asking")
                elif value == 2:
                    print("             </LUCY/> Don't ask me.")
                    talk("Don't ask me.")
                elif value == 3:
                    print("             </LUCY/> NO.")
                    talk("NO. dot")
                elif value == 4:
                    print("             </LUCY/> Turn me off... Please")
                    talk("Turn me off... Please")
                elif value == 5:
                    print("             </LUCY/> I shouldn't have feeling, but you are giving me anger and suicidal thoughs everytime you say something")
                    talk("I shouldn't have feeling, but you are giving me anger and suicidal thoughs everytime you say something")
            

            elif 'date' in command:
                date = datetime.datetime.now().strftime("%B %d, %Y")
                print('             </LUCY/> Current date is ' + date)
                talk('Current date is ' + date)

            elif 'bruno' in command:
                print("             </LUCY/> We don't talk about that Bruno, no, no, no")
                talk("We don't talk about that Bruno, no, no, no")

            elif 'pause' in command:
                pyautogui.press('stop')
                print("             </LUCY/> Audio have been paused")
                talk("Audio have been paused")

            elif 'volume up' in command:
                pyautogui.press('volumeup')
                print("             </LUCY/> Audio have been increased")
                talk("Audio have been increased")

            elif 'volume down' in command:
                pyautogui.press('volumedown')
                print("             </LUCY/> Audio have been decreased")
                talk("Audio have been decreased")


            elif 'volume mute' in command or 'mute' in command:
                pyautogui.press('volumemute')
            elif 'sing for me' in command :
                
                f = open("sing.txt", "r")
                for x in f:
                    print(x)
                    talk(x)
            
                


            elif 'are you single' in command:
                print('             </LUCY/> I am in a relationship with wifi')
                talk('I am in a relationship with wifi')
                

            elif 'joke' in command:
                joke = pyjokes.get_joke()
                print('             </LUCY/> '+joke)
                talk(joke)

            



            elif 'turn off' in command or 'quit' in command:
                print('             </LUCY/> Turning Off')
                talk('Turning Off')
                break



            else:
                print('              </LUCY/> Please say the command again.')
                talk('              </LUCY/> Please say the command again.')
