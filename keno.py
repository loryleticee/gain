# This Python file uses the following encoding: utf-8
import os, sys, time
import csv
from datetime import datetime, timedelta, date
from utils import topNumbers
from match import somByDay,somByMonth, tops_midi, tops_soir, tops_midi_month, tops_soir_month
from constant import nbr_tirage, path, nov19ToNow, fev19ToNov10, mar17ToFev19, csv_files, lap_more, count_day, lap, limit_tirages

n1 = int( sys.argv[1] )

def init():
    #nettoie le terminal
    os.system('clear')
    print('Runing ...')
    fileSize = open("./size.txt", "r")
    oldSize = fileSize.read()
    fileSize.close()
    newSize = os.popen("curl -sI https://media.fdj.fr/static/csv/keno/keno_202010.zip | grep -i Content-Length | awk '{print $2} '").read()

    if(newSize > oldSize):
        print('\n Mise à jour des derniers tirages en cours ...\n')
        #download last result file and unzip 
        os.system('wget https://media.fdj.fr/static/csv/keno/keno_202010.zip && unzip -o keno_202010.zip')
        #Move to keno file 
        os.system('mv keno_202010.csv keno')
        time.sleep(1)
        #delete zip file
        os.system('rm -rf keno_202010.zip')
        fileSize = open("./size.txt", "w+")
        fileSize.write(newSize)
        fileSize.close()
#END init()
#----------------------------------------------------------

def compare():
    global count_day
    global limit_tirages

    for file_lap, document in enumerate(csv_files):
        with open(path+document, 'r') as csv_file:
            csv_tirages = csv.reader(csv_file, delimiter=';')
            
            for row_lap, row in enumerate(csv_tirages):
                if (row_lap == 0):
                    continue
                #END if
                sTirage = row[4:24]
                sDate = row[1]
                sDay_phase = row[2]
                iTirage = map(int, sTirage)

                topNumbers(sDate, sDay_phase, list(iTirage))
            #END for

            for row_lap, row in enumerate(csv_tirages):
                if (row_lap == 0):
                    continue
                #END if
                sTirage = row[4:24]
                sDate = row[1]
                sDay_phase = row[2]
                iTirage = map(int, sTirage)
                if(int(count_day) < int(limit_tirages+1)):
                    count_day+=1
                    somByMonth(sDate, sDay_phase, list(iTirage))
                #END if
            #END for
    #END for

    if(os.path.exists("./logkeno/stats-{}.txt".format(datetime.today().strftime("%d-%m-%Y")))):
        file = open("./logkeno/stats-{}.txt".format(datetime.today().strftime("%d-%m-%Y")),"w+")
    else:
        file = open("./logkeno/stats-{}.txt".format(datetime.today().strftime("%d-%m-%Y")),"a+")

    items_phases_day =  {'tops_midi':tops_midi.items(), 'tops_midi_month':tops_midi_month.items(), 'tops_soir':tops_soir.items(), 'tops_soir_month':tops_soir_month.items()}

    for index, ph in enumerate(items_phases_day):
        sort_orders = sorted(items_phases_day[ph], key=lambda x: x[1], reverse=True)
        print('{} Numeros'.format(ph))
        file.write('{} Numeros \n'.format(ph))  
        for number in sort_orders:
            print('N '+number[0], number[1])
            file.write('N{}, {} \n'.format(number[0], number[1])) 
    file.close()

    #send stats in a telegram channel
    if(n1 == 1):
        os.system('telegram-send --file ./logkeno/stats-{}.txt'.format(datetime.today().strftime("%d-%m-%Y")))
    

#End def compare()
#----------------------------------------------------------

###------------------------------------------------------------- START HERE 

# Step 1 : Launch init function 
init()
# Step 2 : Launch compare function 
compare()
