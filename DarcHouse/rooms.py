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

key1 = False
key2 = False
Key3 = False

class Room:
    def __init__(self, location, new, name, safe, exits, exitno, junk, desc):
        self.location = location
        self.new = new
        self.name = name
        self.safe = safe
        self.exits = exits
        self.exitno = exitno
        self.junk = junk
        self.desc = desc
        
        


perimeter =    Room(0, True, "PERIMETER", True, ["DARK ZONE"], [1], [], " A clearing in a forest, set back from the dirt road that brought you here. An area that may have been a garden once,\n now terribly overgrown sprawls out on either side. \n Before you, the spherical border of the DARK ZONE curves away from you into the night.\n")
front =        Room(1, False, "SOUTH YARD", False, ["VERANDA"], [2], [], " The southern end of the property. In front of you is a gigantic, gothic manor. ")
veranda =      Room(2, True, "VERANDA", False, ["FOYER", "SOUTH YARD"], [3,1], [], "veradesc")
foyer =        Room(3, True, "FOYER", False, ["VERANDA", "PARLOUR", "CONSERVATORY", "LIBRARY"], [2,4,9,11], [], "foyerdesc")
parlour =      Room(4, True, "PARLOUR", False, ["FOYER", "DINING ROOM"], [1,5], [],  "parlourdesc")
dining =       Room(5, True, "DINING ROOM", False, ["PARLOUR", "KITCHEN"], [4,15], [],  "diningdesc")
egarden =      Room(6, True, "EAST GARDEN", False, ["KITCHEN", "SHED", "GREENHOUSE", "SOUTH YARD", "NORTH GROUNDS"], [15,7,8,1,19], [],  "eastdesc")
shed =         Room(7, True, "SHED", False, ["EAST GARDEN"], [6], [], "sheddesc")
greenhouse =   Room(8, True, "GREENHOUSE", False, ["EAST GARDEN"], [6], [], "greendesc")
conservatory = Room(9, True, "CONSERVATORY", False, ["FOYER", "DEN"], [1,10], [], "conservdesc")
den =          Room(10, True, "DEN", False, ["CONSERVATORY", "LIBRARY"], [9,11], [], "dendesc")
library =      Room(11, True, "LIBRARY", False, ["DEN", "FOYER", "ANNEX"], [10,1,14], [], "librarydesc")
vestibule =    Room(12, True, "VESTIBULE", False, ["ANNEX"], [14], [], "vestdesc")
laundry =      Room(13, True, "LAUNDRY", False, ["ANNEX"], [14], [], "laundrydesc")
annex =        Room(14, True, "ANNEX", False, ["LIBRARY", "STUDIO", "VESTIBULE", "PATIO", "NORTH GROUNDS", "LAUNDRY"], [11,17,12,26,19,13], [], "annexdesc")
kitchen =      Room(15, True, "KITCHEN", False, ["DINING ROOM", "PANTRY"], [5,16], [], "kitchendesc")
pantry =       Room(16, True, "PANTRY", False, ["KITCHEN"], [15], [], "pantrydesc")
studio =       Room(17, True, "STUDIO", False, ["ANNEX", "DARKROOM"], [14,18], [], "studiodesc")
darkroom =     Room(18, True, "DARKROOM", False, ["STUDIO"], [17], [],"darkdesc")
grounds =      Room(19, True, "NORTH GROUNDS", False, ["PATIO", "ANNEX", "MAZE", "EAST GARDEN", "WEST GARDEN"], [26,14,20,6,22], [], "groundsdesc")
maze =         Room(20, True, "MAZE", True, ["NORTH GROUNDS", "CENTRE OF THE MAZE"], [19,21], [], "mazedesc")
centre =       Room(21, True, "CENTRE OF THE MAZE", True, ["MAZE"], [21], [], "centredesc")
wgarden =      Room(22, True, "WEST GARDEN", True, ["POOL", "PAGODA", "TENNIS COURT", "NORTH GROUNDS", "SOUTH YARD"], [23,24,25,19,1], [], "westdesc")
pool =         Room(23, True, "POOL", False, ["WEST GARDEN"], [22], [], "pooldesc")
pagoda =       Room(24, True, "PAGODA", False, ["WEST GARDEN"], [22], [], "pagodadesc")
tennis =       Room(25, True, "TENNIS COURT", False, ["WEST GARDEN"], [22], [], "tennisdesc")
patio =        Room(26, True, "PATIO", False, ["ANNEX", "NORTH GROUNDS"], [14,19], [], "patiodesc")

Xr = [perimeter, front, veranda, foyer, parlour, dining, egarden, shed, greenhouse, conservatory, den, library, vestibule, laundry, annex, kitchen, pantry, studio, darkroom, grounds, maze, centre, wgarden, pool, pagoda, tennis, patio]


