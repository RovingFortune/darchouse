#------------------IMPORTS---------------------
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


#-------------------UNIVERSALS------------------
colorama.init(autoreset=True)
cursor.hide()
shift = False
tutor = True
safe = False
speed = 0.05
locno = 0
fail = "⌂H: Negative copy, ☼Sunshine - try something else.\n"
pingno = 0
CURSOR_UP_ONE = '\x1b[1A' 
ERASE_LINE = '\x1b[2K'

#-------------------INVENTORIES------------------
pack = []
hand = []
mixer = []
access = []
perimeterjunk = []
frontjunk = []
junk = [perimeterjunk, frontjunk]
locname = ["PERIMETER", "FRONT YARD"]
locdesc = [" A clearing in a forest, set back from the dirt road that brought you here. An area that may have been a garden once,\n now terribly overgrown sprawls out on either side. \n Before you, the spherical border of the DARK ZONE curves away from you into the night.\n", "Front placeholder\n"]
canmix = ["TOWER B", "WIRE"]
blends = ["WIRE+TOWER B", "TOWER B+WIRE"]

#-------------------TEXT STYLES------------------

def erase(n=1): 
    for _ in range(n): 
        sys.stdout.write(ERASE_LINE)

def backtrack(n=1): 
    for _ in range(n): 
        sys.stdout.write(CURSOR_UP_ONE)

def clear():
    os.system('cls')


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
        time.sleep(3)

def readbats(s):
    for c in s:
        print(fill.CYAN + opac.BRIGHT + c, end='')
        time.sleep(speed/5)
    time.sleep(1)
    
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




#-------------------COMMANDS--------------------
def take(c):
    hand.append(c)
    pack.remove(c)
    readbats("[BATS]:" + str(c) + " is in your hand.\n")
    return
    
def stash(c):
    pack.append(c)
    hand.remove(c)
    readbats("[BATS]:" + str(c) + " placed in pack.\n")
    return

def openpack():
    readbats("\n[PACK]:\n")
    for item in pack:
        print("• " + str(item))
    def inpack():
        cursor.show()
        c = input("\nITEM:")
        c = c.upper()
        cursor.hide()
        if c in pack:
            take(c)
        elif c in hand:
            stash(c)
        elif c in ["BACK"]:
            return
        else: 
            radiofast("⌂H: Sorry, ☼Sunshine, fresh out of that.")
            openpack()
    inpack()

def pickup(c):
    hand.append(c)
    junk[locno].remove(c)
    readbats("[BATS]: " + str(c) + " is in your hand.\n")
    return
    
def putdown(c):
    junk[locno].append(c)
    hand.remove(c)
    readbats("[BATS]: " + str(c) + " dropped.\n")
    return
'''
def goto(l):
    if l in access:
'''

    

def ping():
    global pingno
    readbats("\n[BATS READOUT: PING " + f"{pingno:03}" + "]\n")
    pingno += 1
    print("Location: " + str(locname[locno]))
    if len(junk[locno]) == 1:
        print(str(locdesc[locno]) + " There is a " + junk[locno][0] + " on the ground.")
    elif len(junk[locno]) == 0:
        print(str(locdesc[locno]))
    else:
        print(" Objects in the vicinity:")
        for item in junk[locno]:
            print("• " + str(item))
    def insurvey():
        cursor.show()
        c = input("COMMAND:")
        c = c.upper()
        cursor.hide()
        if c in junk[locno]:
            if len(hand) < 5:
                pickup(c)
            else:
                if len(pack) < 5:
                    readbats("[BATS]: Your hands are full, but you can fit that in your pack.\n")
                    pack.append(c)
                    junk[locno].remove(c)
                else:
                    radiofast("⌂H: Slow down there, you're way too overloaded to do anything with that.\n")
                    insurvey()
        elif c in hand:
            putdown(c)
        elif c in ["BACK"]:
            return
        else: 
            radiofast("⌂H: Sorry, ☼Sunshine, nothing like that around these parts.")
            ping()
    insurvey()

