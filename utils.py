from datetime import datetime

day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
month_name = ['null_month','January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


def getDate (sDate):
    jour = int(sDate[0:2])
    mois = int(sDate[3:5])
    annee = int(sDate[6:10])

    day_word = getDayWord(getDayNumber(sDate))
    month_word = month_name[mois]

    return day_word+' '+str(jour)+' '+ month_word + ' '+ str(annee)
    
def getDayWord(iDay):
    global day_name
    return str(day_name[iDay])

def getDayNumber(sDate):
    return int(datetime.strptime(sDate, '%d/%m/%Y').weekday())
