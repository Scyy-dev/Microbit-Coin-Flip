from microbit import *
import random

choices = [Image.SKULL, Image.HEART]

while True:
    
    if button_a.was_pressed():
        
        for i in range(2):
            for clock in Image.ALL_CLOCKS:
                display.show(clock)
                sleep(100)
    
        image = random.choice(choices)
        display.show(image)