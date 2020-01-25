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

sprint("Print Red Text", 5, "red")
sprint("Print Green Text", 5, "green")
sprint("Print Blue Text", 5, "blue")
sprint("Print Yellow Text", 5, "yellow")
sprint("Print Orange Text", 5, "orange")