import random
import tkinter as tk

window = tk.Tk()
window.title("Number Guessing Game")

Name_Label = tk.Label(window, text="Enter Your Name")
Name_entry = tk.Entry(window)
name = str(Name_entry.get())
Name_Label.pack()
Name_entry.pack()

def W_User():
    welcome = tk.Label(window, text="Good day " + str(Name_entry.get()))
    welcome.pack()

welcome_button = tk.Button(window, text="Start", command=W_User)
welcome_button.pack()

enterGuess_Label = tk.Label(window, text="Enter the Guess")
enterGuess_Label.pack()
enterGuess = tk.Entry(window, text=0)
enterGuess.pack()

n = random.randrange(1,15)

def takeGuess():
    tries = 0
    userGuess = int(enterGuess.get())
    while tries<5:
        tries += 1
        if userGuess < n:
            warningLabel = tk.Label(window, text=" Your Guess was too Low")
            warningLabel.pack()
            break
        elif userGuess > n:
            warningLabel = tk.Label(window, text=" Your Guess was too High")
            warningLabel.pack()
            break
        elif userGuess == n:
            warningLabel = tk.Label(window, text="Bingo! Your Guess is right")
            warningLabel.pack()
            break
        else:
            warningLabel =tk.Label(window, )


guesButton = tk.Button(window, text="Play", command=takeGuess)
guesButton.pack()

def Rules():
    rules = tk.Toplevel(window)
    Rules_Label = tk.Label(rules, text="1. You can Guess Any number between 1-15\n 2. You have only five chances\n ")
    Rules_Label.pack()

rules_Button = tk.Button(window, text="Rules", command=Rules)
rules_Button.pack()

window.mainloop()