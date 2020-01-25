import time
import sys

def sprint(string="[+] This is a test!!", tm=5, color="normal"):
    color = color.lower()
    string = str(string)
    if (color != "normal"):
        if (color == "red"):
            string = "\033[31m" + string
        elif (color == "green"):
            string = "\033[32m" + string
        elif (color == "blue"):
            string = "\033[34m" + string
        elif (color == "yellow"):
            string = "\033[93m" + string
        elif (color == "orange"):
            string = "\033[33m" + string

    for c in string + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(tm / 100)

sprint("1337 future is loading...", 3, "red")
sprint("1337 future is loading...", 3, "green")
sprint("1337 future is loading...", 3, "blue")
sprint("1337 future is loading...", 3, "yellow")
sprint("1337 future is loading...", 3, "orange")
