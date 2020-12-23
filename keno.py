# This Python file uses the following encoding: utf-8
import constant as const
import csv
import FileFunc.file  as ff
import match
import os, sys, time

n1 = int( sys.argv[1] )

def init():
    #nettoie le terminal
    os.system('clear')
    print('Runing ...')
    ff.stats_file_is_update()
#----------------------------------------------------------

def compare():
    for file_lap, document in enumerate(const.csv_files):
        with open(const.path + document, 'r') as csv_file:
            csv_tirages = csv.reader(csv_file, delimiter=';')
            
            for row_lap, row in enumerate(csv_tirages):
                if (row_lap == 0):
                    continue
                sDate, sDay_phase, format_tirage = match.get_draw(row)
                match.topNumbers(sDate, sDay_phase, format_tirage)
            
                if(int(const.count_day) < int(const.limit_tirages+1)):
                    const.count_day+=1
                    match.somByMonth(sDate, sDay_phase, format_tirage)
    ff.save_result()

    #send stats in a telegram channel
    if(n1 == 1):
        os.system('telegram-send --file ./logkeno/stats-{}.txt'.format(datetime.today().strftime("%d-%m-%Y")))
#----------------------------------------------------------
 
init()

compare()
