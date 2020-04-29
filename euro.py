# This Python file uses the following encoding: utf-8
import os, sys

import csv

nbrTirage = 997

##Chemin où sont placées les fichiers csv
path = './euro'

#04/02/2020 <--> 24/04/2020 ####### Fevrier 2020 à maintenant (Retelecharger le ficher à chaque nouveau tirage)
feb20ToNow = '/euromillions_202002.csv'

#01/03/2019 <--> 31/01/2020
mar19ToJan20 = '/euromillions_201902.csv'

#27/09/2016 <--> 26/02/2019  
sep16ToFev19 = '/euromillions_4.csv'

#04/02/2014 <--> 23/09/2016
fev14ToSep16 = '/euromillions_3.csv'

#10/05/2011 <--> 31/01/2014
may11ToJan14 = '/euromillions_2.csv'

#13/02/2004 <--> 06/05/2011
feb04ToMay11 = '/euromillions.csv'

# Les 3 derniers fichiers csv ne sont pas formatés de la meme façon , la colonne des resultats est L au lieu de M
csv_files = [feb20ToNow, mar19ToJan20, sep16ToFev19, fev14ToSep16, may11ToJan14, feb04ToMay11]

# Tableau qui sera comparé avec tous les autres tableaux suivant
aRef = []

tirage = 1

tops = {}

def topNumbers(tops, aFinal):
    for number in aFinal:
        if (tops.get("{}".format(number)) is None):
            numa = 0
        else:
            numa = tops.get("{}".format(number))

        tops["{}".format(number)] =  1 + numa

def compare(tops,tirage, aRef, nbrTirage):
    for fileLap, document in enumerate(csv_files):
        with open(path+document, 'r') as csv_file:
            csv_tirages = csv.reader(csv_file, delimiter=';')
            
            for tirageLap, row in enumerate(csv_tirages):
                if (tirageLap == 0):
                    continue

                sRow = row[12]
                sDate = row[2]
                #
                if (fileLap > 2):
                    sRow = row[11]
                    sDate = str(row[2][6:8])+'/'+(str(row[2][4:6]))+'/'+str(row[2][0:4])
                # Remplace les tiret par des virgule afin de construire une liste(un tableau)
                sArray  = sRow.replace('-',',')
                # Retire la premier virgule de la liste
                aFilter1 = sArray[1:]
                # Retire la dernière virgule de la liste
                aFilter2 = aFilter1[:-1].split(',')
                # Transforme le tableau de chaine de caractere en tableau d'entier
                aFinal = map(int, aFilter2) 

                #print('TIRAGE {}'.format(tirage))
                #Si on est au premier tour de boucle , le tableau qui sera comparé à tous les autres suivant sera le premier 
                if (fileLap == 0 and tirageLap == tirage):
                     aRef = [aFinal, sDate]
                    #print('INIT DE aref {}'.format(aRef))

                aDiff   = list(set(aFinal) - set(aRef[0]))
                
                topNumbers(tops, aFinal)
                #Tirages avec moins de 3 chiffres dfferents

                #if (len(aDiff) < 3 and len(aDiff) > 0):
                #    file = open("./logeuro/testfile{}-{}.txt".format(tirageLap, fileLap),"w") 
                #    file.write("2 chiffres différencies ces Tirages \n Trouvé dans le fichier {} \n Le {} Tirage {} ressemble au tirage {} du {} Differences: {} \n".format(fileLap, sDate, aFinal, aRef[0], aRef[1], aDiff)) 
                #    file.close()

                if (len(aDiff) < 2 and len(aDiff) > 0):
                    TGREEN =  '\033[32m' # Green Text
                    print(TGREEN + "Le {} Tirage {} ressemble au tirage {} du {} Differences: {} \n".format(sDate, aFinal, aRef[0], aRef[1], aDiff)) 
                
                if (len(aDiff) < 3 and sDate!=aRef[1]):
                    print( "🕓{} ⛳️{} like 🕓{} 🏄🏻‍♂️{} Differences: {} \n".format(sDate, aFinal, aRef[1], aRef[0], aDiff)) 
                
                #print('{} Base {} Diff {} index :{}'.format(fileLap, aFinal, aDiff, tirageLap))
                #print('{}{}'.format(row[12], row[13]))
    tirage+=1
    if(tirage < nbrTirage):
        compare(tops, tirage, aRef, nbrTirage)
    else:
        sort_orders = sorted(tops.items(), key=lambda x: x[1], reverse=True)
        for i in sort_orders:
	        print('N '+i[0], i[1])
compare(tops,tirage, aRef, nbrTirage)