# Objective
This version allows the heads or tails to be repetitively flipped without needing to restart the Micro:bit. Animations are covered in the next version.

# Line-by-line Explanation

### Player Input
To allow the player to 'reflip' the coin as many times as they like, we need to prompt them for input. Our best option is a button press!

```python
if button_a.was_pressed():
    image = random.choice(choices)
    display.show(image)
```

### To Infinity!
We ran into a problem - our image never shows! That's because the program runs once, checks if the button was pushed, and then stops.

To fix this, we need the program to constantly check if the button has been pressed. The best way to do this is to checking checking forever!

```python
while True:
    if button_a.was_pressed():
        image = random.choice(choices)
        display.show(image)
```

This ensures our program is constantly checking if the button has been pressed, and then flips our 'coin' for us!

# Next Version

Great! We've added a way to 'reflip' our coin. You can see the full code [here](./v2.py)

The next version will add an animation to make the coin flip a bit more interesting. You can access that [here](../v3/README.md)