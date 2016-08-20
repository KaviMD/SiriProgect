#!/usr/bin/env python
# -*- coding: utf-8 -*-

#                | 
#                |  
#            \   |   / 
#             \  |  /     
#              \ | /      
#               \|/   
''' Go to 'http://www.dronkert.net/rpi/vol.html' or 'https://igrudge.net/script-setting-volume-raspberry-pi-command-line/' to setup volume '''

import pyespeak
import time
from time import sleep
import datetime
e = pyespeak.eSpeak("en")
global song
song = ""

def time():
    import time
    now = time.strftime("%c")
    return str("It is %s"  % now)

def writeWeather():
    import urllib2
    import json
    zip = "15232"
    key = "c250bd529b608df1"
    url = 'http://api.wunderground.com/api/' + key + '/geolookup/conditions/q/PA/' + zip + '.json'
    f = urllib2.urlopen(url)
    json_string = f.read()
    parsed_json = json.loads(json_string)
    city = parsed_json['location']['city']
    state = parsed_json['location']['state']
    weather = parsed_json['current_observation']['weather']
    temperature_string = parsed_json['current_observation']['temperature_string']
    feelslike_string = parsed_json['current_observation']['feelslike_string']
    f.close()
    file = open("weather.txt", "w")
    file.write('In ' + city + ', ' + state + ' it\'s ' + weather.lower() + '. The temperature is ' + temperature_string + ' but it feels like ' + feelslike_string + '.')
    file.close()

def getWeather():
    file = open('weather.txt', 'r')
    data = file.read()
    file.close()
    #return str(data)
    return str("Don't ask me")


def favColor():
    return str("I cannot describe it in your terms. It's ,kind of a multidimensional turqoise but it can only be seen in a different electromagnetic spectrum.")

def name():
    return str("None of your beeswax")

def play(s):
    global song
    song = s
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("wav/"+s+".wav")
    pygame.mixer.music.play()

def stop():
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.rewind()
    pygame.mixer.music.stop()

def pause():
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.pause()
    
def start():
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.unpause()
    
def rewind():
    global song
    stop()
    play(song)

def setVolume(loudness):
    import os
    os.system("vol " + str(loudness))
    
q = str(raw_input("Ask a question "))
q = q.lower()
while 1:
    now = datetime.datetime.now()
    if now.minute % 5 == 0:
        writeWeather()
    if q == "q" or q == "quit":
        break
    elif q == "whats your favorite color" or q == "what's your favorite color" or q == "what is your favorite color":
        pause()
        sleep(0.5)
        e.say(favColor())
        e.reopen()
        start()
    elif q == "what time is it" or q == "what's the time" or q == "whats the time" or q == "what is the time" or q == "time":
        pause()
        sleep(0.5)
        e.say(time())
        e.reopen()
        start()
    elif q == "what is the weather" or q == "what's is the weather" or q == "whats the weather" or q == "weather":
        pause()
        sleep(0.5)
        e.say(getWeather())
        e.reopen()
        start()
    elif q == "what is your name" or q == "what's your name" or q == "whats your name":
        pause()
        sleep(0.5)
        e.say(name())
        e.reopen()
        start()
    elif q == "stop":
        stop()
    elif q == "pause":
        pause()
    elif q == "start" or q == "play":
        start()
    elif q == "rewind" or q == "replay":
        rewind()
    elif q == "volume 0":
        setVolume(0)
    elif q == "volume 1":
        setVolume(10)
    elif q == "volume 2":
        setVolume(20)
    elif q == "volume 3":
        setVolume(30)
    elif q == "volume 4":
        setVolume(40)
    elif q == "volume 5":
        setVolume(50)
    elif q == "volume 6":
        setVolume(60)
    elif q == "volume 7":
        setVolume(70)
    elif q == "volume 8":
        setVolume(80)
    elif q == "volume 9":
        setVolume(90)
    elif q == "volume 10":
        setVolume(100)
    elif q == "play viva la vida": 
        play("vivaLaVida")
    elif q == "play light 'em up" or q == "play light em up" or q == "play light them up":
        play("lightEmUp")
    elif q == "play pompeii" or q == "play pompii":
        play("pompeii")
    elif q == "play lost boy":
        play("lostBoy")
    elif q == "play party in the usa":
        play("partyUSA")
    elif q == "play tiny dancer":
        play("tinyDancer")
    elif q == "play clocks":
        play("clocks")
    elif q == "play star ships":
        play("starShips")
    elif q == "play better when i'm dancing" or q == "better when im dancing":
        play("betterWhenImDancin")
    elif q == "play just the way you are":
        play("theWayYouAre")
    elif q == "play you make me feel":
        play("youMakeMeFeel")
    else:
        pause()
        sleep(0.5)
        e.say("Meesa no understand you sa")
        e.reopen()
        start()
    q = str(raw_input("Ask another question "))
    q = q.lower()
