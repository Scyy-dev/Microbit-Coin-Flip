from microbit import *
import random

choices = [Image.SKULL, Image.HEART]

image = random.choice(choices)
display.show(image) 