# This Python file uses the following encoding: utf-8
import os, sys

from constant import tops_midi

def somByDay(sDate, iTirage):
    for item in iTirage:
        number = tops_midi.get("{}".format(item))
        tops_midi["{}".format(item)] =  number + 1