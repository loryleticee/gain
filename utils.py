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

def topNumbers(sDate, sDay_tirage, iTirage):
    global month_name
       
    print(jour, sDate)
    exit()

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
                        print("{}--{} {} ☀️ {}% ({})   Today is : {} {} {} ☀️ {}% ".format(status, day_word, date, light, sDay_tirage, sToday_status, sToday_day_word, sToday_date, sToday_light ))
                        print("\x1b[5;10;42m 🧨 {} \x1b[0m \n".format(iTirage))
                        somByDay(sDate, sDay_tirage, list(iTirage))
                    else:
                        print("{}--{} {} ☀️ {}% ({})  Today is : {} {} {} ☀️ {}% ".format(status, day_word, date, light, sDay_tirage,  sToday_status, sToday_day_word, sToday_date, sToday_light ))
                        print("\x1b[6;30;42m Top 1 {} \x1b[0m \n".format(list(iTirage)))
                        somByDay(sDate, sDay_tirage, list(iTirage))
                else:
                    #somByDay(sDate, sDay_tirage, iTirage)
                    print("{}--{} {} ☀️ {}% ({})   Today is : {} {} {} ☀️ {}% ".format(status, day_word, date, light, sDay_tirage,  sToday_status, sToday_day_word, sToday_date, sToday_light))
                    print('Top 2 {}  \n'.format(list(iTirage)))