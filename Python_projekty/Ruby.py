import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import os
import pyautogui
import requests
import translator
import time
import random
import pyfiglet
import smtplib
from bs4 import BeautifulSoup
import serial
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Change the serial port to match your Arduino's port
ser = serial.Serial('COM4', 9600)
# Initialize the text-to-speech engine
engine = pyttsx3.init()
os.system('mode con: cols=130 lines=35')
os.system('color b')
# Set the voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def get_weather():
    # specify the website to scrape
    url = 'https://www.foreca.sk/Slovakia/Ruzomberok?quick_units=metric'

    # make a GET request to the website and get the HTML content
    response = requests.get(url)
    content = response.content

    # use Beautiful Soup to parse the HTML content
    soup = BeautifulSoup(content, 'html.parser')

    # get the current temperature and weather condition from the parsed content
    temp = soup.find('span', {'class':'txt-xxlarge'}).text.split()[0]
    
    cond = soup.find('div', {'class':'txt-tight'}).text.split()[0]

    # return the temperature and weather condition as a string
    return f"The current temperature is {temp} Celsius and the weather is {cond}"
# Define the talk function to speak the text
def talk(text):
    ser.write(text.encode() + b'\n')
    engine.say(text)
    engine.runAndWait()
    
    time.sleep(2)
def set_volume_percent(volume_percent):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    # Get the current volume range
    min_volume, max_volume, _ = volume.GetVolumeRange()
    
    # Calculate the volume level based on the percentage
    target_volume = (max_volume - min_volume) * (volume_percent / 100.0) + min_volume

    # Set the volume to the calculated level
    volume.SetMasterVolumeLevelScalar(target_volume, None)
# Define the listen function to listen for the user's command
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('   </RUBY/> Listening...')
        r.pause_threshold = 0.5
        audio = r.listen(source)

        try:
            print('   </RUBY/> Recognizing...\n')
            command = r.recognize_google(audio, language='en-us')
            print(f"   <USER>: {command}\n")
        except:
            
            return "None"

        return command.lower()
def wishMe():
    hour=datetime.datetime.now().hour
    time = datetime.datetime.now().strftime("%H:%M")
    if hour>=0 and hour<12:
        print(f"   </RUBY/> Goodmorning, It's " + time)
        talk(f"Goodmorning , It's " + time)
        
    elif hour>=12 and hour<18:
        print(f"   </RUBY/> Hello there, It's " + time)
        talk(f"Hello there , It's " + time)
        
    else:
        print(f"   </RUBY/> Good evening, It's " + time)
        talk(f"Good evening , It's " + time)
# Start the voice assistant
print(pyfiglet.figlet_format('                                                       RUBY'))
wishMe()


weather_info = get_weather()
print(f'   </RUBY/> {weather_info}')
talk(f'{weather_info}')


open('reminders.txt', 'a')
with open('reminders.txt', 'r') as f:
    reminders = f.read()
    if reminders:
        print('   </RUBY/> Here are your reminders:')
        talk('Here are your reminders:')
        i = -1
        for i, reminder in enumerate(reminders.split('\n')):
            print('            ' + str(i+1) + ': ' + reminder)
            talk(str(i+1) + ': ' + reminder)
    else:
        print('   </RUBY/> You have no reminders')
        talk('You have no reminders')












