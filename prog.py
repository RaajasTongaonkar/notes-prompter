# Just a trial at making a teleprompter for guitar notes
# The idea is, given a collection of notes, these will be shown on the screen one-by-one
# Strumming pattern -> D-D-D-DU-UD-DUDU
# 16 strokes in ~3.6s for this song => ~0.225 for each stroke(?)
# https://www.youtube.com/watch?v=7sc0oB46uc4
# cardigan - Taylor Swift
# For a different song, change the strumming pattern and the notes AND the sleep time

import time
from termcolor import colored
from os import system
system('cls')
t = 4
while t > 0:
    t -= 1
    print(t)
    time.sleep(1)
    system('cls')

strumming = "D-D-D-DU-UD-DUDU"
notes = [
    "Dm,G,F,G",
    "Dm,G,F,G",
    "C,G,F,G",
    "Dm,G,F,G",
    "Dm,G,F,G",
    "C,G,F,G",
    "F,Am,C,F",
    "F,Am,G,F",
    "F,Am,G,F",
    "C,G,F,G",
    "C,G,F,G",
    "C,G,F,G",
    "C,G,F,G",
    "Dm,G,F,G",
    "F,Am,C,F"
]
# print(notes[0])
# words = ['Dm','G','F','G']
for k in range(len(notes)):
    words = notes[k].split(',')
    # print(words)
    for i in range(len(words)):
        for l in range(len(strumming)):
            m = 0
            j = 0
            while j < len(words):
                if j == i:
                    print(colored(words[j], 'red'), end=" ")
                else:
                    print(words[j], end=" ")
                j += 1
            print()
            while m < len(strumming):
                # if (m == l) & (strumming[m] != '-'):
                #     print(colored(strumming[m], 'red'), end="")
                if m == l:
                    if strumming[m] == '-':
                        print(strumming[m], end="")
                    else:
                        print(colored(strumming[m], 'red'), end="")
                else:
                    print(strumming[m], end="")
                m += 1
            print()
            if k != len(notes) - 1:
                print(notes[k + 1])
            time.sleep(0.22)
            system('cls')


