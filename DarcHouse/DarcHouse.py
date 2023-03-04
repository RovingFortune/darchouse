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
import rooms
import asyncio
import monsters
from Darcstyles24 import radio
from Darcstyles24 import radiofast
from Darcstyles24 import radiohush
from Darcstyles24 import radioscram
from Darcstyles24 import radiostrong
from Darcstyles24 import radioslow
from Darcstyles24 import read
from Darcstyles24 import readbats
from Darcstyles24 import readfade
from Darcstyles24 import readfast
from Darcstyles24 import readslow
from Darcstyles24 import readtut
from Darcstyles24 import scram
from Darcstyles24 import scramfade
from Darcstyles24 import scramred
from Darcstyles24 import clear
from Darcstyles24 import erase
from Darcstyles24 import printfade
from Darcstyles24 import batsdata
#------------------UNIVERSALS------------------
colorama.init(autoreset=True)
cursor.hide()
run = True
shift = False
tutor = True
safe = False
speed = 0.03
locno = 0
pingno = 0
CURSOR_UP_ONE = '\x1b[1A' 
ERASE_LINE = '\x1b[2K'

#-------------------INVENTORIES------------------
pack = []
hand = []
mixer = []

canmix = ["TOWER B", "WIRE"]
blends = ["WIRE+TOWER B", "TOWER B+WIRE"]

#-------------------TEXT STYLES------------------
fail = "⌂H: Negative copy, ☼Sunshine - try something else.\n"

#-------------------MONSTERS------------------




#-------------------COMMANDS--------------------
def take(c):
    hand.append(c)
    pack.remove(c)
    readbats("[BATS]: " + f"{c}" + " is in your hand.\n")
    command()
    
def stash(c):
    pack.append(c)
    hand.remove(c)
    readbats("[BATS]:" + f"{c}" + " placed in pack.\n")
    command()

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
            command()
        else: 
            radiofast("⌂H: Sorry, ☼Sunshine, fresh out of that.")
            openpack()
    inpack()

def pickup(c):
    hand.append(c)
    rooms.Xr[locno].junk.remove(c)
    readbats("[BATS]: " + f"{c}" + " is in your hand.\n")
    command()
    
def putdown(c):
    rooms.Xr[locno].junk.append(c)
    hand.remove(c)
    readbats("[BATS]: " + f"{c}" + " dropped.\n")
    command()


def goto(c):
    global locno
    go = rooms.Xr[locno].exits.index(c)
    locno = rooms.Xr[locno].exitno[go]
    readbats("\n[BATS]: Now entering " + f"{c}" +"\n")
    command()
    

def ping():
    global pingno
    readbats("\n[BATS READOUT: PING " + f"{pingno:03}" + "]\n")
    pingno += 1
    batsdata("Location: " + f"{rooms.Xr[locno].name}")
    print(" " + f"{rooms.Xr[locno].desc}")
    if len(rooms.Xr[locno].junk) == 1:
        print(str(" There is a " + f"{rooms.Xr[locno].junk[0]}" + " on the ground."))
    elif len(rooms.Xr[locno].junk) == 0:
        pass
    else:
        print("Objects in the vicinity:")
        for item in rooms.Xr[locno].junk:
            print("• " + f"{item}")
    print("\nExits:")
    for exit in rooms.Xr[locno].exits:
        print("• " + f"{exit}")
    print(" ")
    def insurvey():
        cursor.show()
        c = input("PING:")
        c = c.upper()
        cursor.hide()
        if c in rooms.Xr[locno].junk:
            if len(hand) < 5:
                pickup(c)
            else:
                if len(pack) < 5:
                    readbats("[BATS]: Your hands are full, but you can fit that in your pack.\n")
                    pack.append(c)
                    rooms.Xr[locno].junk.remove(c)
                else:
                    radiofast("⌂H: Slow down there, you're way too overloaded to do anything with that.\n")
                    insurvey()
        elif c in rooms.Xr[locno].exits:
            goto(c)
        elif c in hand:
            putdown(c)
        elif c in ["BACK"]:
            command()
        else: 
            radiofast(fail)
            insurvey()
    insurvey()

