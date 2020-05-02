# This Python file uses the following encoding: utf-8
import os, sys
import csv
from datetime import datetime,timedelta,date
from utils import delOldFiles, topNumbers
from match import somByDay, tops

nbr_tirage = 60 #(997)

##Chemin où sont placées les fichiers csv
path = './keno'

#12/01/2019 <--> 30/04/2020 ####### novembre 2019 à maintenant (Retelecharger le ficher à chaque nouveau tirage)
nov19ToNow = '/keno_201811.csv'

#24/02/2013 <--> 11/11/2018
fev19ToNov10 = '/keno_gagnant_a_vie.csv'

#16/09/1993 <--> 23/02/2013  
mar17ToFev19 = '/keno.csv'

# Les 3 derniers fichiers csv ne sont pas formatés de la meme façon , la colonne des resultats est L au lieu de M
csv_files = [nov19ToNow, fev19ToNov10, mar17ToFev19]#, may76ToOct08]

# Tableau qui sera comparé avec tous les autres tableaux suivant
die_daySort = False
lap_more = 0
lap = 1

def compare():
    for file_lap, document in enumerate(csv_files):
        #print('A: {} B:{}'.format(file_lap,document))

        with open(path+document, 'r') as csv_file:
            csv_tirages = csv.reader(csv_file, delimiter=';')
            
            for row_lap, row in enumerate(csv_tirages):
                #print('C: {} D:{}'.format(row_lap, row))
                if (row_lap == 0):
                    continue
                
                sTirage = row[4:24]
                sDate = row[1]# Transforme le tableau de chaine de caractere en tableau d'entier
                sDay_phase = row[2]

                iTirage = map(int, sTirage)

                topNumbers(sDate, sDay_phase, iTirage)

    sort_orders = sorted(tops.items(), key=lambda x: x[1], reverse=True)
    for number in sort_orders:
        print('N '+number[0], number[1])

"""askInit()"""

#Supprime les anciens logs
delOldFiles()
#nettoie le terminal
os.system('clear')

print('\n Calcul en cours ...\n')

compare()
#os.system('python match.py {}'.format())