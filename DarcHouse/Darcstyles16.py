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
import rooms

colorama.init(autoreset=True)
speed = 0.05
CURSOR_UP_ONE = '\x1b[1A' 
ERASE_LINE = '\x1b[2K'
RESET = '\u001b[0m'
def rgb(r,g,b): 
    return (f"\u001b[38;2;{r};{g};{b}m")

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
        print(fill.YELLOW + c, end='')
        time.sleep(speed)
    time.sleep(1)

def radiofast(s):
    for c in s:
        print(fill.YELLOW + c, end='')
        time.sleep(speed/5)
    time.sleep(1)

def radioslow(s):
    for c in s:
        print(fill.YELLOW + c, end='')
        time.sleep(speed*10)
    time.sleep(1)

def radiostrong(s):
    for c in s:
        print(fill.YELLOW + opac.BRIGHT + c, end='')
        time.sleep(speed/5)
    time.sleep(1)

def radiohush(s):
    for c in s:
        print(fill.YELLOW + opac.DIM + c, end='')
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
    print(fill.CYAN + opac.DIM + s, end='') 

def printfade(s):
    print(fill.BLACK + opac.NORMAL + s, end='\r')
    time.sleep(1)
    print(fill.BLACK + opac.BRIGHT + s, end='\r')
    time.sleep(1)
    print(fill.WHITE + opac.NORMAL + s, end='\r')
    time.sleep(1)
    print(fill.WHITE + opac.BRIGHT + s, end='\r')
    time.sleep(1)
    print(fill.WHITE + opac.NORMAL + s, end='\r')
    time.sleep(1)
    print(fill.BLACK + opac.BRIGHT + s, end='\r')
    time.sleep(1)
    print(fill.BLACK + opac.NORMAL + s, end='\r')
    time.sleep(1)
    erase(1)

def readfade(s):
    for c in s:
        print(c, end='')
        time.sleep(speed)
    print('', end="\r")
    time.sleep(2)
    print(fill.BLACK + opac.BRIGHT + s, end="\r")
    time.sleep(1)
    erase()

def scram(s,d):
    cno = 0
    delay = 0
    o = []
    while cno < len(s):
        g = random.choices(string.ascii_letters, k=cno)
        print(fill.BLACK + opac.BRIGHT + ''.join(g), end='\r')
        cno += 1
        time.sleep(speed)
    while delay <= 10:
        g = random.choices(string.ascii_letters, k=cno)
        print(fill.BLACK + opac.BRIGHT + ''.join(g), end='\r')
        delay += 1
        time.sleep(speed)
    print("\r", end='')
    for c in s:
        o.append(c)
        g = random.choices(string.ascii_letters, k=cno-1)
        print(''.join(o) + ''.join(g), end='\r')
        cno -=1
        time.sleep(speed)
    time.sleep(d)

def scramred(s):
    cno = 0
    delay = 0
    o = []
    while cno < len(s):
        g = random.choices(string.ascii_letters, k=cno)
        print(fill.BLACK + opac.BRIGHT + ''.join(g), end='\r')
        cno += 1
        time.sleep(speed)
    while delay <= 10:
        g = random.choices(string.ascii_letters, k=cno)
        print(fill.BLACK + opac.BRIGHT + ''.join(g), end='\r')
        delay += 1
        time.sleep(speed)
    print("\r", end='')
    for c in s:
        o.append(c)
        g = random.choices(string.ascii_letters, k=cno-1)
        print(fill.RED + opac.BRIGHT + ''.join(o) + ''.join(g), end='\r')
        cno -=1
        time.sleep(speed)
    time.sleep(1)
    print('', end="\r")
    print(fill.RED + opac.NORMAL + s, end="\r")
    time.sleep(1)
    erase()

def scramfade(s):
    scram(s,2)
    print('', end="\r")
    print(fill.BLACK + opac.BRIGHT + s, end="\r")
    time.sleep(1)
    erase()

def radioscram(s):
    scram(s,0)
    radiostrong(s)

