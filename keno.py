# This Python file uses the following encoding: utf-8
import os, sys
import csv
from datetime import datetime

nbrTirage = 997

##Chemin où sont placées les fichiers csv
path = './loto'

#04/11/2019 <--> 27/04/2020 ####### novembre 2019 à maintenant (Retelecharger le ficher à chaque nouveau tirage)
nov19ToNow = '/loto_201911.csv'

#27/02/2019 <--> 02/11/2019
fev19ToNov10 = '/loto_201902.csv'

#06/03/2017 <--> 25/02/2019  
mar17ToFev19 = '/loto2017.csv'

#06/10/2008 <--> 04/03/2017
oct08ToMar17 = '/nouveau_loto.csv'

#19/05/1976 <--> 04/10/2008
#may76ToOct08 = '/loto.csv'

# Les 3 derniers fichiers csv ne sont pas formatés de la meme façon , la colonne des resultats est L au lieu de M
csv_files = [nov19ToNow, fev19ToNov10, mar17ToFev19, oct08ToMar17]#, may76ToOct08]

# Tableau qui sera comparé avec tous les autres tableaux suivant
aRef = []

tirage = 1

tops = {}

rangeWeek = 0

one_diff = {}

def createOneDiff(sDate, aFinal, aRef):
    day_name= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
    day = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    
    one_diff[]
    return (day_name[day]) 

def topNumbers(tops, aFinal):
    for number in aFinal:
        if (tops.get("{}".format(number)) is None):
            numa = 0
        else:
            numa = tops.get("{}".format(number))

        tops["{}".format(number)] =  1 + numa

def compare(tops, tirage, aRef, nbrTirage, rangeWeek, user_input):
    for fileLap, document in enumerate(csv_files):
        with open(path+document, 'r') as csv_file:
            csv_tirages = csv.reader(csv_file, delimiter=';')
            
            for tirageLap, row in enumerate(csv_tirages):
                if (tirageLap == 0):
                    continue

                sRow = row[10]
                sDate = row[2]

                # Si le fichier est ancien formater la date
                if (fileLap == 4):
                    sRow = row[12]
                    sDate = str(row[3][6:8])+'/'+(str(row[3][4:6]))+'/'+str(row[3][0:4])

                # Remplace les tiret par des virgule afin de construire une liste(un tableau)
                sArray  = sRow.replace('-',',')
                sArray = sArray.split("+")[0].split(",")

                # Transforme le tableau de chaine de caractere en tableau d'entier
                aFinal = map(int, sArray) 

                #Si on est au premier tour de boucle , le tableau qui sera comparé à tous les autres suivant sera le premier 
                if (fileLap == 0 and tirageLap == tirage):
                    aRef = [aFinal, sDate]
                    #print('INIT DE aref {}'.format(aRef))

                #Tableau contenant les nombres differents
                aDiff   = list(set(aFinal) - set(aRef[0]))
                #Tableau inversé contenant les nombres differents
                aDiff2  = list(set(aRef[0]) - set(aFinal))

                if(rangeWeek < user_input):
            	    #somme les sortie de chaque numéros distinct 
                    topNumbers(tops, aFinal)
                    rangeWeek+=1

                #Tirages avec moins de 3 chiffres dfferents
                """if (len(aDiff) < 3 and len(aDiff) > 0):
                    file = open("./logloto/testfile{}-{}.txt".format(tirageLap, fileLap),"w") 
                    file.write("2 chiffres différencies ces Tirages \n Trouvé dans le fichier {} \n Le {} Tirage {} ressemble au tirage {} du {} Differences: {} \n".format(fileLap, sDate, aFinal, aRef[0], aRef[1], aDiff)) 
                    file.close()"""
                if (len(aDiff) < 2 and len(aDiff) > 0):
                    file = open("./logloto/2-diff-{}.txt".format(datetime.today().strftime("%d-%m-%Y")),"a+")
                    file.write("\n ⏱ {} {} ⏰{} {} Diffs: {}replace by{} \r\n".format(sDate, aFinal, aRef[1], aRef[0], aDiff, aDiff2)) 
                    file.close()
                    print("⏱ {} {} ⏰{} {} Diffs: {}replace by{}\n".format(sDate, aFinal, aRef[1], aRef[0], aDiff, aDiff2))  
                    createOneDiff(sDate, aFinal, aRef)

    tirage+=1
    if(tirage < nbrTirage):
        compare(tops, tirage, aRef, nbrTirage,rangeWeek, user_input)
    else:
        sort_orders = sorted(tops.items(), key=lambda x: x[1], reverse=True)
        print("Statistic de somme selon la(es) {} derniere(s) semaines(s) \n".format(user_input/2))
        for i in sort_orders:
	        print('N '+i[0], i[1])

if (len(sys.argv) < 2):
    print('\n Tapez control(^)+c pour annuler.\n')
    user_input = input("Enter le nombre de tirage pris en compte pour les statistiques des Tops numbers: \n")
else:
    user_input = int(sys.argv[1])*2
print('\n Calcul en cours ...\n')
compare(tops, tirage, aRef, nbrTirage, rangeWeek, user_input)
