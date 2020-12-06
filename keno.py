# This Python file uses the following encoding: utf-8
import os, sys
import csv
from datetime import datetime, timedelta, date
# from utils import topNumbers
from match import  somByDay5, tops_midi
from constant import nbr_tirage, path, csv_files, lap_more, count_day, lap, limit_tirages

n1 = int( sys.argv[1] )
n2 = int( sys.argv[2] )
n3 = int( sys.argv[3] )
n4 = int( sys.argv[4] )
n5 = int( sys.argv[5] )
ip = str( sys.argv[6] )
i = 0

def init():
    #nettoie le terminal
    os.system('clear')

    print('\n Mise à jour des derniers tirages en cours ...\n')
    #download last result file and unzip 
    os.system('wget https://media.fdj.fr/static/csv/loto/loto_201911.zip && unzip -o loto_201911.zip')
    #delete zip file
    os.system('rm -rf loto_201911.zip')
    #Move to keno file 
    os.system('mv -f loto_201911.csv keno')
    print('Done')

    print('\n Calcul en cours ...\n')
#END init()
#----------------------------------------------------------

def compare():
    os.system('clear')
    global count_day
    global limit_tirages
    global n1
    global n2
    global n3
    global n4
    global n5
    global ip
    global i 

    for file_lap, document in enumerate(csv_files):
        print('file_lap' ,file_lap)
        with open(path+document, 'r') as csv_file:
            csv_tirages = csv.reader(csv_file, delimiter=';')
            
            for row_lap, row in enumerate(csv_tirages):
                if (row_lap == 0):
                    continue
                sTirage = row[4:9]
                sComp = row[9]
                sDate = row[2]
                iTirage = map(int, sTirage)
                somByDay5(sTirage, n1, n2, n3, n4, n5, ip, sDate)
                i+=1
            #END for
    #END for
    # sort_orders = sorted(tops_midi.items(), key=lambda x: x[1], reverse=True)
    # for number in sort_orders:
    #     print('N '+number[0], number[1])
    # print ('I',i)


# Step 2 : Launch compare function 
# init()
compare()