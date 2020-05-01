# This Python file uses the following encoding: utf-8
import os, sys, glob
from datetime import datetime
from moon import moon_phase

dicto = {}
lst = []
tops = {}
current_date = ''

day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
month_name = ['null_month','January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

#----------------------------------------------------------------------------

def ffff(sDate, sDay_phase, sTirage):
    global tops
    for number in aFinal:
        if (tops.get("{}".format(number)) is None):
            numa = 0
        else:
            numa = tops.get("{}".format(number))

        tops["{}".format(number)] =  1 + numa
#----------------------------------------------------------------------------

def reverseCompare(array_1, array_2):
    aDiif = list(set(array_1) - set(array_2))
    aDiif2 = list(set(array_2) - set(array_1))
    return aDiif, aDiif2
#----------------------------------------------------------------------------

def getDayNumber(sDate):
    return int(datetime.strptime(sDate, '%d/%m/%Y').weekday())

#----------------------------------------------------------------------------

def getDayWord(iDay):
    global day_name
    return str(day_name[iDay])

#----------------------------------------------------------------------------

def daySort(day_name, day, dayRef, aFinal, aRefValue):
    if(day_name[day] == day_name[dayRef]):
        #dicto[day_name[day]] = []
        global lst
        lst.append(aFinal)
        lst.append(aRefValue)
        dicto.update( {day_name[day]: [lst]} )
        dicto.update( {day_name[dayRef]: [lst]} )

#----------------------------------------------------------------------------

"""manage bisextile year """

def topNumbers(sDate, sDay_phase, sTirage):
    global month_name
    global current_date
    
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

    if(current_date != sDate):
        if(str(day_word) == str(sToday_day_word)):
            if(month_word == sToday_month_word):
                if(status == sToday_status):
                    if(light == sToday_light):
                        if(jour == sToday_jour):
                            print("{}--{} {} ☀️ {}%    Today is : {} {} {} ☀️ {}% ".format(status, day_word, date,  light, sToday_status, sToday_day_word, sToday_date, sToday_light ))
                            print("\x1b[6;30;42m' +Top 🔥🔥🔥 {} + '\x1b[0m' \n".format(sTirage))
                        else:
                            print("{}--{} {} ☀️ {}%    Today is : {} {} {} ☀️ {}% ".format(status, day_word, date,  light, sToday_status, sToday_day_word, sToday_date, sToday_light ))
                            print("\x1b[6;30;42m' +Top 1 {} + '\x1b[0m' \n".format(sTirage))
                    else:
                        print("{}--{} {} ☀️ {}%    Today is : {} {} {} ☀️ {}% ".format(status, day_word, date,  light, sToday_status, sToday_day_word, sToday_date, sToday_light))
                        print('Top 2 {}  \n'.format(sTirage))
                #else:
                    #print("{}--{} {} ☀️ {}%    Today is : {} {} {} ☀️ {}% ".format(status, day_word, date,  light, sToday_status, sToday_day_word, sToday_date, sToday_light))
                    #print('Top 3 {}  \n'.format(sTirage))
            #else:
                #print("{}--{} {} ☀️ {}%    Today is : {} {} {} ☀️ {}% ".format(status, day_word, date,  light, sToday_status, sToday_day_word, sToday_date, sToday_light))
                #print('Top 4 {}  \n'.format(sTirage)) 
    current_date = sDate

def delOldFiles():
    #Supprime tous les anciens fichiers de log
    files_to_delete = glob.glob("./logloto/*.txt")
    for filePath in files_to_delete:
        try:
            os.remove(filePath)
        except:
            print("Error while deleting file : ", filePath)
    #FinSupprime