def place():
    j = rooms.Xr[locno].junk
    if len(hand) == 1:
        j.append(hand[0])
        readbats("[BATS]: " + f"{hand[0]}" + " placed.\n")
        hand.clear()
    elif len(hand) == 0:
        readbats("[BATS]: You're not holding anything.\n")
    else:
        def placeselect():
            readfast("⌂H: What do you want to place?\n")
            for item in hand:
                print("• " + f"{item}")
            cursor.show()
            i = input("ITEM:")
            i = i.upper()
            cursor.hide()
            if i in hand:
                j.append(i)
                hand.remove(i)
                readbats("[BATS]: " + f"{i}" + " placed.\n")
            elif i in ["BACK"]:
                command()
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
    readbats("[BATS]: What are you combining with your " + f"{mixer[0]}" + "?\n")
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
            elif m in rooms.Xr[locno].junk:
                rooms.Xr[locno].junk.remove(m)
            elif m in ["BACK"]:
                hand.append(mixer[0])
                mixer.clear()
                command()
            y = blend(x)
            hand.append(y)
            readbats("[BATS]: " + f"{y}" + " is now in your hand.\n")
        else:
            radiofast("⌂H: Not a winning combination, those two - try something else.\n")
            mix()
    else:
        radiofast("⌂H: Good start, but you can't combine your " + f"{mixer[0]}" + " with that.\n")
        mix()
    mixer.clear()

def combine():
    if len(hand) == 1:
        if hand[0] in canmix:
            mixer.append(hand[0])
            hand.clear()
            mix()
        else:
            radiofast("⌂H: No can do - can't combine that " + f"{hand[0]}" + " with anything.\n")
            command()
    elif len(hand) == 0:
        readbats("[BATS]: You're not holding anything.\n")
        command()
    else:
        def combineselect():
            readbats("[BATS]: What do you want to combine?\n")
            for item in hand:
                print("• " + f"{item}")
            cursor.show()
            i = input("COMBINE:")
            i = i.upper()
            cursor.hide()
            if i in canmix:
                if i in hand:
                    mixer.append(i)
                    mix()
                elif i in ["BACK"]:
                    command()
                else:
                    readbats("[BATS]: You're not holding that.\n")
                    combineselect()
            else:
                radiofast("⌂H: No can do - can't combine that with anything.\n")
                combineselect()
        combineselect()

def openhand():
    for item in hand:
        readbats("[HAND]:\n")
        print("• " + str(item))
        command()

