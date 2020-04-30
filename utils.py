# This Python file uses the following encoding: utf-8
import os, sys, glob
from datetime import datetime
from moon import moon_phase

dicto = {}
lst = []
tops = {}

day_name= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']

#----------------------------------------------------------------------------

def topNumbers(aFinal):
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

def getMoon(nbr,sDate, aRefDate):
    date, status, light = moon_phase(int(sDate[0:2]), int(sDate[3:5]), int(sDate[6:10]))        
    date_ref, status_ref, light_ref = moon_phase(int(aRefDate[0:2]), int(aRefDate[3:5]), int(aRefDate[6:10]))
    print(sDate, aRefDate)
    file = open("./logkeno/{}-diff-{}.txt".format(nbr, datetime.today().strftime("%d-%m-%Y")),"a+")
    file.write(
        "{} {} ☀️ {}{} ({})                          {} {} ☀️ {}{} ({})"
        .format(
            status,
            date,
            light,
            '%',
            getDayWord(getDayNumber(sDate)),
            status_ref,
            date_ref,
            light_ref,
            '%',
            getDayWord(getDayNumber(aRefDate))
        )
    ) 
    file.close()

    # daySort() creation des tableau par jour
    """daySort(day_name, day, dayRef, aFinal, aRefValue)"""

#----------------------------------------------------------------------------

def showPourcent(obtain, outOf):
    marks = int(obtain)

    outof = int(outOf)

    per = marks*100/outof
    if(per == 25 or  per == 50 or per == 75 or per == 90):
        print ('\n{} %'.format(str(per)))

#----------------------------------------------------------------------------

def delOldFiles():
    #Supprime tous les anciens fichiers de log
    files_to_delete = glob.glob("./logloto/*.txt")
    for filePath in files_to_delete:
        try:
            os.remove(filePath)
        except:
            print("Error while deleting file : ", filePath)
    #FinSupprime