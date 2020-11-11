# This Python file uses the following encoding: utf-8
import os, sys
import csv
from datetime import datetime, timedelta, date
from constant import tops_midi

isN1 = isN2 = isN3 = isN4 = isN5 = isN6 = False

def somByDay(iTirage, n1, n2, n3 , n4, n5):
    global isN1
    global isN2
    global isN3
    global isN4
    global isN5

    for item in iTirage:
        number = tops_midi.get("{}".format(item))
        tops_midi["{}".format(item)] =  number + 1

        if(str(item) == str(n1)):
            isN1 = True

        if(str(item) == str(n2)):
            isN2 = True

        if(str(item) == str(n3)):
            isN3 = True

        if(str(item) == str(n4)):
            isN4 = True

        if(str(item) == str(n5)):
            isN5 = True

    if(isN1 == True & isN2 == True & isN3 == True & isN4 == True & isN5 == True):
        print(iTirage)
        isN1 = isN2 = isN3 = isN4 = isN5 = False
    else:
        isN1 = isN2 = isN3 = isN4 = isN5 = False
            