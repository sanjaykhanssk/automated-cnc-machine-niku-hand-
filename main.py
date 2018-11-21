import requests
from bs4 import BeautifulSoup as bs
import random
import urllib.request
from urllib.request import Request, urlopen
import json
import subprocess
import os
import speech_recognition as sr
#import win32com.client as comspeak
import pyautogui
import pyperclip
import time

#chat = comspeak.Dispatch("SAPI.SpVoice")

r = sr.Recognizer()
if __name__ == '__main__':

   num = [0, 1, 2, 6, 5, 4, 3]

   #chat.Speak("type something to draw")
   you_said1 = input("type something to draw:>")
   more_than_chat = you_said1.split(" ")
   you_said = '+'.join(more_than_chat)
   ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0", ]
   url = ("https://www.google.co.in/search?hl=en&site=imghp&tbm=isch&tbs=isz:l&q={}".format(you_said))
   # url = ("https://duckduckgo.com/?q={}&t=ffnt&atb=v102-2_f&iax=images&ia=images".format(you_said))
   #chat.Speak("started searching......")
   print("started searching......")
   headers = {"User-Agent": random.choice(ua)}
   #chat.Speak("headers found.....")
   print("headers found.....")
   #chat.Speak("requests sending")
   print("requests sending")
   #chat.Speak("it may take some seconds")
   print("it may take some seconds")
   req = requests.get(url, headers=headers)
   #chat.Speak("request accepted")
   print("request accepted")
   #
   html = req.content
   soup = bs(html, "lxml")
   print("getting images info")
   images = soup.find_all("div", {"class": "rg_meta notranslate"}, {"jsname='ik8THc'"})
   #chat.Speak("downloading images info")
   print("downloading images info:")
   images = [i.text for i in images]
   # print(images[0])
   images = [json.loads(i, strict=False) for i in images]
   #chat.Speak("targeting image")
   print("targeting image")
   no = random.choice(num)
   final_url = images[no]['ou']
   image_name = "{}.jpg".format(you_said1)
   data = urllib.request.urlretrieve(final_url, image_name)
   #chat.Speak("done..download finished")
   print("done..download finished")
   print("The name  of downloaded image is {}".format(image_name))
   print("image downloaded from " + final_url)
   # #chat.Speak("the image just downloaded and now iam going to open software called benbox and you just want to open image called {} and adjust the size and click green button".format(image_name))
   # print("the image just downloaded and now iam going to open software called benbox and you just want to open image called {} and adjust the size and click green button".format(image_name))
   #chat.Speak("opening software ")
   print("opening software   ")
   subprocess.Popen([r"D:\Program Files\Benbox\3.7.99\bin\benbox.exe"])
   time.sleep(8)
   locate = pyautogui.locateCenterOnScreen('ben1.png')
   image = str(image_name)
   pyautogui.click(locate)
   time.sleep(5)

   pyperclip.copy(image)

   pyautogui.hotkey('ctrl', 'v')
   pyautogui.press('enter')
   time.sleep(5)
   pyautogui.click(783, 492)
   time.sleep(3)

   for _ in range(1, 7):
      pyautogui.scroll(-10)

"""  with sr.Microphone() as source:
         mess="say something to draw"rajini.jpg

         print(mess)
         #chat.Speak(mess)
         r.adjust_for_ambient_noise(source)
         audio = r.listen(source)
         print("i may take few seconds")
    try:
         you_said=str(r.recognize_google(audio))
         print("You said: " + you_said)
    except sr.RequestError as e:
          print("Could not request results from Google Speech Recognition service; {0}".format(e))
"""
