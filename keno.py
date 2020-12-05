# This Python file uses the following encoding: utf-8
import os, sys
import csv
from datetime import datetime, timedelta, date
from utils import topNumbers
from match import somByDay, tops_midi
from constant import nbr_tirage, path, csv_files, lap_more, count_day, lap, limit_tirages


# numberArray = {x for x in range(1,51)}
# possibleComb = 1906884
numberArray = {x for x in range(1,10)}
possibleComb = 1023

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
    for file_lap, document in enumerate(csv_files):
        print('file_lap' ,file_lap)
        with open(path+document, 'r') as csv_file:
            csv_tirages = csv.reader(csv_file, delimiter=';')
            
            for row_lap, row in enumerate(csv_tirages):
                if (row_lap == 0):
                    continue

                sTirage = row[4:9]
                sDate = row[2]
                sComp = row[9]
                iTirage = map(int, sTirage)
                topNumbers(sDate, iTirage)
                

               
            #END for
    #END for
    if(os.path.exists("./logkeno/loto-{}.txt".format(datetime.today().strftime("%d-%m-%Y")))):
        file = open("./logkeno/loto-{}.txt".format(datetime.today().strftime("%d-%m-%Y")),"w+")
    else:
        file = open("./logkeno/loto-{}.txt".format(datetime.today().strftime("%d-%m-%Y")),"a+")
    sort_orders = sorted(tops_midi.items(), key=lambda x: x[1], reverse=True) 
    for number in sort_orders:
        file.write('N{}, {} \n'.format(number[0], number[1])) 
        #file.write('N{}, {} \n'.format(number[0], number[1])) 
    file.close()


def cartesian_product(s, dim):
    res = [(e,) for e in s]
    for i in range(dim - 1):
        res = [e + (f,) for e in res for f in s]
    return res

def cartesian():
    fileCartesian = open("./cartesian/cartesian.txt","w+")
    for i in range(possibleComb+1):
        if i != possibleComb:
            continue
        else:
            rawDatas = cartesian_product(numberArray, i)
            formatDatas = str(rawDatas).replace('(','[').replace(')',']')
            fileCartesian.write(formatDatas)
# Step 2 : Launch compare function 
#init()
#compare()
print('Realisation du produit cartesien ...')
cartesian()