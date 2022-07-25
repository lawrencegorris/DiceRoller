# DICE ROLLER

## About this project

Found this somewhere as a beginner project idea and decided to make my own version of it.

It asks for how many dice of what type you want to roll.
After giving input it sleeps for some time (replicating rolling the dice)
And then gives the output to the user.
Asks if user wants to roll more or quit.
Console clear when choosing to roll again.

## Running this project

Basic .py file you can run in the console by typing:
python or python3 diceroller.py

You can also create a .exe file by pip installing pyisntaller and then running it.
I used:

pyinstaller --onefile diceroller.py

That way it creates only a single .exe file in the dist directory.

## Future:
Might add some things in the future like a gui (with tkinter), a message that appears upon a crit hit or crit miss and options to roll multiple dice of multiple types. 
ex. rolling 1d6 alongside 2D4 and then printing out:
D6: [3]
D4: [2, 1]
