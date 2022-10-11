import pyttsx3 as pyt
import speech_recognition as sr
import datetime
import os
import cv2
import random
import pywhatkit  # This method can be used to remotely control your PC using your phone (Windows only)
import pyautogui
# from welcome_backsir import *  # welcomeback sir animation code
from requests import get
import psutil#to check battery percentage
import requests
from bs4 import BeautifulSoup
import wikipedia
import webbrowser
from pydub import AudioSegment
from pydub.playback import play
import urllib.request
import time
import numpy as np
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import subprocess# for battery percentage
from jarvis_ui_converted import *
# from jarvis_intro import *
import sys
import cv2
import numpy as np
import winshell #used to clean recycle bin
import ffpyplayer
import ctypes# to turn the screenoff and on
import win32api, win32con #to turn the screen off and on
#ffpyplayer for playing audio
from ffpyplayer.player import MediaPlayer
# from face_recognition_code_for_jarvis import *
# from face_recognition_code import *
import mediapipe as mp
# from doctorstrange import *




engine = pyt.init("sapi5")
voices = engine.getProperty("voices")  # voices is a variable
# print(voices)
'''
voice[0] and voice[3]=david voice
voice[1]= microsoft mark voice(better one)'
voice[2] and voice[4]=zira voice'''
engine.setProperty("voice", voices[
    1].id)  # 1st parameter lo voices ani pedthe male voice ye osthadi everytime change it to voice and voices[should be 1 for female 0 for male]
engine.setProperty("rate", 160)  # 2nd parameter sets speed of voice

chose = 0  # for music


# converts text to speech
def speak(audio):
    engine.say(audio)  # says the given audio
    engine.runAndWait()



def wishme():
        hour = int(datetime.datetime.now().hour)
        # print(hour)

        if hour >= 0 and hour < 12:
            print("good morning")
            speak("good morning ")
        elif hour >= 12 and hour < 18:
            print("good afternoon")
            speak("good afternoon")
        else:
            print("good evening")
            speak("good evening")
        print("i am jarvis,how can i help you")
        speak("i am jarvis,how can i help you")


