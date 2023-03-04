import colorama
from colorama import Fore as fill
from colorama import Back as bkgd
from colorama import Style as opac
import time
import random
from random import randint as Xn
import sys 
import os
import cursor
import string

colorama.init(autoreset=True)
speed = 0.05
CURSOR_UP_ONE = '\x1b[1A' 
ERASE_LINE = '\x1b[2K'
RESET = '\u001b[0m'
def flush():
    sys.stdout.flush
#-------------------------------COLOURS-----------------------------
def rgb(r,g,b): 
    return (f"\u001b[38;2;{r};{g};{b}m")
rad = rgb(207, 180, 48)
radhush = rgb(133, 118, 49)

def erase(n=1): 
    for _ in range(n): 
        sys.stdout.write(ERASE_LINE)

def backtrack(n=1): 
    for _ in range(n): 
        sys.stdout.write(CURSOR_UP_ONE)

def clear():
    os.system('cls')

def readred(s):
    colour = rgb(255,0,0)
    for c in s:
        print(colour + c, end='')
        time.sleep(speed)

def read(s):
    for c in s:
        print(c, end='')
        time.sleep(speed)
    time.sleep(1)

def readfast(s):
    for c in s:
        print(c, end='')
        time.sleep(speed/5)
    time.sleep(1)

def readslow(s):
    for c in s:
        print(c, end='')
        time.sleep(speed*10)
    time.sleep(1)

def radio(s):
    for c in s:
        print(rad + c, end='')
        time.sleep(speed)
    time.sleep(1)

def radiofast(s):
    for c in s:
        print(rad + c, end='')
        time.sleep(speed/5)
    time.sleep(1)

def radioslow(s):
    for c in s:
        print(rad + c, end='')
        time.sleep(speed*10)
    time.sleep(1)

def radiostrong(s):
    for c in s:
        print(fill.YELLOW + opac.BRIGHT + c, end='')
        time.sleep(speed/5)
    time.sleep(1)

def radiohush(s):
    for c in s:
        print(rad + c, end='')
        time.sleep(speed*5)
    time.sleep(1)

def readtut(s):
    for c in s:
        print(fill.GREEN + opac.BRIGHT + c, end='')
        time.sleep(speed/5)
    time.sleep(1)

def readbats(s):
    for c in s:
        print(fill.CYAN + opac.BRIGHT + c, end='')
        time.sleep(speed/5)
    time.sleep(0.5)
    
def batsdata(s):
    print(rgb(126, 234, 252) + s, end='') 

def printfade(s):
    for n in range(1,255):
        grey = rgb(n,n,n)
        print(grey + s, end="\r")
        time.sleep(0.001)
    time.sleep(1)
    for n in reversed(range(1,255)):
        grey = rgb(n,n,n)
        print(grey + s, end="\r")
        time.sleep(0.001)
    erase(1)

def printfadein(s):
    for n in range(1,254,2):
        grey = rgb(n,n,n)
        print(grey + s, end="\r")
        time.sleep(0.0001)
    time.sleep(1)

def printfadeout(s):
    for n in reversed(range(1,254,2)):
        grey = rgb(n,n,n)
        print(grey + s, end="\r")
        time.sleep(0.0001)
    erase(1)

def readfade(s):
    for c in s:
        print(c, end='')
        time.sleep(speed)
    print('', end="\r")
    time.sleep(1)
    for n in reversed(range(1,255)):
        grey = rgb(n,n,n)
        print(grey + s, end="\r")
        time.sleep(0.001)
    erase()



def scram(s,d):
    cno = 0
    delay = 0
    o = []
    while cno < len(s):
        n = Xn(30+cno,200)
        g = random.choices(string.ascii_letters, k=cno)
        print(rgb(n,n,n) + ''.join(g), end='\r')
        cno += 1
        time.sleep(speed)
    flush()
    while delay <= 10:
        n = Xn(100,200)
        g = random.choices(string.ascii_letters, k=cno)
        print(rgb(n,n,n) + ''.join(g), end='\r')
        delay += 1
        time.sleep(speed)
    print("\r", end='')
    flush()
    for c in s:
        o.append(c)
        g = random.choices(string.ascii_letters, k=cno-1)
        print(''.join(o) + ''.join(g), end='\r')
        cno -=1
        time.sleep(speed)
    flush()
    time.sleep(d)

def scramred(s,d):
    cno = 0
    delay = 0
    o = []
    while cno < len(s):
        n = Xn(30+cno,200)
        g = random.choices(string.ascii_letters, k=cno)
        print(rgb(n+cno,n,n) + ''.join(g), end='\r')
        cno += 1
        time.sleep(speed)
    flush()
    while delay <= 15:
        n = Xn(100,255)
        m = n%100
        g = random.choices(string.ascii_letters, k=cno)
        print(rgb(n,m,m) + ''.join(g), end='\r')
        delay += 1
        time.sleep(speed)
    flush()
    print("\r", end='')
    for c in s:
        n = Xn(150,255)
        m = n%50
        o.append(c)
        g = random.choices(string.ascii_letters, k=cno-1)
        print(rgb(n,m,m) + ''.join(o) + ''.join(g), end='\r')
        cno -=1
        time.sleep(speed)
    print(rgb(215,0,0) + s)
    flush()
    time.sleep(d)

def scramfade(s):
    scram(s,0.5)
    printfadeout(s)
    time.sleep(1)
    erase()

def radioscram(s):
    scram(s,0)
    radiostrong(s)