def place():
    j = junk[locno]
    if len(hand) == 1:
        j.append(hand[0])
        readbats("[BATS]: " + str(hand[0]) + " placed.\n")
        hand.clear()
    elif len(hand) == 0:
        readbats("[BATS]: You're not holding anything.\n")
    else:
        def placeselect():
            readfast("⌂H: What do you want to place?\n")
            for item in hand:
                print("• " + str(item))
            cursor.show()
            i = input("ITEM:")
            i = i.upper()
            cursor.hide()
            if i in hand:
                j.append(i)
                hand.remove(i)
                readbats("[BATS]: " + str(i) + " placed.\n")
            elif i in ["BACK"]:
                return
            else:
                readbats("[BATS]: You're not holding that.\n")
                placeselect()
        placeselect()

def blend(x):
    if x in ["WIRE+TOWER B", "TOWER B+WIRE"]:
        return str("WIRED TOWER")
    else:
        return x

def mix():
    readbats("[BATS]: What are you combining with your " + str(mixer[0]) + "?\n")
    cursor.show()
    m = input("COMBINE:")
    m = m.upper()
    cursor.hide()
    x = str(str(m) + "+" + str(mixer[0]))
    if m in canmix:
        if x in blends:
            if m in mixer:
                readbats("[BATS]: You can't mix that with itself.\n")
                mix()
            elif m in hand:
                hand.remove(m)
            elif m in pack:
                pack.remove(m)
            elif m in junk[locno]:
                junk[locno].remove(m)
            elif m in ["BACK"]:
                hand.append(mixer[0])
                mixer.clear()
                return
            y = blend(x)
            hand.append(y)
            readbats("[BATS]: " + y + " is now in your hand.\n")
        else:
            radiofast("⌂H: Not a winning combination, those two - try something else.\n")
            mix()
    else:
        radiofast("⌂H: Good start, but you can't combine your " + str(mixer[0]) + " with that.\n")
        mix()
    mixer.clear()

def combine():
    if len(hand) == 1:
        if hand[0] in canmix:
            mixer.append(hand[0])
            hand.clear()
            mix()
        else:
            radiofast("⌂H: No can do - can't combine that " + str(hand[0]) + " with anything.\n")
            return
    elif len(hand) == 0:
        readbats("[BATS]: You're not holding anything.\n")
        return
    else:
        def combineselect():
            readbats("[BATS]: What do you want to combine?\n")
            for item in hand:
                print("• " + str(item))
            cursor.show()
            i = input("COMBINE:")
            i = i.upper()
            cursor.hide()
            if i in canmix:
                if i in hand:
                    mixer.append(i)
                    mix()
                elif i in ["BACK"]:
                    return
                else:
                    readbats("[BATS]: You're not holding that.\n")
                    combineselect()
            else:
                radiofast("⌂H: No can do - can't combine that with anything.\n")
                combineselect()
        combineselect()

def openhand():
    for item in hand:
        readbats("[BATS]: You are holding:")
        print("• " + str(item))
        return

def command():
    cursor.show()
    a = input("COMMAND:")
    a = a.upper()
    cursor.hide()
    if a in ["PLACE"]:
        place()
    elif a in ["PACK"]:
        openpack()
    elif a in ["PING"]:
        ping()
    elif a in ["COMBINE"]:
        combine()
    elif a in ["HAND"]:
        openhand()
    elif a in ["HELP"]:
        readbats("[BATS] COMMAND LIST:")
        print("HAND: See what you are holding.")
        print("PACK: Open your inventory.")
        print("PING: Scan the area for details, including exits and objects in the vicinity.")
        print("PLACE: Put an object from your HAND down.")
        print("COMBINE: Add an object in your HAND to another object in your HAND, your PACK or in the vicinity.")
        command()
    elif a in ["BACK"]:
        return
    else:
        readfast(fail)
        command()

#--------------------MONSTER------------------
def sing():
    time.sleep(Xn(300,1200))
    print("♪")
    time.sleep(120)
    print("♫")
    time.sleep(3)
    readslow("⌂: Did you hear that?\n")
    time.sleep(2)
    read("⌂: ⌂Homebase to ☼Sunshine, we're getting some interference - running channel check.\n")
    time.sleep(90)
    readslow("♫♪")

