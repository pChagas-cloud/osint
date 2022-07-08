#!/bin/python3
from pyautogui import write
from pyautogui import press
from time import sleep
import sys

def help():
    print("""

            --file      reads from file     spam --file <filename.txt>

            --default   default             spam --default


            """)

def default():
    print("Type message: ")
    x = input()
    print("Delay: ")
    t = float(input())
    print("N?")
    n = int(input())
    s=5;
    for i in range(5):
        print(f"spamming in {s} seconds");
        s-=1;
        sleep(1);
    for i in range(n):
        write(x);
        press('enter')
        sleep(t)

def from_file(file):
    f=open(file,'r')
    x=f.readlines()
    f.close()
    print("Delay: ")
    t = float(input())
    print("N?")
    n = int(input())
    s=5;
    for i in range(5):
        print(f"spamming in {s} seconds");
        s-=1;
        sleep(1);
    for i in range(n):
        write(x);
        press('enter')
        sleep(t)

def noves():
    print("Delay: ")
    t = float(input())
    print("N?")
    n = int(input())
    s=5;
    for i in range(5):
        print(f"spamming in {s} seconds");
        s-=1;
        sleep(1);

    x="9?"

    for i in range(n):
        write(x);
        x=x.replace("?","")
        x=f"{x}9?"
        press('enter')
        sleep(t)


y=sys.argv[1]

if y == "-d" or y=="--default":
    default()
elif y=="-f" or y=="--file":
    from_file(sys.argv[2])
elif y=="-n" or y=="--nove":
    noves()






