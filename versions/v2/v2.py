from microbit import *
import random

choices = [Image.SKULL, Image.HEART]

while True:

    if button_a.was_pressed():
        image = random.choice(choices)
        display.show(image)
