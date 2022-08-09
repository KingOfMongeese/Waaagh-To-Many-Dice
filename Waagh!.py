import random
import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.title("Waaagh! To Many Dice")

numOfDice_start = tk.IntVar()
ones = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0

tk.Label(window, text='Number of dice to roll: ', font=('calibre', 12)).grid(row = 0)
diceEntry = tk.Entry(window, textvariable= numOfDice_start, font = ('calibre', 12)).grid(row = 0, column = 1)


def roll(numOfDice):

    global ones, twos, threes, fours, fives, sixes

    count = 0
    t = [1,2,3,4,5,6]
    while count < numOfDice:
        outcome = random.choice(t)
        match outcome:
            case 1:
                ones += 1
            case 2:
                twos += 1
            case 3:
                threes += 1
            case 4:
                fours += 1
            case 5:
                fives += 1
            case 6:
                sixes += 1
        count += 1
    output_string = 'Outcome:\n1: ' + str(ones) + '\n2: ' + str(twos) + "\n3: " + str(threes) + "\n4: " + str(fours) + "\n5: " + str(fives) + "\n6: " + str(sixes)
    dialogue = tk.Label(window, text=output_string, font=('calibre', 12)).grid(row = 2, columnspan= 2)
    ones = 0
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    sixes = 0





def showLicense():
    global system
    Ltext =""
    with open("LICENSE.txt") as file:
        for line in file:
            Ltext += line
    licenseWindow = tk.Toplevel(window)
    licenseWindow.title("MIT License")
    text = tk.Label(licenseWindow, text=Ltext)
    text.pack()


def rollWaaagh():
    try:
        numOfDice = numOfDice_start.get()
        roll(numOfDice)
    except:
        tkinter.messagebox.showinfo("Error", "Try entring only numbers for input.")



if __name__ == '__main__':
    roll_btn = tk.Button(window, text='Roll Lots of Dice!', command=rollWaaagh).grid(row = 1)
    license_button = tk.Button(window, text='View License', command= showLicense).grid(row = 1, column=1)
    window.mainloop()