# This Python file uses the following encoding: utf-8
import os, sys
import csv
from datetime import datetime, timedelta, date
from utils import topNumbers
from match import somByDay, tops_midi
from constant import nbr_tirage, path, csv_files, lap_more, count_day, lap, limit_tirages

n1 = int( sys.argv[1] )
n2 = int( sys.argv[2] )
n3 = int( sys.argv[3] )
n4 = int( sys.argv[4] )
n5 = int( sys.argv[5] )

def init():
    #nettoie le terminal
    os.system('clear')

    print('\n Mise à jour des derniers tirages en cours ...\n')

    #download last result file and unzip 
    os.system('wget https://media.fdj.fr/static/csv/keno/keno_201811.zip && unzip -o keno_201811.zip')
    #delete zip file
    os.system('rm -rf keno_201811.zip')
    #Move to keno file 
    os.system('mv keno_201811.csv keno')
    print('Done')

    print('\n Calcul en cours ...\n')
#END init()
#----------------------------------------------------------

def compare():
#    global count_day
#    global limit_tirages

    for file_lap, document in enumerate(csv_files):
        print('file_lap' ,file_lap)
        with open(path+document, 'r') as csv_file:
            csv_tirages = csv.reader(csv_file, delimiter=';')
            
            for row_lap, row in enumerate(csv_tirages):
                if (row_lap == 0):
                    continue

                sTirage = row[4:9]
                sComp = row[9]
                #print(sTirage)
                #print('comp = ',sComp)

                iTirage = map(int, sTirage)
                somByDay(sTirage, n1, n2, n3 , n4, n5)
            #END for
    #END for
    print('--------------------- \n\n')
    sort_orders = sorted(tops_midi.items(), key=lambda x: x[1], reverse=True)
    #file.write('{} Numeros \n'.format(ph))  
    for number in sort_orders:
        print('N '+number[0], number[1])
        #file.write('N{}, {} \n'.format(number[0], number[1])) 

# Step 2 : Launch compare function 
compare()
