from datetime import datetime, timedelta, date
from constant import tops_midi
from utils import getDate, getDayWord, month_name, day_name
isN1 = isN2 = isN3 = False
            
def somByDay3(iTirage, n1, n2, n3, ip, sDate):
    ipAdress = ip.replace('.','')
    now =  date.today().strftime("%d-%m-%Y")

    global isN1
    global isN2
    global isN3

    for item in iTirage:
        number = tops_midi.get("{}".format(item))
        tops_midi["{}".format(item)] =  number + 1

        if(str(item) == str(n1)):
            isN1 = True

        if(str(item) == str(n2)):
            isN2 = True

        if(str(item) == str(n3)):
            isN3 = True

    if(isN1 == True & isN2 == True & isN3 == True):
        fileTiragExist = open("./exist/exist-"+ now +'-'+ ipAdress+".txt","w+")
        fileTiragExist.write(str('[["'+getDate(sDate)+'"],'+str(iTirage)+']'))
        isN1 = isN2 = isN3 = False
    else:
        isN1 = isN2 = isN3 = False
    # fileTiragExist.close()
