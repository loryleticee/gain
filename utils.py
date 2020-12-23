# This Python file uses the following encoding: utf-8
import os, sys, glob
from datetime import datetime

day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']

# def askInit():
#     global user_input
#     if (len(sys.argv) < 2):
#         print('\n Tapez control(^)+c pour annuler.\n')
#         user_input = input("Enter le nombre de tirage pris en compte pour les statistiques des Tops numbers: \n")
#     else:
#         user_input = int(sys.argv[1])*21

def getDayNumber(sDate):
    return int(datetime.strptime(sDate, '%d/%m/%Y').weekday())
#----------------------------------------------------------------------------

def getDayWord(iDay):
    global day_name
    return str(day_name[iDay])