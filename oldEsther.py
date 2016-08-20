#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
    return "It is %s"  % now 

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
    #return "I cannot access the weather"

def getWeather():
    file = open('weather.txt', 'r')
    data = file.read()
    file.close()
    return data


def favColor():
    return "I cannot describe it in your terms. It's ,kind of a multidimensional turqoise but in a different electromagnetic spectrum."

def name():
    return "None of your beeswax"

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

q = str(raw_input("Ask a question "))
q = q.lower()
while 1:
    now = datetime.datetime.now()
    if now.minute % 5 == 0:
        writeWeather()
    if q == "q" or q == "quit":
        break
    elif q == "whats your favorite color" or q == "what's your favorite color" or q == "what is your favorite color":
        e.say(favColor())
    elif q == "what time is it" or q == "what's the time" or q == "whats the time" or q == "what is the time" or q == "time":    
        e.say(time())
    elif q == "what is the weather" or q == "what's is the weather" or q == "whats the weather" or q == "weather":
        e.say(getWeather())
    elif q == "what is your name" or q == "what's your name" or q == "whats your name":        e.say(name())
        e.say(name())
    elif q == "stop":
        stop()
    elif q == "pause":
        pause()
    elif q == "start" or q == "play":
        start()
    elif q == "rewind":
        rewind()
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
        e.say("I don't understand that request.")
    q = str(raw_input("Ask another question "))
    q = q.lower()
