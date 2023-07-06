# Objective

To display 2 random images. No attempts to accept user input or animations are done at this stage.

# Line-by-line Explanation

### Important Libraries

We'll need to import the libraries that we need to make sure our code works with a Micro:bit.

```python
from microbit import *
import random
```

### Heads or Tails?

Now we need to add code that randomly selects heads or tails. We start by creating a list of our options. In this case,
we'll use the SKULL image for heads, and the HEART image for tails.

```python
choices = [Image.SKULL, Image.HEART]
image = random.choice(choices)
```

This creates a list containing our 2 options. We then randomly pick one using the `random.choice()` function - this will
randomly select an element from the list for us.

### Show the result

With our chosen image, we now need to display the result.

```python
display.show(image)
```

# Next Version

Great! We've added a way to randomly generate heads or tails, and to show that on the Micro:bit. You can see the full
code [here](./v1.py)

The next version will let us flip our pretend 'coin' as many times as we like without restarting the Micro:bit. You can
access that [here](../v2/README.md)