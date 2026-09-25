# Activity 9: Number Guessing Game With Multiple Files

In this activity, we will walk through how to organize a number guessing game by breaking it down into separate files.

Once you have completed the guided part of the activity, be sure to also complete the [Extension Activity](#extension-activity-modular-mayhem)

## Why Bother With Multiple Files?

As programs grow larger, it becomes increasingly difficult to manage all of the code in a single file. Splitting a project into **modules** helps organize related code, making it easier to read, test, and maintain.

| Module                                                                                                                              |
|:------------------------------------------------------------------------------------------------------------------------------------|
| *A Python file that contains code, such as functions, classes, or variables, which can be imported and used by other Python files.* |

A common approach is to place functions, classes, or other related code into modules and then import them into the main program. This keeps files focused on a specific purpose and allows code to be reused across multiple projects.


## 1. Create a Root Folder

Whenever you are creating a new Python project, it is best to stay organized by placing all the files related to the project in the same folder. This is especially true for this activity. Be sure to create a folder named `root`.

Inside the folder, create a new `root/main.py` file. **You will also create a file called `root/utils.py`.** *Please make sure for this activity that your file names are exactly the same as these.*

## 2. Planning Out the Game

Here we have some functions outlined in a flowchart for the logic behind the number guessing game. 

![Number guessing game flowchart](./Number-Guessing-Game.webp)

Overall we need a program that generates one random number at the start, then has a continuous loop for comparing an input guess to the value of the number that repeats until the number is guessed! Additionally, there is a validation function to ensure the correct type of data is being processed.

## 3. Adding Code to `root/utils.py`

While this project is still relatively small compared to others you will complete in this course, organizing different parts of your code into different files will make it much easier to debug and plan your programs. 

For this project, we can keep our main function fairly simple, and put most of the logic into our `root/utils.py` file. Here is one way it could be divided:

![Split number guessing game flowchart](./split-number-guessing-game.webp)

This means that we can build out `root/utils.py` like this:

Import the random module because we need random number generation:

```python utils.py
import random
```

I also find it helpful whenever making a range to use constants instead of literal values throughout the code. This makes it easier to tweak values as we change our code:

```python utils.py
MAX = 100
MIN = 100
```

Here is our number generation function:

```python utils.py
def generate_secret_number():
    secret_number = random.randint(MIN, MAX)
    return secret_number
```

Here is our function for allowing user guesses:

```python utils.py
def check_user_guess(secret_number):
    guess = prompt_valid_guess()
    if guess == secret_number:
        print("Correct!")
        return True
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
    return False
```

And finally our input validation to ensure the user is providing valid input for the game:

```python utils.py
def prompt_valid_guess():
    while True:
        print(f"Guess a number between {MIN} and {MAX}")
        guess = input()
        try:
            guess = int(guess)
        except ValueError:
            print("Invalid guess.")
            print("Guess must be a number!")
            continue
        if guess > MAX:
            print("Invalid guess.")
            print(f"Out of range, cannot be greater than {MAX}")
            continue
        if guess < MIN:
            print("Invalid guess.")
            print(f"Out of range, cannot be lower than {MIN}")
            continue
        return guess
```

You'll notice that right now if you run this code, nothing happens! We should check to make sure that all of our functions are working properly, so after defining them, we will add some simple `print()` statements just to verify things are working:

```python utils.py
# Verify the secret number generator
number_to_print = generate_secret_number()
print(f"Secret number: {number_to_print}")

# Verify that the guess validation works on the secret number
for _ in range(3):
    print(f"Secret number: {number_to_print}")
    print("Check if the code can identify numbers above, numbers below, and a correct guess.")
    check_user_guess(number_to_print)
```

When we run our code, we should get a pretty clear idea of whether or not it works. At this point, we can move on to creating our actual game in `root/main.py`

## 4. Importing to `root/main.py`

If we want to actually use these functions we have created, we can import `root/utils.py` directly into `root/main.py`:

```python main.py

from root import utils
```

With that we can use the `root/utils.py` functions through the `utils` namespace:

```python main.py
secret_number = utils.generate_secret_number()

while True:
    if utils.check_user_guess(secret_number):
        break
```

This code will work just fine, but usually when you are creating your own modules, you want them imported directly into the main file's namespace.

## 5. Importing Directly into the `root/main.py` Namespace

To import them directly into `root/main.py`'s namespace, we can use the following code:

```python main.py
from root.utils import generate_secret_number, check_user_guess

secret_number = generate_secret_number()

while True:
    if check_user_guess(secret_number):
        break
```

Time to run our `root/main.py` file and see how it works!

Oh no! We get all of the `print()` statements from our other file!

```terminaloutput
Secret number: 72
Secret number: 72
Check if the code can identify numbers above, numbers below, and a correct guess.
Guess a number between 1 and 100
```

## 6. Preventing Unwanted Code From Running With `if __name__ == "__main__"`

When Python imports a module, it actually just runs the file! So that means that all of our test code gets run when imported! 

Your first thought to solve this problem might be to just delete the test code. But when you delete test code, your deleting valuable tests that provided you important debug information **and** from a teacher's perspective, evidence of your learning. So don't delete the test code!

Your next instinct might be to comment the test code out. In many projects however, as you continue to build out files, finding and commenting out test code is very cumbersome.

Fortunately, Python has a built-in solution! Whenever a file is run as the main file being run (i.e. hitting the play button on a file in PyCharm or VS Code), it is given a value for a hidden property called `__name__`. This value is always set to `"__main__"` for the main file being run. This means that you can prevent test code from running by placing it in a selection control structure that only runs when it's the main file!

Above your test code in `root/utils.py` add the following selection control structure:

```python utils.py
if __name__ == "__main__":
    # Test code for a module goes here
```

Then try running `root/utils.py`. You'll notice that it still runs like normal!

Now try running `root/main.py`. You'll notice that now it doesn't output all of the extra information from `root/utils.py`!

Including `if __name__ == "__main__"` for test code is a standard practice when creating Python modules and is expected to be used.

# Extension Activity: Modular Mayhem

Extend the Number Guessing Game by adding a second module that manages the player's score.

### Requirements

* Create a new module named `score.py` containing **all functions related to scoring**.
* The player starts with **100 points** and loses **10 points for every incorrect guess**. The score cannot go below `0`.
* Create a function in `score.py` that accepts the **current score** and returns the new score after an incorrect guess.
* Create a second function in `score.py` that accepts the **final score** and returns a rating: **80–100 = `"Excellent"`, 50–79 = `"Good"`, and 0–49 = `"Keep Practicing"`**.
* Import both functions into `root/main.py`. When the player correctly guesses the number, display their **final score and rating**.
* Program appropriately uses `__name__ == "__main__"` to prevent data from contaminating programs in other files.

