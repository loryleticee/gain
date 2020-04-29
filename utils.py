# This Python file uses the following encoding: utf-8
import os, sys, glob
from datetime import datetime
from moon import moon_phase

dicto = {}
lst = []

#----------------------------------------------------------------------------

def createOneDiff(nbr,sDate, aFinal, aRefDate, aRefValue):
    day_name= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']

    day = datetime.strptime(sDate, '%d/%m/%Y').weekday()
   
    dayRef = datetime.strptime(aRefDate, '%d/%m/%Y').weekday()

    if(day_name[day] == day_name[dayRef]):
        #dicto[day_name[day]] = []
        lst.append(aFinal)
        lst.append(aRefValue)
        dicto.update( {day_name[day]: [lst]} )
        dicto.update( {day_name[dayRef]: [lst]} )

    date, status, light = moon_phase(int(sDate[0:2]), int(sDate[3:5]), int(sDate[6:10]))        
    date_ref, status_ref, light_ref = moon_phase(int(aRefDate[0:2]), int(aRefDate[3:5]), int(aRefDate[6:10]))
    
    file = open("./logloto/{}-diff-{}.txt".format(nbr, datetime.today().strftime("%d-%m-%Y")),"a+")
    file.write("{} {} ☀️ {}{} ({})                          {} {} ☀️ {}{} ({})"
    .format(status, date, light, '%', day_name[day], status_ref, date_ref, light_ref, '%', day_name[dayRef])) 
    file.close()
    #print ("{} {} ☀️ {}{} ({})              {} {} ☀️ {}{} ({})").format(status, date, light, '%', day_name[day], status_ref, date_ref, light_ref, '%', day_name[dayRef])
    #return (day_name[day]) 

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