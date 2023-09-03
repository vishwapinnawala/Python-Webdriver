from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import speech_recognition as sr
import time
import pyttsx3
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
options.add_argument("disable-infobars")
options.add_argument("--kiosk")
driver = webdriver.Chrome('C:\\Users\vishw\\Desktop\\voice-assistant-main\\chromedriver.exe',chrome_options=options)

#driver.maximize_window()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
driver.get('http://testmirror.c1.biz/')

recognizer = sr.Recognizer()
microphone = sr.Microphone()

def speak(query):
    engine.say(query)
    engine.runAndWait()

def recognize_speech():
    with microphone as source:
        audio = recognizer.listen(source, phrase_time_limit=5)
    response = ""
    speak("Identifying speech..")
    try:
        response = recognizer.recognize_google(audio)
    except:
        response = "Error"
    return response
time.sleep(3)

speak("Hello Vishwa! I am now online..")

while True:
    speak("How can I help you?")
    voice = recognize_speech().lower()
    print(voice)
    if 'open dashboard' in voice:
        speak('Opening Dashboard..')        
        driver.get('http://testmirror.c1.biz/index.php')
    elif 'open camera' in voice:
        speak('Opening CCTV Feed..')        
        driver.get('http://testmirror.c1.biz/camera.php')
    elif 'open news' in voice:
        speak('Opening News Headlines..')        
        driver.get('http://testmirror.c1.biz/news.php')
    elif 'turn light on' in voice:
        speak('Turning Room Lights On..')        
        driver.get('http://testmirror.c1.biz/lightson.php')
    elif 'turn lights on' in voice:
        speak('Turning Room Lights On..')        
        driver.get('http://testmirror.c1.biz/lightson.php')
    elif 'turn light off' in voice:
        speak('Turning Room Lights Off..')        
        driver.get('http://testmirror.c1.biz/lightsoff.php')
    elif 'turn lights off' in voice:
        speak('Turning Room Lights Off..')        
        driver.get('http://testmirror.c1.biz/lightsoff.php')

        
    elif 'open google' in voice:
        speak('Opening google..')
        
        #driver.execute_script("window.open('');")
        #window_list = driver.window_handles
        #driver._switch_to.window(window_list[-1])
        
        driver.get('https://google.com')
    elif 'search google' in voice:
        while True:
            speak('Tell what to Search..')
            query = recognize_speech()
            if query != 'Error':
                break
        query=str(query)
        element = driver.find_element("name", "q")
        element.clear()
        element.send_keys(query)
        element.send_keys(Keys.RETURN)
    elif 'open youtube' in voice:
        speak('Opening youtube..')
        driver.get('https://youtube.com')
    elif 'search youtube' in voice:
        while True:
            speak('Tell what to Search..')
            query = recognize_speech()
            if query != 'Error':
                break
        element = driver.find_element("name", "search_query")
        element.clear()
        element.send_keys(query)
        element.send_keys(Keys.RETURN)
    
    elif 'open mirror' in voice:
        speak('Opening Mirror..')
        driver.execute_script("window.open('');")
        window_list = driver.window_handles
        driver._switch_to.window(window_list[-1])
        driver.get('http://testmirror.c1.biz')
    elif 'switch tab' in voice:
        num_tabs = len(driver.window_handles)
        cur_tab = 0
        for i in range(num_tabs):
            if driver.window_handles[i] == driver.current_window_handle:
                if i != num_tabs - 1:
                    cur_tab = i + 1
                    break
        driver._switch_to.window(driver.window_handles[cur_tab])
    elif 'close tab' in voice:
        speak('Closing Tab..')
        driver.close()
    elif 'go back' in voice:
        driver.back()
    elif 'go forward' in voice:
        driver.forward()
    elif 'exit' in voice:
        speak('Goodbye Master!')
        driver.quit()
        break
    else:
        speak('Not a valid command. Please try again.')
    time.sleep(2)