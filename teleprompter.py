"""
Just a trial at making a simple teleprompter for guitar notes
The idea is, given a collection of notes, these will be shown on the screen one-by-one
Strumming pattern -> D-D-D-DU-UD-DUDU
16 strokes in ~3.6s for this song => ~0.225 for each stroke(?)
Guitar tutorial - https://www.youtube.com/watch?v=7sc0oB46uc4
Song - Cardigan by Taylor Swift
For a different song, will have to change the strumming pattern and the notes AND the sleep time
"""
import time
from termcolor import colored
from os import system
import platform

def playSong(colour):
    
    """Detect OS name to choose the correct string to clear the display"""
    OSName = platform.system()
    clearStr = "clear"
    if OSName=='Windows':
        clearStr='cls'

    system(clearStr)
    getReady = 4
    while getReady > 0:
        getReady -= 1
        print(getReady)
        time.sleep(1)
        system(clearStr)

    strummingPattern = "D-D-D-DU-UD-DUDU"
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
    
    for k in range(len(notes)):
        """Split each line of the notes into consituent chords"""
        chords = notes[k].split(',')

        for indChords in range(len(chords)):
            for indStrumming in range(len(strummingPattern)):
                m = 0
                j = 0

                """Loop to colour the current chord"""
                while j < len(chords):
                    if j == indChords:
                        print(colored(chords[j], colour), end=" ")
                    else:
                        print(chords[j], end=" ")
                    j += 1
                print()
                
                """Loop to highlight the current strumming pattern to play ie D or U"""
                while m < len(strummingPattern):
                    if m == indStrumming:
                        """Keeping the commented part incase a future update wants to revert the dash highlighting behaviour"""
                        # if strummingPattern[m] == '-':
                        #     print(strummingPattern[m], end="")
                        # else:
                        print(colored(strummingPattern[m], colour), end="")
                    else:
                        print(strummingPattern[m], end="")
                    m += 1
                print()

                """This prints the next line to play"""
                if k != len(notes) - 1:
                    print(notes[k + 1])
                
                time.sleep(0.22)
                system(clearStr)
    time.sleep(1)
    print("Fin.")


if __name__=="__main__":
    """Colour can be 'red', 'green', 'blue', 'white', 'black', etc. More colours can be found on the homepage of termcolor
     https://github.com/termcolor/termcolor?tab=readme-ov-file#text-properties """
    colour = 'magenta'
    playSong(colour)