import threading
from time import time, sleep
#import pygame

class Timer:
    def __init__(self, length, sound):
        # Initalize pygame sound
        #pygame.mixer.init()
        
        # Length of timer
        self.length = float(length)
        
        #Sound played once timer is done
        self.sound = sound

        # Set the starting time
        self.begin = time()

        # Initalize the timer
        self.a = threading.Timer(self.length, self.play,[self.sound])

        # Start the timer
        self.a.start()
        
    # Function to play a sound
    def play(self, s):
        # load the music file
        ''' pygame.mixer.music.load("wav/" + s)
        # play the music
        pygame.mixer.music.play()'''
        print "wav/" + s
        
    # Function to cancel the timer
    def cancel(self):
        self.a.cancel()

    # Function to pause the timer
    def pause(self):
        self.a.cancel()
        self.end = time()

    # Function to resume the timer
    def resume(self):
        self.t = threading.Timer(self.length-(self.end-self.begin), self.play,[self.sound])
        self.t.start()

