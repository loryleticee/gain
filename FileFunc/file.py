import os, time
from datetime import datetime, timedelta
from match import tops_midi, tops_soir, tops_midi_month, tops_soir_month
from moon import moon_phase
from dotenv import load_dotenv
from pathlib import Path  # Python 3.6+ only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

def get_remote_stats_file_size():
    return os.popen("curl -sI " + os.getenv('KENO') + " | grep -i Content-Length | awk '{print $2} '").read()

def get_local_stats_file_size():
    #Ouvrir le fichier en leture
    file = open("./size.txt", "r")
    oldSize = file.read()
    file.close()

    return oldSize

def stats_file_is_update():
    remote_file_size = get_remote_stats_file_size()
    if(remote_file_size > get_local_stats_file_size()):
        download_new_stats_file()
        set_local_stats_file_size(remote_file_size)

def set_local_stats_file_size(new_size):
    #Ouvrir le fichier en ecriture
    file = open("./size.txt", "w+")
    file.write(new_size)
    file.close()

def download_new_stats_file():
    print('\n Mise à jour des derniers tirages en cours ...\n')
    #download last result file and unzip it for get the csv file
    os.system('wget ' + os.getenv('KENO') + ' && unzip -o keno_202010.zip')
    #Move the csv file to keno directory
    os.system('mv ../keno_202010.csv ../keno')
    #pause d'une seconde
    time.sleep(1)
    #delete zip file
    os.system('rm -rf keno_202010.zip')

def save_result():
    if(os.path.exists(os.getenv('STATS_PATH')+"{}.txt".format(datetime.today().strftime("%d-%m-%Y")))):
        file = open(os.getenv('STATS_PATH')+"{}.txt".format(datetime.today().strftime("%d-%m-%Y")),"w+")
    else:
        file = open(os.getenv('STATS_PATH')+"{}.txt".format(datetime.today().strftime("%d-%m-%Y")),"a+")

    items_phases_day =  {'tops_midi':tops_midi.items(), 'tops_midi_month':tops_midi_month.items(), 'tops_soir':tops_soir.items(), 'tops_soir_month':tops_soir_month.items()}

    for index, ph in enumerate(items_phases_day):
        sort_orders = sorted(items_phases_day[ph], key=lambda x: x[1], reverse=True)
        print('{} Numeros'.format(ph))
        file.write('{} Numeros \n'.format(ph))  
        for number in sort_orders:
            print('N '+number[0], number[1])
            file.write('N{}, {} \n'.format(number[0], number[1])) 
    file.close()