#---------------------STORY-------------------

def prologue():
    radio("⌂H: Radio check.\n\n") 
    time.sleep(2)
    clear()
    radio("⌂H: ⌂Homebase to ☼Sunshine, come in ☼Sunshine.\n\n")
    time.sleep(2)
    clear()
    radio("⌂H: Check check, radio check one-two, uh, Tango Tango Foxtrot Rumba che-\n")
    radiostrong("☼S: Would you shut the fuck up? I hear you.\n")
    time.sleep(1)
    radio("⌂H: Uh, ⌂Homebase to ☼Sunshine, that's a negative copy. Please observe radio protocol on check.\n\n")
    time.sleep(2)
    radio("⌂H: ...check.\n\n")
    radio("☼S:")
    radiohush(" *sigh*")
    radio(" Goddamnit.\n")
    radio("☼S: ☼Sunshine to ⌂Homebase, affirmative check, reading five by five.\n")
    time.sleep(1)
    radio("⌂H: Affirmative, ☼Sunshine, check is good, channel secure.\n")
    time.sleep(1)
    radio("☼S: Good. Now, ⌂Homebase?\n")
    radio("⌂H: Yes, ☼Sunshine?\n")
    time.sleep(2)
    radiostrong("☼S: Shut the fuck up.\n" )
    time.sleep(1)
    radio("⌂H: Such hostility on an official channel.\n")
    radio("☼S: I'll show you some hostility on your unofficial channel in a minute. Who made you comms op anyway?\n")
    time.sleep(1)
    radio("⌂H: I believe that was you.\n")
    radio("☼S: Remind me to kick myself when I get out of here.\n")
    radio("⌂H: Roger that, ☼Sunshine, kick reminder set. Approaching DARK ZONE now.\n")
    time.sleep(1)
    radio("☼S: Holy shit.\n")
    radio("⌂H: Affirmative, ☼Sunshine. What are you seeing?\n")
    radio("☼S: It's like... a dome, uh - a perfect hemisphere of just... nothing. Like a chunk just got carved\n    straight out of space.\n")
    time.sleep(3)
    radio("⌂H: Roger - GO TO the PERIMETER and set up the hardline so we can communicate with you inside.\n\n\n")

def run():
    radiostrong("☼S: No, no I can't do this!\n")
    radio("⌂H: What? What are you talking about?\n")
    radiostrong("☼S: I can't do this, it's not right, I'm getting the fuck out of here!\n")
    time.sleep(1)
    radio("⌂H: Come on, ☼Sunshine, you can't bail now - you're right there!\n")
    radiostrong("☼S: Fuck you, I'm out of this chicken shit outfit. Come do it yourself.\n")
    time.sleep(1)
    radio("⌂H: ☼Sunshine, if you leave now you know what will happen.\n\n")
    radiohush("☼S:.....\n\n")
    radio("⌂H: ☼Sunshine?\n\n")
    radiohush("☼S:.....\n\n")
    time.sleep(2)
    radiohush("⌂H: *sigh*\n\n")
    time.sleep(2)
    radio("⌂H: ⌂Homebase to †Damocles, ☼Sunshine is rogue. Initiate Hudson Protocol, codeword: sunset.\n")
    radio("†D: Roger.\n\n")
    time.sleep(4)
    radio("†D: ☼Sunshine is down.\n")
    time.sleep(2)
    radio("⌂H: Roger that, †Damocles, stand down.\n\n\n")
    radiohush("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n⌂H: Game over, man... game over.\n\n\n")
    time.sleep(3)
    print(fill.RED + "ENDING ZERO: EL RIESGO SIEMPRE VIVE")
    sys.exit()

