# Objective

This version adds an animation to help the player tell each time they flip the 'coin'.

# Line-by-line Explanation

### Choosing an animation

There are a lot of different ways to add an animation. You could add flashing lights, display a bunch of random images,
play a sequence of images, show an animation of a coin being 'flipped', the list goes on!

I highly encourage you to experiment and play around until you find an animation you like. The animation I'll be
covering is a clock that comes pre-packed with the Micro:bit

### The Clock Animation

The clock animation comes pre-packed with the Micro:bit library, so we'll just be putting what we need together to make
it work. The animation itself is packaged as a list of all 12 hours on a clock.

you can access the list using `Images.ALL_CLOCKS`.

If you want to check out what some of them do, try adding the following line:

```python
display.show(Images.All_CLOCKS[n])
```

Replace the `n` with a number between 0 and 11 (inclusive).

To use the clock, we need to iterate over each item in the list. We can do so like this:

```python
for clock in Images.ALL_CLOCKS:
# do something with the clock image!
```

for now, let's try displaying the clocks and seeing how we go:

```python
for clock in Images.ALL_CLOCKS:
    display.show(clock)
```

But if we try running this, our clock never shows!

### Dude, Where's my Clock?

For us to be able to see the clock, we need to slow everything down a bit. Each time we show a clock image, we need to '
pause' the Micro:bit so it has time to show the clock, and then us as humans have time to actually see the image show
up.

We can do this by simply adding a `sleep()` call every time we display a clock image. I use `150` milliseconds because I
believe it's a long enough time for the player to see each image without being too slow.

```python
for clock in Images.ALL_CLOCKS:
    display.show(clock)
    sleep(150)
```

### Putting it all together

Now we know how to show off our clock, we need to run it when we flip our 'coin'. It's as simple as copy-pasting what
we've done so far and putting it in the right spot:

```python
if button_a.was_pressed():

    for clock in Images.ALL_CLOCKS:
        display.show(clock)
        sleep(150)

    image = random.choice(choices)
    display.show(image)
```

This means our animation runs every time we hit the `A` button, and then a skull or heart is shown!

I also like to run the clock animation twice just to keep the player a little extra on their toes, and I'll leave that
as an extra challenge for you! (if you get stuck, see [Further Challenges](#further-challenges)

# Further Challenges

Great job for making it this far! If you've managed to get everything working up to this point, you should have a coin
flip with a fun animation each time you flip the coin.

If you got stuck, or want a hint for the animation challenge, you can see the full code [here](./v3.py)

There's not really much more to add to it, but if you want to add more, go crazy with the animations!