def facerecognition():
        recognizer = cv2.face.LBPHFaceRecognizer_create()  # Local Binary Patterns Histograms
        recognizer.read('trainer/trainer.yml')  # load trained model
        cascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascadePath)  # initializing haar cascade for object detection approach

        font = cv2.FONT_HERSHEY_SIMPLEX  # denotes the font type

        id = 2  # number of persons you want to Recognize

        names = ['', 'kiran','sri teja','shalini','abu','pramod']  # names, leave first empty bcz counter starts from 0

        cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # cv2.CAP_DSHOW to remove warning
        cam.set(3, 640)  # set video FrameWidht
        cam.set(4, 480)  # set video FrameHeight

        # Define min window size to be recognized as a face
        minW = 0.1 * cam.get(3)
        minH = 0.1 * cam.get(4)

        flag = True

        while flag:

            ret, img = cam.read()  # read the frames using the above created object

            converted_image = cv2.cvtColor(img,
                                           cv2.COLOR_BGR2GRAY)  # The function converts an input image from one color space to another

            faces = faceCascade.detectMultiScale(
                converted_image,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(int(minW), int(minH)),
            )

            for (x, y, w, h) in faces:

                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # used to draw a rectangle on any image

                id, accuracy = recognizer.predict(converted_image[y:y + h, x:x + w])  # to predict on every single image

                # Check if accuracy is less them 100 ==> 35 is perfect match

                ''' we are taking greater than 40 becuz sometimes for other persons accuracy will be 10 to 40 accuracy
                 depends upon on the camera quality in which sample photos are taken
                 if their is only one person sample then the model cannot distinguish between
                 different peoples so train more images add more images in samples either from internet or 
                  from camera but sequence must be 1.1, 2.1,3.1 etc each person should have unique sequence'''

                if (accuracy < 100 and accuracy >= 40):
                    id = names[id]
                    accuracy = "  {0}%".format(round(100 - accuracy))
                    # pyautogui.press('esc')
                    import ffpyplayer
                    # ffpyplayer for playing audio
                    from ffpyplayer.player import MediaPlayer
                    video_path = "D:\Jarvis project\WELCOME BACK SIR - J.A.R.V.I.S 4K UHD _shorts(1080P_HD).mp4"
                    window_name = "welcome back sir"

                    def welcomebacksir(video_path):
                        video = cv2.VideoCapture(video_path)
                        player = MediaPlayer(video_path)
                        cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)  # necessary for full screen
                        cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN,
                                              cv2.WINDOW_FULLSCREEN)  # necessary for full screen
                        while True:
                            grabbed, frame = video.read()
                            audio_frame, val = player.get_frame()
                            if not grabbed:
                                print("End of video")
                                break
                            if cv2.waitKey(30) & 0xFF == ord(
                                    "q"):  # video duration speed ki idhi adjust according to video length
                                break

                                # 0xFF==ord("q") press q to quit from video

                            cv2.imshow(window_name, frame)
                            if val != 'eof' and audio_frame is not None:
                                # audio
                                img, t = audio_frame
                        video.release()
                        cv2.destroyAllWindows()

                    welcomebacksir(video_path)  # calling function
                    # call the above code in face recogition with jarvis code

                    # speak("verification successfull")
                    # speak("welcome back sir")
                    flag = False  # flag becomes zero andd ends while loop
                    break  # breaks the current for loop



                else:
                    speak("verification unsuccessful")
                    id = "unknown"
                    accuracy = "  {0}%".format(round(100 - accuracy))
                    # line for jarvis.py you get error if you run face_recognition code
                    # break

                cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
                cv2.putText(img, str(accuracy), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

            cv2.imshow('camera', img)

            k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
            if k == 27:
                break
        cam.release()
        cv2.destroyAllWindows()


    # facerecognition()
'''Modules to import
Opencv
Mediapipe
Opencv-contrib

Type the following command in cmd
Pip install opencv-python mediapipe opencv-contrib-python
'''




class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()
        self.facerecognition()

        # self.JarvisIntro()




    # takecommand takes voiceinput from user and converts it to text and displays it on screen (required module=speechrecognition)
    def takecommand(self):
        listener = sr.Recognizer()
        # microphone is source for voice
        with sr.Microphone() as source:
            print("Listening.....")
            startsound=AudioSegment.from_wav("start up sound.wav")
            play(startsound)
            listener.pause_threshold = 1
            voice = listener.listen(source, timeout=10,
                                        phrase_time_limit=5)  # listens user voice from source(microphone)
            # if you dont speak or microphone is off for sometime(5) jarvis will automatically terminate
            endsound=AudioSegment.from_wav("end up sound.wav")
            play(endsound)

        try:
            print("Recognizing...")
            query = listener.recognize_google(voice, language="en-in")  # lang=english-india
            # string madyala variable name iyaniki format strings vadtham

            query = query.lower()  # converts user input to small letters
            print(f"user said:{query}")  # prints what user said

        except Exception as e:
            print("Say that again please...")
            speak("Say that again please...")
            return "none"
        return query


    def TaskExecution(self):
        wishme()

        while True:

            # userinput will be stored in query var
            self.query = self.takecommand()
            self.query = self.query.replace("jarvis", "")
            # when ever a person says jarvis how are you this code will help the interpretor to avoid jarvis and listen the words after jarvis word
            # for example if i dont write this code and say jarvis open command prompt then it wont open and says sorry sir i didnt understand
            # with the above code the interpretor will take the open command prompt and and avoid jarvis in beginning

            if "introduce yourself" in self.query or "tell me about yourself" in self.query or "jarvis introduce yourself" in self.query:
                #speak("hello,i am jarvis built by my boss kiran oruganti")
        
                video_path="D:\Jarvis project\jarvis introduction.mp4"
                def PlayVideo(video_path):
                    video=cv2.VideoCapture(video_path)
                    player = MediaPlayer(video_path)
                    while True:
                        grabbed, frame=video.read()
                        audio_frame, val = player.get_frame()
                        if not grabbed:
                            print("End of video")
                            break
                        if cv2.waitKey(35) & 0xFF == ord("q"):
                            break

                            # 0xFF==ord("q") press q to quit from video

                        cv2.imshow("Video", frame)
                        if val != 'eof' and audio_frame is not None:
                            #audio
                            img, t = audio_frame
                    video.release()
                    cv2.destroyAllWindows()
                PlayVideo(video_path)

            elif "clean recycle bin" in self.query:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)

            elif "turn off the screen" in self.query or "turn the screen off" in self.query:
                ctypes.windll.user32.SendMessageW(65535, 274, 61808, 2)

            elif "turn on the screen" in self.query or "turn the screen on" in self.query:
                ctypes.windll.user32.SendMessageW(65535, 274, 61808, -1)
                x, y = (0,0)#mouse
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y)#mouse will move and prevent from turning off the screen again

            elif "mute volume" in self.query:
                from sound import Sound
                Sound.mute()
            
            elif "unmute volume" in self.query:
                from pynput.keyboard import Key,Controller  
                keyboard = Controller()
                # keyboard.press(Key.media_volume_up)
                # keyboard.release(Key.media_volume_up)

        # setting volume to specific number
            
            elif "set volume to " in self.query: 
                self.query = self.query.replace("set volume to ", "")#the query should be as it is the spaces should also be their to  replace perfectly
                from pynput.keyboard import Key,Controller  
                keyboard = Controller()

                # range(1)= decreases or increases 2 percent volume (multiple of 2) range(50) means volume becomes 100

                for j in range(50):
                    keyboard.press(Key.media_volume_up) 
                    keyboard.release(Key.media_volume_up)
                #volume ni first 100 chesthanam tarwata dhanni set chesetappudu decrease chesthanam in this way we get accurate results in volume
                volrange=0
                # volume=self.takecommand()

                if self.query=="100" or self.query=="hundred":
                    volrange=50
                    for i in range(volrange):
                        keyboard.press(Key.media_volume_down)
                        keyboard.release(Key.media_volume_down)

                elif self.query =="90" or self.query=="ninety":
                    volrange=5 #5x2=10, 100-10 =90
                    for i in range(volrange):
                        keyboard.press(Key.media_volume_down)
                        keyboard.release(Key.media_volume_down)

                elif self.query =="80" or self.query=="eighty":
                    volrange=10  #10x2=20, 100-20 =80
                    for i in range(volrange):
                        keyboard.press(Key.media_volume_down)
                        keyboard.release(Key.media_volume_down)

                elif self.query =="70" or self.query=="seventy":
                    volrange=15 
                    for i in range(volrange):
                        keyboard.press(Key.media_volume_down)
                        keyboard.release(Key.media_volume_down)
                
                elif self.query =="60" or self.query=="sixty":
                    volrange=20
                    for i in range(volrange):
                        keyboard.press(Key.media_volume_down)
                        keyboard.release(Key.media_volume_down)

                elif self.query =="50" or self.query=="fifty":
                    volrange=25 
                    for i in range(volrange):
                        keyboard.press(Key.media_volume_down)
                        keyboard.release(Key.media_volume_down)
                
                elif self.query =="40" or self.query=="fourty" or self.query=="forty":
                    volrange=30 
                    for i in range(volrange):
                        keyboard.press(Key.media_volume_down)
                        keyboard.release(Key.media_volume_down)

                elif self.query =="30" or self.query=="thirty":
                    volrange=35 
                    for i in range(volrange):
                        keyboard.press(Key.media_volume_down)
                        keyboard.release(Key.media_volume_down)

                elif self.query =="20" or self.query=="twenty":
                    volrange=40
                    for i in range(volrange):
                        keyboard.press(Key.media_volume_down)
                        keyboard.release(Key.media_volume_down)
                
                elif self.query =="10" or self.query=="ten":
                    volrange=45
                    for i in range(volrange):
                        keyboard.press(Key.media_volume_down)
                        keyboard.release(Key.media_volume_down)

                elif self.query =="0" or self.query=="zero":
                    volrange=50
                    for i in range(volrange):
                        keyboard.press(Key.media_volume_down)
                        keyboard.release(Key.media_volume_down)

                
                
                    

                

            elif "how are you" in self.query:
                speak("I'm great thanks for asking")
            
            elif "hai" in self.query or "hello" in self.query:
                speak("Hi,How may i help you")

            elif "open notepad" in self.query or "open Notepad" in self.query:
                if True:
                    speak("opening notepad")
                    os.system("start notepad")
                else:
                    speak("you dont have notepad in your system so i cannot open notepad")
            elif "close notepad" in self.query:
                os.system("TASKKILL /F /IM Notepad.exe")

            elif "open command prompt" in self.query:
                if True:
                    speak("opening command prompt")
                    os.system("start cmd")
                else:
                    speak("sorry you dont have command prompt")

            elif "close command prompt" in self.query:
                os.system("TASKKILL /F /IM cmd.exe")

            elif "open file explorer" in self.query:
                speak("opening file explorer")
                os.system("explorer")

            elif "open camera" in self.query:
                speak("opening camera")
                speak("press q to close camera")
                cap = cv2.VideoCapture(0)
                while True:
                    #
                    ret, img = cap.read()
                    cv2.imshow("webcam", img)
                    k = cv2.waitKey(50)
                    if k == ord("q") or k == ord("Q"):  # press q to close camera
                        break
                cap.release()
                cv2.destroyAllWindows()
            elif "close camera" in self.query:
                pyautogui.hotkey("q")

            elif "what is the time" in self.query or "time" in self.query:
                time = datetime.datetime.now().strftime('%I:%M %p')
                print('Current time is ' + time)
                speak('Current time is ' + time)

            elif "change voice to female" in self.query:
                engine.setProperty("voice", voices[
                    2].id)  # 1st parameter lo voices ani pedthe male voice ye osthadi everytime change it to voice and voices[should be 1 for female 0 for male]
                engine.setProperty("rate", 160)

            elif "change voice to male" in self.query or "change to male voice" in self.query:
                engine.setProperty("voice", voices[
                    1].id)  # 1st parameter lo voices ani pedthe male voice ye osthadi everytime change it to voice and voices[should be 1 for female 0 for male]
                engine.setProperty("rate", 160)

                # <------------------------------------SENDING WHATSAPP MESSAGE USING JARVIS------------------------------------------------->

            elif "send whatsapp message" in self.query or "send whatsapp message" in self.query or \
                            " i want to send a message in whatsapp" in self.query or "send a whatsapp message" in self.query \
                            or "whatsaap message" in self.query:

                contacts = {"mother": "+9196522 61371", "sister": "+919666678143", "teja reddy": "+918499086087",
                                    "swaranjitha": "+91 79810 40672", "nandini": "+91 93812 74249", "swetha": "+9190523 38989",
                                    "sushma": "+919381746260", "vyshnavi": "+91 80085 77233", "afreen": "+91 95427 71221 ",
                                    "shirisha": "+91 93909 04160", "shivani": "+916305336475", "gracy": "+919390420357",
                                    "saketh": "+91 96187 35313", "nagacharan": "+917675915987", "tony": "+919014241961",
                                    "pavan": "+91 93982 58816", "nikhil": "+917793906095", "balaji": "+91 95152 37210 ",
                                    "sri teja": "7889490068", "shalini": "+919100891759", "madhukar sir": "+9198469117393",
                                    "cp sir": "+919848072444", "aravind sir": "+91 77300 70111", "ranjith sir": "+919347309750",
                                    "ramesh sir": "+919866826110", "ramu sir": "+918309175449",
                                    "srikanth sir": "+919985740968 ",
                                    "varaprasad sir": "+91 8555950622", "hema bindu mam": "+919908881941",
                                    "shoba mam": "+919849384255",
                                    "deepthi mam": "+919573817887", "sumalatha mam": "+919700215715",
                                    "srilatha mam": "+919100374481",
                                    "shirisha mam": "+918008743213"}

                names_list = list(contacts.keys())  # converts keys to list
                speak("sure!,whom do you wanna send")
                msgloop = True
                while msgloop:
                    #
                    contact_name = self.takecommand()  # calling takemethod again to take voice input for this sepecific variable(contact_name)

                    if contact_name in names_list:
                        #
                        number = contacts[contact_name]
                        print(number)
                        speak("what message u wanna send")
                        msg = self.takecommand()  # calling takemethod again to take voice input for this sepecific variable(msg)
                        print("your message:", msg)
                        speak("your message will be delivered in 10 to 30 seconds")
                        pywhatkit.sendwhatmsg_instantly(number, msg)  # pywhatkitsends msg instantly
                        speak("message delivered")
                        pyautogui.hotkey("alt","tab")
                        msgloop = False

                    else:
                        speak("please enter from available contacts")
                        msgloop = False

        #brightness percentage control
            elif "set brightness percentage" in self.query or "set brightness level" in self.query or "set brightness" in self.query:
                def run(cmd):
                 completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
                 return completed

                if __name__ == '__main__':
                    speak("how much brightness percentage should i set ?")
                    take_brightness=self.takecommand()
                    command = "(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1," + take_brightness + ")"
                    hello_command = f"Write-Host {command}"
                    hello_info = run(hello_command)
                    speak(f"{take_brightness} brightness percentage set")


    #<--------------------------------LIVE SKETCH USING JARVIS-------------------------->
            elif "draw a sketch of me" in self.query or "draw a live sketch of me" in self.query:
                    speak("sure, please give me 5 to 10 seconds")
                    speak("to exit from the live sketch diagram press q")
                

                    camera = cv2.VideoCapture(0)

                    while True:
                        ret, frame = camera.read()
                        if ret == False:
                            break
                        # getting width and height of image
                        height, width, _ = frame.shape

                        # creating copy of image using resize function
                        resziedImage = cv2.resize(frame, (width, height),
                                                interpolation=cv2.INTER_AREA)

                        # creating 3X3 kernel, inorder to sharpen the image /frame
                        kernel = np.array([[-1, -1, -1],
                                        [-1, 9, -1],
                                        [-1, -1, -1]])
                        # Appling kernel on the frame using filter2D function .
                        sharpenImage = cv2.filter2D(resziedImage, -1, kernel)

                        # converting image into Grayscale image.
                        gray = cv2.cvtColor(sharpenImage, cv2.COLOR_BGR2GRAY)

                        # creating inverse of sharpen image .
                        inverseImage = 255-gray

                        # applying Gussain Blur on the image .
                        bluredImage = cv2.GaussianBlur(inverseImage, (15, 15), 0, 0)

                        # create a pencilSketch using divide function on opencv .
                        pencilSketch = cv2.divide(gray, 255-bluredImage, scale=256)

                        # show the frame on the screen .
                        #cv.imshow('Sharpen Image', sharpenImage)
                        cv2.imshow("pencilSketch", pencilSketch)

                        cv2.imshow("frame", frame)
                        key = cv2.waitKey(1)
                        if key == ord('q') or key== ord('Q'):
                            break

                    cv2.destroyAllWindows()
                    camera.release()
                    speak("You might think the live sketch diagram is not that great. The problem is the laptop camera comes with only 1 megapixel resolution, I cant do anything about it")


        #cp sir
            elif "what do you know about cp sir" in self.query:
                speak('''Dr. Ch.V. Purushotham Reddy, B.Ed., M.Sc., Ph.DFounder 
                / President & ChancellorDr Reddy is instrumental in the promotion of higher education in the backward area of Telangana.
                 He served as the Principal of Chaitanya Degree College and also the Secretary-cum-Correspondent of Chaitanya Group of Colleges and presently the Founder and Chancellor of Chaitanya Deemed to be University. 
                 He has participated in 16 National and International seminars, and published some research papers despite his hectic schedule''')




    # <-----------------playing audio and fun using jarvis------------------------>
            elif "i love you" in self.query or "friday i love you" in self.query:
                romeo = AudioSegment.from_wav("nuvemaina romeo.wav")
                play(romeo)
                # from romeodilogue import *

            elif "he died loving but I am not his type" in self.query or "he died loving" in self.query:
                cp = AudioSegment.from_wav("chala shekal unnay ra neelo.wav")
                play(cp)
                #from chala_shekal_unnay import *

            elif "jarvis do you love me" in self.query or "do you love me" in self.query:
                fs = AudioSegment.from_wav("I Just Want Flirtationship.wav")
                play(fs)
                # from I_just_want_flirtationship import *

            elif "propose me" in self.query or "propose this lady" in self.query or "propose this girl" in self.query or "propose girl" in self.query or "this girl" in self.query:
                pd = AudioSegment.from_wav("Malli Malli Idhi Rani Roju.wav")
                play(pd)
                # from propose_dialogue import *

            elif "propose him" in self.query or "propose this guy" in self.query:
                mca = AudioSegment.from_wav("mca proposal scene.wav")
                play(mca)
                # from mca_proposal_scene import *

            elif "idiot" in self.query or "stupid" in self.query or "waste fellow" in self.query or "psycho" in self.query:
                brahmi1 = AudioSegment.from_wav("yendi bro antha mata annav(720P_HD).wav")
                play(brahmi1)
                # from yendi_bro_anthamataannav import *


            elif "who is teja reddy" in self.query or "teja reddy" in self.query:
                kingu = AudioSegment.from_wav("kingu koduku.wav")
                play(kingu)
                # from kingu_koduku import *

            elif "jarvis she loves you" in self.query or "love you" in self.query or "she loves you" in self.query:
                # from devudu_unnadra import *
                karthi1 = AudioSegment.from_wav("Devudu unnadra.wav")
                play(karthi1)

            elif "but as a friend" in self.query:
                karthi2 = AudioSegment.from_wav("Devudu ledra.wav")
                play(karthi2)

            elif "why should anyone love you" in self.query or "jarvis why should anyone love you" in self.query or "jarvis why should i love you" in self.query:

                orange = AudioSegment.from_wav("nijayithi unnodini.wav")
                play(orange)

            elif "bye jarvis" in self.query or "bye" in self.query or "goodbye" in self.query or "jarvis bye" in self.query:
                husharu1 = AudioSegment.from_wav("Undiporadhey song.wav")
                play(husharu1)
                # from undiporadhe import *

            elif "jarvis sing a song for me" in self.query or "jarvis sing a song" in self.query or "sing a song" in self.query:
                husharu2 = AudioSegment.from_wav("vere janmantu naake nduku le.wav")
                play(husharu2)
                # from verejanmantu import *


        #<----------------------------------------DOCTORSTRANGEUSINGJARVIS---------------------------------------------->
            # elif "make me doctor strange" in self.query or "i want to become doctor strange" in self.query\
            #         or "make me doctor strange" in self.query:
            #     speak("as you wish")
            #     speak("but please wait for 10 to 30 seconds to open the camera")
            #     speak("i will assure you that you will enjoy it")
            #     print("press q to exit from doctor strange filter")
            #     speak("press q to exit from doctor strange filter")
            #     import doctorstrange# from import * throws an error





                    # to make this work we have to link whatsapp web in microsoft edge to mobile
                    # elif "send WhatsApp message" in query:
                    #     pywhatkit.sendwhatmsg("+919652261371",
                    #                           "hello i am jarvis this message is sent by my boss from pycharms code", 11, 57)

            elif "music" in self.query or "hit some music" in self.query:
                chose=0
                speak("playing music")
                music_dir_path = "C:\\Users\\kiran\\Music"
                songs = os.listdir(music_dir_path)  # converting songs into list
                d = random.choice(songs)  # chooses random music
                os.startfile(os.path.join(music_dir_path, songs[1]))  # plays random music
                chose += 1

            elif "next" in self.query or "i don't like this " in self.query \
                            or "next song" in self.query:
                music_dir_path = "C:\\Users\\kiran\\Music"
                songs = os.listdir(music_dir_path)  # converting songs into list
                length = len(songs)
                chose += 1
                if chose >= length:
                    speak("no more music to next")
                    speak("i'm playing music from starting")
                    chose = 0
                    os.startfile(os.path.join(music_dir_path, songs[chose]))
                else:
                    os.startfile(os.path.join(music_dir_path, songs[chose]))
                    chose += 1
            
                '''if sir ask why jarvis cant play before files explain in this way manam play or next anna prathi sari oka kotha file ni 
                    open chesi play chesthandi before kuda work avvali ante motham folder ni select chesi play midha click chesthe work aithadi
                    manam windows lo oka file open chesnappudu before song button kodthe same song malla play aithadi
                    next song aane option asal undane undadh'''


            #this code is to play before songs only but wont work(check above statement)
            #this before button will work but u have to comment the random(music) line even though the before button work 
            #it will play some random song becuz chose= value change 
            elif "before song" in self.query or "repeat" in self.query or "repeat the song" in self.query:
                music_dir_path = "C:\\Users\\kiran\\Music"
                songs = os.listdir(music_dir_path)  # converting songs into list
                length = len(songs)
                chose += 1
                if chose >= length:
                    speak("no more music to next")
                    speak("i'm playing music from starting")
                    chose = 0
                    os.startfile(os.path.join(music_dir_path, songs[chose]))
                else:
                    os.startfile(os.path.join(music_dir_path, songs[chose]))
                    chose -= 1


            elif 'stop' in self.query or "stop the music" in self.query or "quit music" in self.query or "stop music" in self.query:
                speak('okay')
                speak("now i stop music")
                # we are writing different music players name hear becuz one one person will have their own wish music players
                # the following codes will work for music players
                os.system('taskkill /F /FI "WINDOWTITLE eq Movies & Tv" ')
                os.system('taskkill /F /FI "WINDOWTITLE eq Groove Music" ')
                os.system('taskkill /F /FI "WINDOWTITLE eq Media Player" ')
                os.system('taskkill /F /FI "WINDOWTITLE eq Windows Media Player" ')
                # os.system('taskkill /F /FI "WINDOWTITLE eq VLC media player" ')

    # <----------------------------------------------WEATHER FORECAST USING JAJRVIS----------------------------------------->
            # THERE SHOULD BE "in" COMPULSORY IN  QUERY OTHERWISE THIS CODE WILL NOT WORK
            elif "temperature in" in self.query or "weather in" in self.query or "what's the weather in "\
                 in self.query or "weather at " in self.query or "what's the weather at" in self.query\
                    or "what is the weather at" in self.query or "what is the weather in" in self.query:
                city = self.query.split("in", 1)
                city1=self.query.split("at",1) # at,is or add cheyali ante take another variable and write query.split("is",1)
                soup = BeautifulSoup(requests.get(f"https://www.google.com/search?q=weather+in+{city[1]}").text,
                                    "html.parser")
                region = soup.find("span", class_="BNeawe tAd8D AP7Wnd")
                temp = soup.find("div", class_="BNeawe iBp4i AP7Wnd")
                day = soup.find("div", class_="BNeawe tAd8D AP7Wnd")
                weather = day.text.split("m", 1)
                temperature = temp.text.split("C", 1)
                # Response("Its Currently"+weather[1]+"and"+temperature[0]+"celsius"+"in"+region.text)
                print("Its Currently" + weather[1] + " and " + temperature[0] + "celsius " + "in " + region.text)
                speak("Its Currently" + weather[1] + " and " + temperature[0] + "celsius " + "in " + region.text)





            # <----------------IP ADDRESS(using request module)---------------------->
            elif "ip address " in self.query or "what is my ip address" in self.query or "my ip address" in self.query:

                ip = get("https://api.ipify.org").text  # website gives ip address we are converting it into text
                print(f"your ip address is: {ip} ")
                speak(f"your ip address is: {ip} ")



            elif "who" in self.query or "where " in self.query or "what is" in self.query or "how " in self.query:
                self.query = self.query.replace("who", "")
                self.query = self.query.replace("what is", "")
                self.query = self.query.replace("how", "")
                self.query = self.query.replace("where", "")
                info = wikipedia.summary(self.query, sentences=2)  # read only 3 sentences
                speak("according to wikipedia")
                print(info)
                speak(info)

    # <-----------------------playing in youtube using pywhatkit------------------------>
            elif "play" in self.query:
                self.query = self.query.replace('play', '')  # empty string replaces play
                # if i say play saranga dariya then system takes only saranga dariya.''(in this empty string saranga dariya will be stored)
                print("Playing" + self.query)
                speak("Playing" + self.query)
                pywhatkit.playonyt(self.query)


            elif "search" in self.query or "google" in self.query:
                self.query = self.query.replace("search ", "")
                self.query = self.query.replace("google ", "")
                print("okay,Searching for", self.query)
                speak("okay searching for" + self.query)
                pywhatkit.search(self.query)

                # webbrowser.open("www.youtube.com")


            elif "open google" in self.query:
                webbrowser.open("www.google.com")

            elif "open facebook" in self.query:
                webbrowser.open("www.facebook.com")


    #<----------------------------------------------ACCESSING MOBILE CAMERA---------------------------------------------------------->
            elif "open mobile camera" in self.query or "access mobile camera" in self.query:
                speak("okay")
                speak("press q to exit from mobile camera")
                # the url will change sometimes check the url in ipwebcam app in mobile
                url = "http://26.118.103.157:8080/shot.jpg"
                while True:
                    img_arr = np.array(bytearray(urllib.request.urlopen(url).read()), dtype=np.uint8)
                    img = cv2.imdecode(img_arr, -1)
                    cv2.imshow("webcam", img)
                    q = cv2.waitKey(1)
                    if q == ord("q") or q== ord("Q"):
                        break
                cv2.destroyAllWindows()






    # <------PYAUTOGUI FEATURES=used to automate python using shortcut keys------->
            elif "open hidden menu" in self.query:
                # win +X=opens hidden menu
                pyautogui.hotkey("winleft", "x")

            elif "open task manager" in self.query:
                # Crtl + Shift +Esc=opens task manager
                pyautogui.hotkey("ctrl", "shift", "esc")

            elif "open task view" in self.query:
                # win +tab=shows running tasks
                pyautogui.hotkey("winleft", "tab")

            elif "shift tab" in self.query or "switch tab" in self.query or "get back to ur screen" in self.query:
                # alt+tab=shifts the tab
                pyautogui.hotkey("alt", "tab")

            elif "take screenshot" in self.query:
                # win+prtscr
                pyautogui.hotkey("winleft", "prtscr")
                print("screenshot location C:\\Users\\kiran\\OneDrive\\Pictures\\Screenshots")
                speak("okay ,you the screenshot is in the given location")

            elif "take snip" in self.query:
                pyautogui.hotkey("winleft", "shift", "s")
                speak("please take your snip of your choice")

            elif "close current application" in self.query:
                pyautogui.hotkey("alt", "f4")

            elif "take me to desktop" in self.query:
                pyautogui.hotkey("winleft", "d")

            elif "open new virtual desktop" in self.query:
                pyautogui.hotkey("winleft", "ctrl", 'd')

            elif "open file explorer" in self.query:
                pyautogui.hotkey("winleft", "e")

            elif "open run dialog box" in self.query:
                pyautogui.hotkey("winleft", "r")

            elif "copy the selected text" in self.query or "copy" in self.query:
                pyautogui.hotkey("ctrl", "c")
                speak("copied")

            elif "paste the copied text" in self.query or "paste" in self.query:
                pyautogui.hotkey("ctrl", "v")
                speak("pasted")

            elif "type what i say" in self.query:  # u might get error if you get error comment this code
                pyautogui.hotkey("winleft", "h")


    # <-----------------------------------BATTERY PERCENTAGE(psutil module)------------------------->

            elif "battery percentage" in self.query or "what is my battery percentage" in self.query or "battery percentage in my system" in self.query:
                # import psutil

                battery = psutil.sensors_battery()
                percentage = battery.percent
                if percentage >= 75 and percentage <= 100:
                    speak(f"our system has {percentage} percent battery left,which is sufficient for about 2 hours at a moderate usage ")
                elif percentage >= 30 and percentage < 75:
                    speak(f"our system has {percentage} percent battery left,which might give you 60 to 70 minutes at a moderate usage")
                elif percentage >= 0 and percentage < 30:
                    speak(f"our system has a very crtical battery left, that is {percentage} percent battery,Please pluggin the charger")

            elif "jarvis sleep" in self.query or "bye" in self.query or "sleep" in self.query or "close jarvis" in self.query or "terminate yourself" in self.query:
                    # speak("bye")
                    speak("press exit to turn me off")
                    # break