def tutorial():
    readtut("[[TUTORIAL]]: Type GO TO PERIMETER to advance - commands are not case sensitive.\n")
    def tperi():
        cursor.show()
        c = input("COMMAND:")
        cursor.hide()
        if c.upper() in ["GO TO PERIMETER"]:
            pass
        elif c.upper() in ["RUN"]:
            run()      
        else:
            readfast(fail)
            tperi()
    tperi()
    radio("\n☼S: Approaching perimeter. It's getting cold...\n")
    radio("⌂H: Roger, ☼Sunshine, temperature has dropped by 1.4 Kelvin and falling. It should theoretically \n    come back up on the other side.\n")
    radio("☼S: Theoretically?\n")
    radio("⌂H: You know as much as we do about this place - probably more since you're\n    actually on the ground. Now, we can't get any signals into or out of that\n    thing, so you'll need to set up a hardline. PLACE the first TOWER from your PACK \n    outside the PERIMETER.\n\n")
    global shift
    while shift is False:
        readtut("[[TUTORIAL]]: Type PACK to open your inventory.\n")

        def tpack():
            pack.append("TOWER A")
            pack.append("TOWER B")
            pack.append("WIRE")
            cursor.show()
            c = input("COMMAND:")
            cursor.hide()
            if c.upper() in ["PACK"]:
                pass
            elif c.upper() in ["RUN"]:
                run()      
            else:
                readfast(fail)
                tpack()
        tpack()
        readtut("[[TUTORIAL]]: Type TOWER A to take it out of your PACK and put it in your HAND.\n")
        openpack()
        if len(hand) == 1 and hand[0] == "TOWER A":
            shift = True
        else:
            readfast(fail)
    shift = False
    while shift is False:
        readtut("[[TUTORIAL]]: You can hold up to 5 items in your PACK.\n              You can also hold up to 5 items in your HAND but holding too many items \n              may make some things more difficult, or stop you from doing other things entirely.\n")
        readtut("              Now type PLACE to put the object in your HAND on the ground.\n")
        command()
        if len(junk[locno]) == 1 and junk[locno][0] == "TOWER A":
            shift = True
        readtut("[[TUTORIAL]]: " + junk[locno][0] + " is now on the ground. You can PLACE as many items\n              from your HAND on the ground as you want, but too much junk lying around could get in your way.\n" )
        time.sleep(1)
    radio("⌂H: First Tower is transmitting, ☼Sunshine - attach the WIRE to the second TOWER and take it \n    through the PERIMETER.\n")
    shift = False
    while shift is False:
        readtut("[[TUTORIAL]]: Type PACK to open your inventory and take out TOWER B. \n")
        command()
        if len(hand) == 1 and hand[0] == "TOWER B":
            readtut("[[TUTORIAL]]: Now type COMBINE to add the WIRE to TOWER B. \n")
            command()
            if len(hand) == 1 and hand[0] == "WIRED TOWER":
                shift = True
            else:
                readfast(fail)
                hand.clear()
                pack.clear()
                pack.append("TOWER B")
                pack.append("WIRE")
        else:
            readfast(fail)
            hand.clear()
            pack.clear()
            pack.append("TOWER B")
            pack.append("WIRE")
    readtut("[[TUTORIAL]]: You can COMBINE one item in your HAND with another item in your HAND, your PACK or on the ground.\n              When you COMBINE items, the new item will be in your HAND.\n              Some objects will change when you combine them, so pay attention to the results!\n")
    radio("⌂H: One last thing before you head in - give me a ping.\n")
    radio("☼S: Buy me a drink first, ⌂Homebase.\n")
    radio("⌂H: From your BATS unit,  ☼Sunshine. From what we can tell there's no light in there - even artifical light doesn't\n    travel, so you'll need to rely on the Bounced Acoustic Telemetry System to get you around.\n")
    radio("☼S: Nice backronym. You couldn't just call it sonar?\n")
    radio("⌂H: Anyone ever tell you you're no fun?\n")
    radio("☼S: Why do you think they call me ☼Sunshine?\n")
    radio("⌂H: Good point.\n\n")
    shift = False
    readtut("[[TUTORIAL]]: Type PING to get a description of your surroundings.\n              You can type BACK at any time to exit your current menu.\n")
    while shift is False:
        command()
        shift = True
    radio("☼S: Kind of verbose for an AI processor.\n")
    radio("⌂H: Thanks, I coded it myself.\n")
    radio("☼S: Never would have guessed.\n")
    shift = False
    while shift is False:
        radio("☼S: Am I clear to start mission?\n")
        radio("⌂H: Standby...\n")
        radio("⌂H: ")
        radioslow("...\n")
        if len(pack) == 0 and len(hand) == 1 and hand[0] in ["WIRED TOWER"]:
            radio("⌂H: Affirmative, mission is go. You are cleared for takeoff, ☼Sunshine.\n")
            shift = True
        elif len(hand) == 0 and len(pack) == 1 and pack[0] in ["WIRED TOWER"]:
            radio("⌂H: Affirmative, mission is go. You are cleared for takeoff, ☼Sunshine.\n")
            shift = True
        else:
            radio("⌂H: Something's not right... make sure TOWER A is placed and you have the WIRED TOWER ready to go.\n")
            command()
    radio("☼S: Roger. Approaching DARK ZONE.\n")
    radio("⌂H: Breaching DARK ZONE border in three...\n")
    clear()
    radio("two.")
    radioslow("..")
    clear()
    radio("one.")
    radioslow("..")

