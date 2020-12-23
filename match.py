# This Python file uses the following encoding: utf-8
from constant import tops_soir_month, tops_midi_month, tops_soir, tops_midi, month_name
import csv
from datetime import datetime, timedelta, date
from moon import moon_phase 
from utils import getDayWord, getDayNumber
import os, sys

def get_draw(row):
    sTirage = row[4:24]
    sDate = row[1]
    sDay_phase = row[2]
    iTirage = map(int, sTirage)
    format_tirage = list(iTirage)
    return sDate, sDay_phase, format_tirage

def topNumbers(sDate, sDay_phase, iTirage):
    #Stat pasted
    jour = int(sDate[0:2])
    mois = int(sDate[3:5])
    annee = int(sDate[6:10])
    date, status, light = moon_phase(jour, mois, annee)

    #Stat jour
    sToday = datetime.today().strftime("%d/%m/%Y")
    
    sToday_jour = int(sToday[0:2])
    sToday_mois = int(sToday[3:5])
    sToday_annee = int(sToday[6:10])
    sToday_date, sToday_status, sToday_light = moon_phase(sToday_jour, sToday_mois, sToday_annee)

    day_word = getDayWord(getDayNumber(sToday))
    sToday_day_word = getDayWord(getDayNumber(sDate))

    month_word = month_name[mois]
    sToday_month_word = month_name[sToday_mois]
    
    if(day_word == sToday_day_word):
        if(month_word == sToday_month_word):
            if(status == sToday_status):
                if(light == sToday_light):
                    if(jour == sToday_jour):
                        print("{}--{} {} ☀️ {}% ({})   Today is : {} {} {} ☀️ {}% ".format(status, day_word, date, light, sDay_phase, sToday_status, sToday_day_word, sToday_date, sToday_light ))
                        print("\x1b[5;10;42m 🧨 {} \x1b[0m \n".format(iTirage))
                        somByDay(sDate, sDay_phase, list(iTirage))
                    else:
                        print("{}--{} {} ☀️ {}% ({})  Today is : {} {} {} ☀️ {}% ".format(status, day_word, date, light, sDay_phase,  sToday_status, sToday_day_word, sToday_date, sToday_light ))
                        print("\x1b[6;30;42m Top 1 {} \x1b[0m \n".format(list(iTirage)))
                        somByDay(sDate, sDay_phase, list(iTirage))
                else:
                    #somByDay(sDate, sDay_phase, iTirage)
                    print("{}--{} {} ☀️ {}% ({})   Today is : {} {} {} ☀️ {}% ".format(status, day_word, date, light, sDay_phase,  sToday_status, sToday_day_word, sToday_date, sToday_light))
                    print('Top 2 {}  \n'.format(list(iTirage)))

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

        