startExecution =MainThread() # created object for MainThread class

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_.clicked.connect(self.startTask) #we have to create startTask function becuz it not predefined
        self.ui.pushButton_2.clicked.connect(self.close)# close is predefined
    

    def endtask(self):
        if "jarvis sleep" in self.query or "bye" in self.query or "sleep" in self.query or "close jarvis" in self.query or "terminate yourself" in self.query:
         self.ui.pushButton_2.clicked.connect(self.close)
    
    def startTask(self):
        facerecognition()
        # JarvisIntro(video_path)
        
        self.ui.bluebg=QtGui.QMovie(":/gifs/lib/bg gif.gif")
        self.ui.label.setMovie(self.ui.bluebg)
        self.ui.bluebg.start()

        self.ui.electricblue1=QtGui.QMovie(":/gifs/lib/blue rotating bg.gif")
        self.ui.label_2.setMovie(self.ui.electricblue1)
        self.ui.electricblue1.start()

        self.ui.neongif=QtGui.QMovie(":/gifs/lib/3OdB.gif")
        self.ui.label_3.setMovie(self.ui.neongif)
        self.ui.neongif.start()

        self.ui.electricblue2=QtGui.QMovie(":/gifs/lib/blue rotating bg.gif")
        self.ui.label_4.setMovie(self.ui.electricblue2)
        self.ui.electricblue2.start()

        self.ui.hologram=QtGui.QMovie(":/gifs/lib/hologram.gif")
        self.ui.label_5.setMovie(self.ui.hologram)
        self.ui.hologram.start()

        # :/gifs/lib/Iron_Template_1.gif

        self.ui.middleironman=QtGui.QMovie(":/gifs/lib/Jarvis_Gui (1).gif")
        self.ui.label_6.setMovie(self.ui.middleironman)
        self.ui.middleironman.start()


        self.ui.left_top_bg=QtGui.QMovie(":/gifs/lib/Jarvis_Loading_Screen.gif")
        self.ui.label_7.setMovie(self.ui.left_top_bg)
        self.ui.left_top_bg.start()

        self.ui.earth_template=QtGui.QMovie(":/gifs/lib/Earth_Template.gif")
        self.ui.label_8.setMovie(self.ui.earth_template)
        self.ui.earth_template.start()
        
        # Dspeak =MainThread()
        self.date = time.strftime("%A,%d %B")

        # Dspeak.start()
        #self.ui.label_4.setPixmap(QPixmap("D:\Jarvis project\jarvis gui\futuristic gui\lib\png bg.png"))
        self.ui.label_10.setText("<font size=6 color='white'>"+self.date+"</font>")
        self.ui.label_10.setFont(QFont(QFont('Acens',7)))


        timer =QTimer(self)
        timer.timeout.connect(self.showTime)#calling showTime method
        timer.start(1000)
        startExecution.start() #starting mainthread class using startExecution object
    

    def showTime(self):
        current_time= QTime.currentTime()
        # current_date=QDate.currentDate()
        self.time = datetime.datetime.now().strftime('%I:%M %p')
        label_time= current_time.toString("hh:mm:ss") # if you want in 12 hours format give time variable in paranthesis instead of "hh:mm:ss"
        # label_date=current_date.toString(Qt.ISODate)
        # self.ui.label_10.setText(label_date)
        self.ui.label_9.setText(label_time)
        self.ui.label_9.setText("<font size=12 color='white'>"+self.time+"</font>")
        self.ui.label_9.setFont(QFont(QFont('Acens',10)))






        # self.time=datetime.datetime.now().strftime('%I:%M %p')
        # self.ui.label_9.setText("<font size=12 color='white'>"+self.time+"</font>")
        # self.ui.label_9.setFont(QFont(QFont('Acens',8)))

        
















        startExecution.start() #starting mainthread class using startExecution object




        
        
    #     timer =QTimer(self)
    #     timer.timeout.connect(self.showTime)
    #     timer.start(1000)
    #     startExecution.start() #starting mainthread class using startExecution object
    

    # def showTime(self):
    #     current_time= QTime.currentTime()
    #     current_date=QDate.currentDate()
    #     time = datetime.datetime.now().strftime('%I:%M %p')
    #     label_time= current_time.toString("hh:mm:ss") # if you want in 12 hours format give time variable in paranthesis instead of "hh:mm:ss"
    #     label_date=current_date.toString(Qt.ISODate)
    #     self.ui.label_2.setText(label_date)
    #     self.ui.label_3.setText(label_time)

app=QApplication(sys.argv)

jarvis=Main()
jarvis.show()
exit(app.exec_())
