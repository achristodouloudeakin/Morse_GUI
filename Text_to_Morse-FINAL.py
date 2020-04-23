import tkinter as tk
from tkinter import StringVar
import RPi.GPIO as gpio
from time import sleep
from gpiozero import LED


gpio.setmode(gpio.BCM)
red = LED(24)
red.off()


def short_beep():
    red.off()
    sleep(0.025)
    red.on()
    sleep(0.4)
    red.off()
    sleep(0.025)


def long_beep():
    red.off()
    sleep(0.025)
    red.on()
    sleep(1)
    red.off()
    sleep(0.025)


def char_to_morse(character_x):
    if str(character_x) == "a":
        short_beep()
        long_beep()

    elif str(character_x) == "b":
        long_beep()
        short_beep()
        short_beep()
        short_beep()

    elif str(character_x) == "c":
        long_beep()
        short_beep()
        long_beep()
        short_beep()

    elif str(character_x) == "d":
        long_beep()
        short_beep()
        short_beep()

    elif str(character_x) == "e":
        short_beep()

    elif str(character_x) == "f":
        short_beep()
        short_beep()
        long_beep()
        short_beep()

    elif str(character_x) == "g":
        long_beep()
        long_beep()
        short_beep()

    elif str(character_x) == "h":
        short_beep()
        short_beep()
        short_beep()
        short_beep()

    elif str(character_x) == "i":
        short_beep()
        short_beep()

    elif str(character_x) == "j":
        short_beep()
        long_beep()
        long_beep()
        long_beep()

    elif str(character_x) == "k":
        long_beep()
        short_beep()
        long_beep()

    elif str(character_x) == "l":
        short_beep()
        long_beep()
        short_beep()
        short_beep()

    elif str(character_x) == "m":
        long_beep()
        long_beep()

    elif str(character_x) == "n":
        long_beep()
        short_beep()

    elif str(character_x) == "o":
        long_beep()
        long_beep()
        long_beep()

    elif str(character_x) == "p":
        short_beep()
        long_beep()
        long_beep()
        short_beep()

    elif str(character_x) == "q":
        long_beep()
        long_beep()
        short_beep()
        long_beep()

    elif str(character_x) == "r":
        short_beep()
        long_beep()
        short_beep()

    elif str(character_x) == "s":
        short_beep()
        short_beep()
        short_beep()

    elif str(character_x) == "t":
        long_beep()

    elif str(character_x) == "u":
        short_beep()
        short_beep()
        long_beep()

    elif str(character_x) == "v":
        short_beep()
        short_beep()
        short_beep()
        long_beep()

    elif str(character_x) == "w":
        short_beep()
        long_beep()
        long_beep()

    elif str(character_x) == "x":
        long_beep()
        short_beep()
        short_beep()
        long_beep()

    elif str(character_x) == "y":
        long_beep()
        short_beep()
        long_beep()
        long_beep()

    elif str(character_x) == "z":
        long_beep()
        long_beep()
        short_beep()
        short_beep()

    else:
        red.off()
        sleep(1)


root = tk.Tk()
text_str = StringVar()
canvas_1 = tk.Canvas(root, width=400, height=300)
canvas_1.pack()

entry_1 = tk.Entry(root)
canvas_1.create_window(200, 140, window=entry_1)
text_str = StringVar()

def main():

    user_text = entry_1.get()

    char_list = list(user_text)
    total_characters = int(len(char_list))

    if total_characters > 12:
        label_1 = tk.Label(root, textvariable=text_str)
        text_str.set("Please keep the word bellow 12 letters")
        canvas_1.create_window(200, 230, window=label_1)

    else:
        for x in char_list:
            char_to_morse(x)

        label_1 = tk.Label(root, textvariable=text_str)
        text_str.set("Completed")
        canvas_1.create_window(200, 230, window=label_1)


button_1 = tk.Button(text="Enter text", command=main)
canvas_1.create_window(200, 300, window=button_1)


root.mainloop()
