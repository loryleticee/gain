# This Python file uses the following encoding: utf-8
import os, sys, glob
from datetime import datetime
from moon import moon_phase
from match import somByDay

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

def topNumbers(sDate, sDay_phase, sTirage):
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
                        print("{}--{} {} ☀️ {}% ({})   Today is : {} {} {} ☀️ {}% ".format(status, day_word, date,  light, sDay_phase, sToday_status, sToday_day_word, sToday_date, sToday_light ))
                        print("\x1b[6;30;42m' +Top 🔥🔥🔥 {} + '\x1b[0m' \n".format(sTirage))
                        somByDay(sDate, sDay_phase, sTirage)
                    else:
                        somByDay(sDate, sDay_phase, sTirage)
                        print("{}--{} {} ☀️ {}% ({})  Today is : {} {} {} ☀️ {}% ".format(status, day_word, date,  light, sDay_phase,  sToday_status, sToday_day_word, sToday_date, sToday_light ))
                        print("\x1b[6;30;42m' +Top 1 {} + '\x1b[0m' \n".format(sTirage))
                        
                else:
                    #somByDay(sDate, sDay_phase, sTirage)
                    print("{}--{} {} ☀️ {}% ({})   Today is : {} {} {} ☀️ {}% ".format(status, day_word, date,  light, sDay_phase,  sToday_status, sToday_day_word, sToday_date, sToday_light))
                    print('Top 2 {}  \n'.format(sTirage))

def getDayNumber(sDate):
    return int(datetime.strptime(sDate, '%d/%m/%Y').weekday())

#----------------------------------------------------------------------------

def getDayWord(iDay):
    global day_name
    return str(day_name[iDay])

#----------------------------------------------------------------------------

def currentResult(sTirage):
        global current_tirage
        if(current_tirage is not []):
            aDiff, aDiff2   = reverseCompare(sTirage, current_tirage[2])
            print("\x1b[0;1;32m' Tirage d'aujourdhui : {} No Similar numbers {} {} for {} tirage + '\x1b[0m' \n".format(current_tirage[0], aDiff, aDiff2, current_tirage[1]))


#produit cartésien 
#cross join (Msql)
#donne les toutes combinaisons possible entre un nombre delement donnée 