def title():
    clear()
    time.sleep(1)
    printfade("<<<<<<<DARC HOUSE>>>>>>>")
    printfade("----by RovingFortune----")
    clear()

def front0():
    global locno
    locno = 1
    readfade("....")
    erase()
    time.sleep(1)
    scramfade("...shine, come in....")
    time.sleep(2)
    scramfade("..Sun..ine, are you..vi.. me?...")
    time.sleep(2)
    scramred("                  Sun                ")
    time.sleep(2)
    scramred("                 Come In                 ")
    erase()
    radioscram("⌂H: Come in, ☼Sunshine, do you read?! Are you ok in there?!")
    radioslow("\n☼S: .....")
    radio("...ow.\n")
    radio("⌂H: Holy fucknuts, what happened?\n")
    radio("☼S: Pretty sure holy fucknuts isn't in the radio protocol, ⌂Homebase.\n")
    radiostrong("⌂H: Report, ☼Sunshine! What is your status?!\n")
    radio("☼S: Take it easy, ⌂Homebase, I just fell on my ass when I came through the barrier!\n    The whole world just turned over and tried to leave me behind.\n")
    radio("⌂H: Huh... some kind of gravity shift. Would explain why the exploratories all came back with inverted y-axes.\n")
    radio("☼S: I'm fine, by the way, thanks for asking.\n")
    time.sleep(0.05)
    radio("⌂H: I did ask.\n")
    time.sleep(1)
    radio("☼S: ")
    radioslow("Oh,")
    radio(" right.")
    time.sleep(0.5)
    radio(" Sorry.\n")
    radio("⌂H: All good. Now, dust yourself off and PLACE the other TOWER so we can get you moving.\n")
    radio("☼S: PLACE it where? I can't see a damn thing.\n")
    radio("⌂H: Anywhere - once the TOWER is placed, BATS will be your eyes - that dent your ass made\n    should be a good start.\n")
    radio("☼S: Nice. Just the kind of professionalism we want from an operative.\n")
    radio("⌂H: I learned from the best, ☼Sunshine.\n")

    def tower():
        cursor.show()
        a=input("COMMAND:")
        cursor.hide()
        a=a.upper()
        if a in ["PLACE"]:
            place()
        else:
            radiofast("⌂H: Gotta put the TOWER down first, ☼Sunshine. Otherwise you won't have eyes or ears in there.\n")
            tower()
    tower()
    radio("⌂H: Ok, second TOWER is transmitting and...\n")
    radio("☼S: ")
    radioslow("...")
    radio("and?\n")
    radio("⌂H: And it looks like you've got your work cut out for you.\n")
    radio("☼S: Meaning?\n")
    radio("⌂H: Meaning you should get moving, ☼Sunshine. It's going to be a long night.\n")




#---------------START-------------------
clear()
cursor.show()
a=input("DARC HOUSE:")
a=a.upper()
cursor.hide()
clear()
if a == "SKIP":
    speed = 0.001
    tutorial() 
    title()
elif a == "TITLE":
    hand.append("WIRED TOWER")
    title()
else:
    prologue()
    tutorial()
    title()
speed = 0.05
front0()
print("[END OF DEMO]")