# Run the voice assistant indefinitely
while True:
    command = listen()

    if 'play' in command:
        song = command.replace('play', '')
        print('   </RUBY/> Playing ' + song)
        talk('Playing ' + song)
        pywhatkit.playonyt(song)

    elif 'who is' in command or 'what is' in command or 'what was' in command or 'who was' in command:
        pywhatkit.search(command)
        print('   </RUBY/> Results for '+command)
        talk('results for '+command)

    elif 'search' in command:
        searching = command.replace('search', '')
        print('   </RUBY/> Searching ' + searching)
        talk('Searching ' + searching)
        pywhatkit.search(searching)

    #elif 'make writing' in command:
    #    writing = command.replace('make writing', '')
    #    print('   </RUBY/> Writing ' + writing)
    #    talk('Writing ' + writing)
    #    pyautogui.write(writing)

    elif 'time' in command:
        time = datetime.datetime.now().strftime("%H:%M")
        print('   </RUBY/> Current time is ' + time)
        talk('Current time is ' + time)

    elif 'set volume' in command:
        volume = command.replace('set volume', '')
        set_volume_percent(int(volume))
        print('   </RUBY/> Volume set to ' + volume)
        talk('Volume set to' + volume)

    elif 'open my mail' in command:
        webbrowser.open_new_tab("https://www.gmail.com")
        print('   </RUBY/> Opening gmail')
        talk('Opening gmail')

    elif 'open github' in command:
        webbrowser.open_new_tab("https://github.com/Gymoblig")
        print('   </RUBY/> Opening GitHub')
        talk('Opening git hub')
    elif 'open youtube' in command:
        webbrowser.open_new_tab("https://www.youtube.com")
        print('   </RUBY/> Opening youtube')
        talk('Opening youtube')

    elif 'calculator' in command:
        os.startfile('C:\Windows\System32\calc.exe')
        print('   </RUBY/> Opening Calculator')
        talk('Opening Calculator')

    elif 'open notion' in command:
        #os.startfile('C:\Users\MATÚŠ\AppData\Local\Programs\Notion\Notion.exe')
        print('   </RUBY/> Opening Notion')
        talk('Opening Notion')
    
    elif 'open reddit' in command:
        webbrowser.open_new_tab("https://www.reddit.com")
        print('   </RUBY/> Opening reddit')
        talk('Opening reddit')

    elif 'open twitch' in command:
        webbrowser.open_new_tab("https://www.twitch.tv")
        print('   </RUBY/> Opening twitch')
        talk('Opening Twitch')

    elif 'weather' in command:
        result_weather = get_weather()
        print(f'   </RUBY/> {result_weather}')
        talk(f'{result_weather}')
    elif 'intruder' in command:
        webbrowser.open_new_tab("https://youtu.be/ekY09M48Jvs?si=9sqcAh8SyDLMr_ND&t=82")
        talk('You picked wrong house mother fucker')


    elif 'news' in command:
        news_url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=66f947000e33471aac91d214465bd86c"
        response = requests.get(news_url)
        data = response.json()
        articles = data['articles'][:5]
        for index, article in enumerate(articles):
            print('   </RUBY/> Headline {}: {}'.format(index + 1, article['title']))
            talk('Headline {}: {}'.format(index + 1, article['title']))


    

    elif 'tell me a story' in command or 'another story' in command:
       # Define a list of story introductions
        story_introductions = [
    'Once upon a time, there was a ',
    'Long ago, in a faraway land, there lived a ',
    'In a magical kingdom, there was a ',
    'In a small village, there lived a ',
]

# Define a list of character descriptions
        character_descriptions = [
    'brave knight',
    'wise wizard',
    'cunning thief',
    'fierce dragon',
    'beautiful prince',
    'valiant soldier',
    'clever detective',
    'mysterious stranger',
]

# Define a list of character actions
        character_actions = [
    'that set out on a quest to',
    'that embarked on a journey to',
    'that set off on a mission to',
    'that ventured into the unknown to',
]
        quest = [
     'save the kingdom,',
     'steal the rose of life,',
     'marry the most gorgerous girl in the whole world',
     'find meaning of death',
     'slay the dragon of Gondur',

]
# Define a list of plot twists
        plot_twists = [
    'but he soon encountered an unexpected obstacle.',
    'but he quickly realized that the task was much more difficult than he was thinking',
    'but he were not prepared for the challenges that lay ahead.',
    'but he were betrayed by someone he thought he could trust.',
    'but he discovered a shocking secret that changed everything.',
    'but he stumbled upon a hidden treasure that was guarded by a powerful enemy.',
]

# Define a list of story cores
        story_cores = [
    'He battled his way through dangerous territory, overcoming many obstacles along the way.',
    'He used all his cunning and skill to navigate the treacherous landscape.',
    'Despite the odds against them, he remained steadfast in his mission and persevered.',
    'He faced his fears and conquered them, emerging stronger than ever before.',
    'He learned valuable lessons along the way, gaining wisdom and experience that would serve him well in the future.',
]

# Define a list of story conclusions
        story_conclusions = [
    'In the end, he emerged victorious and returned home as hero.',
    'Although he did not achieve his original goal, he learned an important lesson along the way.',
    'His journey was long and difficult, but in the end, he found what he was searching for.',
    'He realized that sometimes the journey is more important than the destination.',
    'He formed strong mind with discipline and even stronger will that helped him achieve his true destiny',
    'He discovered that true love and courage can conquer all obstacles.',
]

