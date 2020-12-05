# This Python file uses the following encoding: utf-8
import os, sys, glob
#import pandas as pds
from datetime import datetime
from moon import moon_phase
from match import somByDay

#date_n= pds.to_datetime('2020/06/24')
#print('A: {}'.format(date_n))

aDiff = aDiff2 = lst = current_tirage = []

day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
month_name = ['null_month','January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def askInit():
    global user_input
    if (len(sys.argv) < 2):
        print('\n Tapez control(^)+c pour annuler.\n')
        user_input = input("Enter le nombre de tirage pris en compte pour les statistiques des Tops numbers: \n")
    else:
        user_input = int(sys.argv[1])*21

"""manage bisextile year """

def topNumbers(sDate, sTirage):
    global month_name
    global current_tirage
    global aDiff
    global aDiff2

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
                        print("{}--{} {} ☀️ {}%    Today is : {} {} {} ☀️ {}% ".format(status, day_word, date,  light, sToday_status, sToday_day_word, sToday_date, sToday_light ))
                        print("\x1b[6;30;42m' +Top 🔥🔥🔥 {} + '\x1b[0m' \n".format(sTirage))
                        somByDay(sDate, sTirage)
                    else:
                        somByDay(sDate, sTirage)
                        print("{}--{} {} ☀️ {}%   Today is : {} {} {} ☀️ {}% ".format(status, day_word, date,  light,  sToday_status, sToday_day_word, sToday_date, sToday_light ))
                        print("\x1b[6;30;42m' +Top 1 {} + '\x1b[0m' \n".format(sTirage))
                        
                else:
                    #somByDay(sDate, sTirage)
                    print("{}--{} {} ☀️ {}%   Today is : {} {} {} ☀️ {}% ".format(status, day_word, date,  light,  sToday_status, sToday_day_word, sToday_date, sToday_light))
                    print('Top 2 {}  \n'.format(sTirage))

def getDayNumber(sDate):
    return int(datetime.strptime(sDate, '%d/%m/%Y').weekday())

#----------------------------------------------------------------------------

def getDayWord(iDay):
    global day_name
    return str(day_name[iDay])

#----------------------------------------------------------------------------