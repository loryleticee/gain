# This Python file uses the following encoding: utf-8
import os, sys
import csv
from datetime import datetime
from utils import getMoon, dicto , showPourcent, delOldFiles, daySort , reverseCompare, topNumbers, tops

nbr_tirage = 60 #(997)

##Chemin où sont placées les fichiers csv
path = './keno'

#04/11/2019 <--> 29/04/2020 ####### novembre 2019 à maintenant (Retelecharger le ficher à chaque nouveau tirage)
nov19ToNow = '/keno_201811.csv'

#27/02/2019 <--> 02/11/2019
fev19ToNov10 = '/keno_gagnant_a_vie.csv'

#06/03/2017 <--> 25/02/2019  
mar17ToFev19 = '/keno.csv'

# Les 3 derniers fichiers csv ne sont pas formatés de la meme façon , la colonne des resultats est L au lieu de M
csv_files = [nov19ToNow, fev19ToNov10, mar17ToFev19]#, may76ToOct08]

# Tableau qui sera comparé avec tous les autres tableaux suivant
aRef = []
die_daySort = False
lap_more = 0
lap = 1
range_week = 0

def compare(nbr_tirage, user_input):
    global aRef
    global range_week
    global tops
    global lap
    global lap_more
    for file_lap, document in enumerate(csv_files):
        with open(path+document, 'r') as csv_file:
            csv_tirages = csv.reader(csv_file, delimiter=';')
            
            for row_lap, row in enumerate(csv_tirages):
                if (row_lap == 0):
                    continue
                
                sTirage = row[4:24]
                sDate = row[1]# Transforme le tableau de chaine de caractere en tableau d'entier

                iTirage = map(int, sTirage)

                if(range_week < user_input):
                    #somme les sortie de chaque numéros distinct 
                    topNumbers(iTirage)
                    range_week+=1
                
                #Si on est au premier tour de boucle , le tableau qui sera comparé à tous les autres suivant sera le premier 
                if (lap_more != lap):
                    aRef = [iTirage, sDate]
                    lap_more = lap_more+1

                    if(lap_more > 0):
                        lap_more=1
                
                if (row_lap > 1):  
                    #Tableaux contenant les nombres qui le differencie de l'autre
                    aDiff, aDiff2   = reverseCompare(iTirage, aRef[0])
                    
                    if (len(aDiff) > 7 and len(aDiff) < 9 ):
                        getMoon(1, sDate, aRef[1])
                        file = open("./logkeno/1-diff-{}.txt".format(datetime.today().strftime("%d-%m-%Y")),"a+")
                        file.write("\n ⏱ {} {}      ⏰{} {} Diffs: {}replace by{} \r\n".format(sDate, iTirage, aRef[1], aRef[0], aDiff, aDiff2)) 
                        file.close()
                    
                        #print("⏱ {} {}      ⏰{} {} Diffs: {}replace by{}\n".format(sDate, aFinal, aRef[1], aRef[0], aDiff, aDiff2)) 

        if(file_lap == (len(csv_files) -1 )):
            lap_more = 0

    sort_orders = sorted(tops.items(), key=lambda x: x[1], reverse=True)
    print("Statistic de somme selon la(es) {} derniere(s) semaines(s) \n".format(user_input/21))

    for i in sort_orders:
        print('N '+i[0], i[1])

if (len(sys.argv) < 2):
    print('\n Tapez control(^)+c pour annuler.\n')
    user_input = input("Enter le nombre de tirage pris en compte pour les statistiques des Tops numbers: \n")
else:
    user_input = int(sys.argv[1])*21

#Supprime les anciens logs
delOldFiles()
#nettoie le terminal
os.system('clear')

print('\n Calcul en cours ...\n')

compare(nbr_tirage, user_input)
