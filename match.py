import os
from datetime import datetime, timedelta, date
from constant import tops_midi
from utils import getDate, getDayWord, month_name, day_name
isN1 = isN2 = isN3 = isN4 = False

fileIsEmpty = True

def somByDay4(sTirage, n1, n2, n3, n4, ip, sDate):
    ipAdress = ip.replace('.','')

    global isN1
    global isN2
    global isN3
    global isN4
    global fileIsEmpty

    for item in sTirage:
        number = tops_midi.get("{}".format(item))
        tops_midi["{}".format(item)] =  number + 1

        if(str(item) == str(n1)):
            isN1 = True
            continue

        if(str(item) == str(n2)):
            isN2 = True
            continue
        if(str(item) == str(n3)):
            isN3 = True
            continue

        if(str(item) == str(n4)):
            isN4 = True
            continue

    if(isN1 == True & isN2 == True & isN3 == True & isN4 == True):
        if(os.path.exists("./exist/exist-"ipAdress+".txt")):
            fileTiragExist = open("./exist/exist-"ipAdress+".txt","a+")
        else:
            fileTiragExist = open("./exist/exist-"ipAdress+".txt","w+")
        
        iTirage = list(map(int, sTirage))
        tirage = str(iTirage)

        fileTiragExist.write(str('[["'+getDate(sDate)+'"],'+str(tirage)+']'))
        fileIsEmpty = False

        isN1 = isN2 = isN3 = isN4 = False
        print(tirage + ' ' + getDate(sDate))
    else:
        isN1 = isN2 = isN3 = isN4 = False
    
    if (fileIsEmpty):
        fileTiragExist = open("./exist/exist-"+ipAdress+".txt","w+")
        fileTiragExist.write('[[]]')
#fileTiragExist.close()