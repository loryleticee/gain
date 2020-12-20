# This Python file uses the following encoding: utf-8
import os, sys
import csv
from datetime import datetime, timedelta, date
from constant import tops_soir_month, tops_midi_month, tops_soir, tops_midi

def somByDay(sDate, sDay_phase, iTirage):
    for item in iTirage:
        if(sDay_phase == 'midi'):
            number = tops_midi.get("{}".format(item))
            tops_midi["{}".format(item)] =  number + 1

        if(sDay_phase == 'soir'):
            number = tops_soir.get("{}".format(item))
            tops_soir["{}".format(item)] =  number + 1
            
def somByMonth(sDate, sDay_phase, iTirage):
    global tops_midi_month
    global tops_soir_month

    for item in iTirage:
        if(sDay_phase == 'midi'):
            number = tops_midi_month.get("{}".format(item))
            tops_midi_month["{}".format(item)] =  number + 1
        if(sDay_phase == 'soir'):
            number = tops_soir_month.get("{}".format(item))
            tops_soir_month["{}".format(item)] =  number + 1

        
