import speech_recognition as sr
from selenium.webdriver import ActionChains 
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
from gtts import gTTS 
import os
import pyttsx3 

r = sr.Recognizer()                                                                                         #To recognize speech
with sr.Microphone() as source:                                                                             #Microphone is considered as the source
    print("Talk")                   
    audio_text = r.listen(source)                                                                           #Speech is stored in variable: audio_text
    print("Time over, thanks")
    
#recoginize_() method will throw a request error if the API is unreachable, hence exception handling is done
    
    try:
        print("Text: "+r.recognize_google(audio_text))                                                      #using google's SpeechRecognition API
    except:
         print("Sorry, I did not get that")

    K = r.recognize_google(audio_text)                                                                      #After conversion, the text recognised is stored in another var K.
    L = K.split(" ")                                                                                        #The string is split to store keywords (Amount, To, From) separately.
    Amount, From, To = L[0], L[1], L[3]                                                                     #L[0],L[1] and L[3] are stored in variables: Amount, From and To respectively

    driver = webdriver.Chrome("C:\Users\DHRUVI\Desktop\Currency convertor\chromedriver.exe")            
    URL = "https://www.xe.com/currencyconverter/convert/?Amount=" + Amount + "&From=" + From + "&To=" + To  #Amount, To and From values are added in the URL.
    driver.get(URL)                                                                                         #xe.com is opened
    elements = driver.find_elements_by_xpath('//*[@id="converterResult"]/div/div/div[2]/span[1]')           #The converted amount is stored as an object.
    content = "".join([element.text for element in elements])                                               #The amount is accessed digit-by-digit by element.text() and then joined.
    text = content + " " + To                                                                               #stores input in the form of amount +" "+ currency  
    driver.quit()                                                                                           #Close browser
    
    # The converted amount is read aloud by the system 
    engine = pyttsx3.init()                                                                                 #call the pyttsx library (python text to speech library)
    engine.say(content + " " + To)                                                                          #System converts text to speech without opening external software.
    engine.runAndWait()                                                                             