def chatter():
    greet = ["What's the story, ☼Sunshine?", "Go ahead.", "Talk to me.", "What's crackin'?", "How do you do?", "How can I be of assistance?", "We've got to stop meeting like this. The neighbours will talk.", "So good of you to drop by!", "Did you miss me?", "Out with it.", "Gimme words.", "Speak now, or forever hold your peace.", "Anything you say can and will be used against you.", "Keep it short, I charge by the word." "Tell me what you're wearing.", "Tell me something good.", "A/S/L?", "Talk fast, or I'll burn my croissants", "Who the hell gave you this number?! Just kidding. What's up?", "Terms and conditions apply, results may vary.", "Your call is being recorded for quality assurance purposes.", "Kei te pēhea koe?", "Speak, peasant.", "Keep it clean, you're on speaker."]
    if pingno/2 <= len(greet)-1:
        chatXd = int(pingno/2)
    else:
        chatXd = len(greet)-1
    radiofast("☼S: ☼Sunshine to ⌂Homebase.\n")
    radiofast("⌂H: ⌂Homebase receiving. ")
    radiofast(f"{greet[Xn(0,chatXd)]}" + "\n")
    def subjects():
        chatsub = []
        chatsub.append(f"{rooms.Xr[locno].name}")
        if monsters.sirenenc == 1:
            chatsub.append["WEIRD SOUND"]
        if monsters.sirenenc == 2:
            chatsub.append["INTERFERENCE"]
        if monsters.sirenenc == 3:
            chatsub.append["MUSIC"]
        for subject in chatsub:
            print("• " + str(subject))
        c = input("CHATTER:")
        c = c.upper()
        if c in chatsub:
            if c == chatsub[0]:
                rooms.Xr[locno].chatter()
            if c in ["WEIRD SOUND"]:
                radio("☼S: Did you pick strange anything up just now?\n")
                radio("⌂H: ")
                radioslow("...")
                radio("no? I mean I can hear you. You're pretty strange.\n")
                radio("☼S: No, I mean before wh... never mind. I must be hearing things.\n")
                radio("⌂H: Mkay. You doing alright in there, ☼Sunshine?\n")
                radio("☼S: Yeah, yeah, I'm fine. Just losing my mind a little.\n")
                radio("⌂H: Copy. Let me know if you start finding it.")
            elif c in ["INTERFERENCE"]:
                radio("☼S: So am I crazy, or did you hear it?\n")
                radio("⌂H: Affirmative - trying to figure out where it's coming from.\n")
                radio("☼S: I'll tell you where it's coming from. It's in the damn house.\n")
                radio("⌂H: Gotta be sure first, could still be an artifact.\n")
                radio("☼S: If you say so, ⌂Homebase.\n")
                radio("⌂H: I sure do, ☼Sunshine.")
            elif c in ["MUSIC"]:
                radio("☼S: Someone is singing in here.\n")
                radio("⌂H: That's sure what it sounds like.\n")
                radio("☼S: You seem awfully cavalier about there being another person in here with me.\n")
                radio("⌂H: Would it help you to hear that I've been pulling my hair out since it came through?\n")
                radio("☼S: Not exactly.\n")
                radio("⌂H: Right.")
                radio("☼S: ")
                radioslow("...")
                radio("so?")
                radio("⌂H: So what?")
                radio("☼S: So what do you think?")
                radio("⌂H: I think it sounds like someone's singing in there.")
                radio("☼S: I love our little talks.")
                radio("⌂H: The feeling is mutual.")
            radio(" Anything else?\n")
            subjects()
        elif c in ["BACK"]:
            signoff = ["over and out.", "don't be a stranger.", "good luck in there.", "lots of love.", "kisses!", "signing off.", "don't keep me waiting too long.", "report soon!", "speak soon!", "mwah ♥", "don't burn the house down.", "see you next Tuesday!", "see you later!", "get back to work!", "gotta go, my croissants are burning!", "knock 'em dead.", "don't poke the ghosts.", "kthxbai.", "chur.", "ka kite anō!"]
            radio("☼S: Nothing further, ⌂Homebase. Over.")
            radio("⌂H: Roger, ☼Sunshine - ")
            radiofast(f"{signoff[Xn(0,chatXd)]}" + "\n")
            command()
        else:
            radiofast("⌂H: Uh, that's a negative copy, ☼Sunshine, no idea what you're talking about. Go again?\n")
            subjects()
    subjects()

    

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
    elif a in ["CHATTER"]:
        chatter()
    elif a in ["HELP"]:
        readbats("[BATS] COMMAND LIST:")
        print("HAND: See what you are holding.")
        print("PACK: Open your inventory.")
        print("PING: Scan the area for details, including exits and objects in the area.")
        print("PLACE: Put an object from your HAND down.")
        print("COMBINE: Add an object in your HAND to another object in your HAND, your PACK or in the vicinity.")
        print("CHATTER: Call in to ⌂Homebase.")
        command()
    elif a in rooms.Xr[locno].exits:
        goto(a)
    elif a in ["BACK"]:
        command()
    else:
        radiofast(fail)
        command()



#---------------------STORY-------------------

