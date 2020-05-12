# This Python file uses the following encoding: utf-8
import os, sys
import csv
from datetime import datetime,timedelta,date
from utils import delOldFiles, topNumbers
from match import somByDay,somByMonth, tops_midi, tops_soir, tops_midi_month, tops_soir_month

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
                sDate = row[1]
                sDay_phase = row[2]

                iTirage = map(int, sTirage)

                if(sDate <= (datetime.today()-timedelta(days=6)).strftime("%d/%m/%Y")):
                    somByMonth(sDate, sDay_phase, sTirage)
                
                topNumbers(sDate, sDay_phase, iTirage)


    if(os.path.exists("./logkeno/stats-{}.txt".format(datetime.today().strftime("%d-%m-%Y")))):
        file = open("./logkeno/stats-{}.txt".format(datetime.today().strftime("%d-%m-%Y")),"w+")

    else:
        file = open("./logkeno/stats-{}.txt".format(datetime.today().strftime("%d-%m-%Y")),"a+")

    sort_orders = sorted(tops_midi.items(), key=lambda x: x[1], reverse=True)
    print('STATISTIQUES DU MATIN')
    file.write('STATISTIQUES DU MATIN \n')  
    for number in sort_orders:
        print('N '+number[0], number[1])
        file.write('N{}, {} \n'.format(number[0], number[1])) 

    sort_orders = sorted(tops_soir.items(), key=lambda y: y[1], reverse=True)
    print('STATISTIQUES DU SOIR')
    file.write('STATISTIQUES DU SOIR \n')  
    for number in sort_orders:
        print('N '+number[0], number[1])
        file.write('N{}, {} \n'.format(number[0], number[1]))  
    

    sort_orders = sorted(tops_midi_month.items(), key=lambda z: z[1], reverse=True)
    print('STATISTIQUES SUR LE DERNIERS MOI MATIN')
    file.write('STATISTIQUES SUR LE DERNIERS MOI MATIN \n')  
    for number in sort_orders:
        print('N '+number[0], number[1])
        file.write('N{}, {} \n'.format(number[0], number[1]))  
    

    sort_orders = sorted(tops_soir_month.items(), key=lambda a: a[1], reverse=True)
    print('STATISTIQUES SUR LE DERNIERS MOI SOIR')
    file.write('STATISTIQUES SUR LE DERNIERS MOI SOIR \n')  
    for number in sort_orders:
        print('N '+number[0], number[1])
        file.write('N{}, {} \n'.format(number[0], number[1]))
    file.close()

    #send stats in a telegram channel
    os.system('telegram-send --file ./logkeno/stats-{}.txt'.format(datetime.today().strftime("%d-%m-%Y")))

"""askInit()"""

#Supprime les anciens logs
delOldFiles()
#nettoie le terminal
os.system('clear')

print('\n Calcul en cours ...\n')

#download last result file and unzip
os.system('wget https://media.fdj.fr/static/csv/keno/keno_201811.zip && unzip -o keno_201811.zip')
#delete zip file
os.system('rm -rf keno_201811.zip')
#Move to keno file 
os.system('mv keno_201811.csv keno')
print('Done')

print('\n Calcul en cours ...\n')

compare()
#os.system('python match.py {}'.format())