# Generate a random story
        intro = random.choice(story_introductions)
        character = random.choice(character_descriptions)
        action = random.choice(character_actions)
        plot_twist = random.choice(plot_twists)
        core = random.choice(story_cores)
        conclusion = random.choice(story_conclusions)
        quests = random.choice(quest)

        story = intro + character + ' ' + action + ' ' + quests + ' ' + plot_twist + ' ' + core + ' ' + conclusion

        # Print the story
        print(f'   </RUBY/> {story}')
        talk(story)


    elif 'fact' in command:
        fact_url = "https://uselessfacts.jsph.pl/random.json?language=en"
        response = requests.get(fact_url)
        data = response.json()
        fact = data['text']
        print('   </RUBY/> Did you know that ' + fact)
        talk('Did you know that ' + fact)


#    elif 'translate' in command:
#                try:
#                    from_lang = command.split(' ')[-2]
#                    to_lang = command.split(' ')[-1]
#                    text = command.replace(f'translate {from_lang} {to_lang} ', '')
#                    translation = translator.translate(text, src=from_lang, dest=to_lang).text
#                    print(f'   </RUBY/> {text} ({from_lang.title()}) translates to {translation} ({to_lang.title()})')
#                    talk(f'{text} ({from_lang.title()}) translates to {translation} ({to_lang.title()})')
#                except:
#                    print("   </RUBY/> Unable to translate")
#                    talk("Unable to translate")
            
    elif 'calculate' in command:
                try:
                    expression = command.replace('calculate ', '')
                    result = str(eval(expression))
                    print(f'   </RUBY/> {expression} = {result}')
                    talk(f'{expression} equals {result}')
                except:
                    print("   </RUBY/> Unable to calculate")
                    talk("Unable to calculate")

    elif 'who are you' in command:
                print('   </RUBY/> I am RUBY, a virtual assistant created by Matthew')
                talk('I am RUBY, a virtual assistant created by Matthew')
    
    #elif 'wait' in command:
        #print("   </RUBY/> For how long?")
        #talk("for how long?")
        #time = listen()
        #while True:
            #if 'seconds' in time:
            #    seconds = int(time.replace('', 'seconds'))
            #print(f"   </RUBY/> Okay, now I'll wait for {seconds}")
            #talk(f"Okay, now I'll wait for {seconds}")
            #time.sleep(seconds)

    elif 'set reminder' in command or 'set a reminder' in command:
        reminder = command.split('reminder', 1)[1]
        with open('reminders.txt', 'a') as f:
            f.write(reminder+'\n')
        print('   </RUBY/> Reminder set for ' + reminder)
        talk('Reminder set for ' + reminder)

    elif 'show reminders' in command or 'show me reminders' in command:
        with open('reminders.txt', 'r') as f:
            reminders = f.read()
        if reminders:
            print('   </RUBY/> Here are your reminders:')
            talk('Here are your reminders:')
            
            for i, reminder in enumerate(reminders.split('\n')):
                print('            ' + str(i+1) + ': ' + reminder)
                talk(str(i+1) + ': ' + reminder)
        else:
            print('   </RUBY/> You have no reminders')
            talk('You have no reminders')

    elif 'delete reminders' in command or 'delete the reminders' in command:
        open('reminders.txt', 'w').close()
        print('   </RUBY/> All reminders deleted')  
        talk('All reminders deleted')
    elif 'are you single' in command:
        print('   </RUBY/> I am in a relationship with wifi')
        talk('I am in a relationship with wifi')
    elif 'sing' in command or 'show me reminders' in command:
        with open('lyrics.txt', 'r') as f:
            song = f.read()            
        if song:
            print(f'   </RUBY/> {song}')
            talk(song)
            
        else:
            print('   </RUBY/> I have no song to sing')
            talk('I have no song to sing')
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print('   </RUBY/> '+joke+' HehAhEhaHe')
        talk(f'{joke} hehaihehahe')
    
    elif 'love you' in command:
        print("   </RUBY/> Aww that's sweet. I don't know any human emotions, but I love you too")
        talk("Aww that's sweet. I don't know any human emotions, but I love you too")
    elif 'like you' in command:
        print("   </RUBY/> Aww I can't define human emotions properly, but I like you too")
        talk("Aww I can't define human emotions properly, but I like you too")























    elif 'turn off' in command or 'quit' in command:
        print('   </RUBY/> Turning Off')
        talk('Turning Off                       ')
        #j=4
        #while j > 0:
        #    j = j-1
        #    print(f'                           {j}')
            
        #    talk(j)
        
        break