def prologue():
    clear()
    time.sleep(2)
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
    readtut("[[TUTORIAL]]: Type PERIMETER to advance - commands are not case sensitive.\n")
    def tperi():
        cursor.show()
        c = input("COMMAND:")
        cursor.hide()
        if c.upper() in ["PERIMETER"]:
            pass
        elif c.upper() in ["RUN"]:
            run()      
        else:
            radiofast(fail)
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
            pack.clear()
            hand.clear()
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
                radiofast(fail)
                tpack()
        tpack()
        readtut("[[TUTORIAL]]: Type TOWER A to take it out of your PACK and put it in your HAND.\n")
        openpack()
        if len(hand) == 1 and hand[0] == "TOWER A":
            shift = True
        else:
            radiofast("⌂H: Wrong item, ☼Sunshine - give it another go")
    shift = False
    readtut("[[TUTORIAL]]: You can hold up to 5 items in your PACK.\n              You can also hold up to 5 items in your HAND but holding too many items \n              may make some things more difficult, or stop you from doing other things entirely.\n")
    readtut("              Now type PLACE to put the object in your HAND on the ground.\n")
    while shift is False:
        def tplace():
            cursor.show()
            c = input("COMMAND:")
            cursor.hide()
            if c.upper() in ["PLACE"]:
                pass
            elif c.upper() in ["RUN"]:
                run()      
            else:
                rooms.Xr[locno].junk.clear()
                hand.clear()
                hand.append("TOWER A")
                radiofast(fail)
                tplace()
        tplace()
        place()
        if len(rooms.Xr[locno].junk) == 1 and rooms.Xr[locno].junk[0] == "TOWER A":
            shift = True
    readtut("[[TUTORIAL]]: " + f"{rooms.Xr[locno].junk[0]}" + " is now on the ground. You can PLACE as many items\n              from your HAND on the ground as you want, but too much junk lying around could get in your way.\n" )
    time.sleep(1)
    radio("⌂H: First Tower is transmitting, ☼Sunshine - attach the WIRE to the second TOWER and take it through.\n")
    shift = False
    while shift is False:
        readtut("[[TUTORIAL]]: Type PACK to open your inventory and take out TOWER B. \n")
        def tpack2():
            pack.clear()
            hand.clear()
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
                radiofast(fail)
                tpack2()
        tpack2()
        openpack()
        if len(hand) == 1 and hand[0] == "TOWER B":
            readtut("[[TUTORIAL]]: Now type COMBINE to add the WIRE to TOWER B. \n")
            def tcombine():
                pack.clear()
                pack.append("WIRE")
                cursor.show()
                c = input("COMMAND:")
                cursor.hide()
                if c.upper() in ["COMBINE"]:
                    pass
                elif c.upper() in ["RUN"]:
                    run()      
                else:
                    radiofast(fail)
                    tcombine()
            tcombine()
            combine()
            if len(hand) == 1 and hand[0] == "WIRED TOWER":
                shift = True
            else:
                radiofast(fail)
                hand.clear()
                pack.clear()
                pack.append("TOWER B")
                pack.append("WIRE")
        else:
            radiofast(fail)
            hand.clear()
            pack.clear()
            pack.append("TOWER B")
            pack.append("WIRE")
    readtut("[[TUTORIAL]]: You can COMBINE one item in your HAND with another item in your HAND, your PACK or on the ground.\n              When you COMBINE items, the new item will be in your HAND.\n              Some objects will change when you combine them, so pay attention to the results!\n")
    radio("⌂H: One last thing before you head in - give me a ping.\n")
    radio("☼S: Buy me a drink first, ⌂Homebase.\n")
    radio("⌂H: From your BATS unit, ☼Sunshine. From what we can tell there's no light in there - even artifical light doesn't\n    travel, so you'll need to rely on the Bounced Acoustic Telemetry System to get you around.\n")
    radio("☼S: Nice acronym. You couldn't just call it sonar?\n")
    radio("⌂H: Anyone ever tell you you're no fun?\n")
    radio("☼S: Why do you think they call me ☼Sunshine?\n")
    radio("⌂H: Good point.\n\n")
    shift = False
    while shift is False:
        readtut("[[TUTORIAL]]: Type PING to get a description of your surroundings.\n")
        def tping():
            cursor.show()
            c = input("COMMAND:")
            cursor.hide()
            if c.upper() in ["PING"]:
                global pingno
                readbats("\n[BATS READOUT: PING " + f"{pingno:03}" + "]\n")
                pingno += 1
                print("Location: " + f"{rooms.Xr[locno].name}")
                print(" " + f"{rooms.Xr[locno].desc}")
                print(str(" There is a " + f"{rooms.Xr[locno].junk[0]}" + " on the ground."))
                print("\nExits:")
                for exit in rooms.Xr[locno].exits:
                    print("• " + f"{exit}")
                print(" ")
            elif c.upper() in ["RUN"]:
                run()      
            else:
                radiofast(fail)
                tping()
        def tback():
            readtut("[[TUTORIAL]]: Type BACK at any time to exit your current menu.")
            cursor.show()
            c = input("PING:")
            cursor.hide()
            if c.upper() in ["BACK"]:
                pass
            elif c.upper() in ["RUN"]:
                run()      
            else:
                radiofast(fail)
                tback()
        tping()
        tback()
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
            rooms.perimeter.junk.clear()
            readtut("[[TUTORIAL]]: Type PACK to open your inventory.\n")
            tpack()
            openpack()
            tpack()
            tplace()
            place()
            tcombine()
            combine()
            radio("☼S: Ok, let's try this again.")
    shift = False
    while shift is False:
        readtut("[[TUTORIAL]]: Type the name of an EXIT to your current location to go to there. ")
        def texit():
                global shift
                cursor.show()
                c = input("COMMAND:")
                cursor.hide()
                if c.upper() in ["DARK ZONE"]:
                    shift = True
                elif c.upper() in ["RUN"]:
                    run()      
                else:
                    radiofast(fail)
                    texit()
        texit()
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
    scramfade("..Sun..ine, are you...ceivi..me?...")
    time.sleep(2)
    scramred("                Sun                   ",1)
    time.sleep(2)
    scramred("              Come In                 ",1)
    erase()
    radioscram("⌂H: Come in, ☼Sunshine, do you read?! Are you ok in there?!")
    radio("\n☼S: ")
    radioslow(".....")
    radio("...ow.\n")
    radio("⌂H: Holy fucknuts, what happened?\n")
    radio("☼S: ")
    radioslow("Ngh, ")
    radio("Pretty sure holy fucknuts isn't in the radio protocol, ⌂Homebase.\n")
    radiostrong("⌂H: Report, ☼Sunshine! What is your status?!\n")
    time.sleep(1)
    radio("☼S: Take it easy, ⌂Homebase, I just fell on my ass when I came through the barrier!\n    The whole world just turned over and tried to leave me behind.\n")
    radio("⌂H: Huh... some kind of gravity shift. Would explain why the exploratories all came back with inverted y-axes.\n")
    radio("☼S: I'm fine, by the way, thanks for asking.\n")
    time.sleep(0.05)
    radio("⌂H: I did ask.\n")
    time.sleep(1)
    radio("☼S: ")
    radio("Oh,")
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
    rooms.front.junk.clear()




#---------------START-------------------

clear()
speed = 0.05
cursor.show()
def splash():
    global speed
    a=input("DARC HOUSE:")
    a=a.upper()
    cursor.hide()
    if a == "SKIP":
        speed = 0.00001
        tutorial() 
        title()
    elif a == "TITLE":
        hand.append("WIRED TOWER")
        title()
    elif a == "FRONT":
        hand.append("WIRED TOWER")
        speed = 0.005
        title()
        front0()
    elif a == "START":
        prologue()
        tutorial()
        title()
    elif a == "YARD":
        pass
    else:
        radiofast(fail)
        clear()
        splash()
    
splash()
clear()
locno = 1
command()


#print("[END OF DEMO]")