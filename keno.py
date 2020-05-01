# This Python file uses the following encoding: utf-8
import os, sys
import csv
from datetime import datetime,timedelta,date
from utils import delOldFiles, topNumbers, tops

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
die_daySort = False
lap_more = 0
lap = 1

def compare():
    for document in enumerate(csv_files):
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

"""askInit()"""

#Supprime les anciens logs
delOldFiles()
#nettoie le terminal
os.system('clear')

print('\n Calcul en cours ...\n')

compare()
