# This Python file uses the following encoding: utf-8
import os, sys
import csv
from datetime import datetime, timedelta, date
# from utils import topNumbers
from match import  somByDay, tops_midi
from constant import nbr_tirage, path, csv_files, lap_more, count_day, lap, limit_tirages
from utils import topNumbers

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
    print('Runing ...')
    fileSize = open("./size.txt", "r")
    oldSize = fileSize.read()
    fileSize.close()
    newSize = int(os.popen("curl -sI https://media.fdj.fr/static/csv/euromillions/euromillions_202002.zip | grep -i Content-Length | awk '{print $2} '").read())
  
    if(newSize > int(oldSize)):
        print('\n Mise à jour des derniers tirages en cours ...\n')
        #download last result file and unzip 
        os.system('wget https://media.fdj.fr/static/csv/euromillions/euromillions_202002.zip && unzip -o euromillions_202002.zip')
        #Move to keno file 
        os.system('mv euromillions_202002.csv euro')
        #change file to utf8 to match special char
        os.system("iconv -f ISO-8859-1 -t UTF-8//TRANSLIT './euro/euromillions_202002.csv' > 'euromillions_202002.csv'")
        #remvoe not utf8 file in /euro
        os.system('rm ./euro/euromillions_202002.csv')
        #move new file to dir
        os.system('mv euromillions_202002.csv euro')
        #replace é by e in file with make bug loop under
        os.system("sed -i.bu 's/é/e/g' ./euro/euromillions_202002.csv")
        #remove .bu file create by sed
        os.system("rm ./euro/*.bu")
        #delete zip file
        os.system('rm -rf euromillions_202002.zip')
        fileSize = open("./size.txt", "w+")
        fileSize.write(str(newSize))
        fileSize.close()
    else:
        print('Last result no yet save')
#END init()
#----------------------------------------------------------

def compare():
    global count_day
    global limit_tirages
    global n1
    global n2
    global n3
    global n4
    global n5
    global ip

    for file_lap, document in enumerate(csv_files):
        with open(path+document, 'r') as csv_file:
            csv_tirages = csv.reader(csv_file, delimiter=';')
            
            for row_lap, row in enumerate(csv_tirages):
                if (row_lap == 0):
                    continue

                sDate=row[2]

                if(file_lap == 0):
                    year = row[2][0:4]
                    month = row[2][4:6]
                    day = row[2][6:8]
                    # print(day+'/'+month+'/'+year)
                    sDate = str(day+'/'+month+'/'+year)

                sTirage = row[4:9]

                if(file_lap >=3 ):
                    sTirage = row[5:10]
                
                sComp = row[9]
                sDay_tirage = row[1]
                # sDate = row[2]
                iTirage = map(int, sTirage)
                #topNumbers(sDate, sDay_tirage, iTirage)
                somByDay(sTirage, n1, n2, n3, n4, n5, ip, sDate)
            #END for()
    #END for

init()
compare()