import random
from random import randint as Xn
import sys 
import os
import cursor
import string
import asyncio
import monsters
import darcstyles as d




#------------------UNIVERSALS----


# Alabaster - painter
# Blanche - matriarch
# Alvaro - patriarch
# Candice - siren
# Wynn - thug

sirenXd = 10
sirenenc = 0
def siren0():
    global sirenXd
    global sirenenc
    sirenroll = Xn(1,sirenXd)
    if sirenroll == 5:
        d.readfade("♪")
        sirenXd -= 1
        sirenenc += 1

def siren1():
    global sirenXd
    global sirenenc
    sirenroll = Xn(1,sirenXd)
    if sirenroll == 5:
        d.readfade("♫")
        d.radio("⌂H: Did you hear that?")
        sirenXd -= 1
        sirenenc += 1
