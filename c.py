from distutils.cmd import Command
from email.mime import audio
from re import search
import speech_recognition
import pyttsx3

import webbrowser as wb
from datetime import date 
from datetime import datetime


robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

while True:

    with speech_recognition.Microphone() as mic:
        print("robot: Im listening")
        audio = robot_ear.listen(mic)
    
    print("robot: ...")

    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""

    if you == "":
        robot_brain = " i cannot hear you, try again"
    elif "hello" in you:
        robot_brain = "hello zu"
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minutes %S seconds")
    elif " girl friend" in you:
        robot_brain = "Im not into terrestrial partnerships. I'm more of free radical "
    elif " tired " in you:
        robot_brain = " 1. eat often to beat tiredness. 2. get moving somewhere you want 3. cut out caffein. 4. take a rest 5. sleep well . It will be better for you, love you so much"
    elif "her" in you:
        robot_brain = "yes s"
    elif "name" in you:
        robot_brain = "My name is DITCONME, or you can call me DCM it is a beautiful name that i love it so much"
    elif "sad" in you:
        robot_brain = "Im sorry you're feeling that way. Sometimes, taking a quiet monment can help. You could try listening to your favourite music , or doing some simple stretches,and the last do not overthink negative, i just wanna say i love you, you're not alone."
    elif "Hey you" in you:
        robot_brain = "hmmmm"
    elif "morning" in you:
        robot_brain = "You too"
    elif "night" in you:
        robot_brain = "sweatdream sir"
    elif "afternoon" in you:
        robot_brain = "You too"
    
    elif "away" in you:
        robot_brain = "have a nice day sir"
        print("robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain = "im fine"

    print("robot: " + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()

            