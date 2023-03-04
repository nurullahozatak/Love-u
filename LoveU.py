import os
import time

myMessage = "I LOVE YOU"

alphabet = list("ABCDEFGHIJKLMNOPRQSTUVYZXW")

def clear_console():
    if os.name == 'nt':  # for Windows
        os.system('cls')
    else:  # for Linux and Mac
        os.system('clear')

greeting = ""
for i in range(0, len(myMessage)):
    if i == 1 or i == 6:
        greeting = greeting + " "
        clear_console()
    for j in range(0 , len(alphabet)):
        if myMessage[i] == alphabet[j]:
            print(greeting + alphabet[j])
            greeting = greeting + myMessage[i]
            time.sleep(0.05)
            clear_console()
            break
        else:
            print(greeting + alphabet[j])
            time.sleep(0.05)
            clear_console()

print(f"\n\n","                                              ╰(✿´⌣`✿)╯♡", myMessage, "<3", "\n\n")

