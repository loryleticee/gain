from itertools import product

# This Python file uses the following encoding: utf-8
nbr_tirage = 60 #(997)

#Chemin où sont placées les fichiers csv
path = './keno'

now = '/keno_202010.csv'

#12/01/2019 <--> 30/04/2020 ####### novembre 2019 à maintenant (Retelecharger le ficher à chaque nouveau tirage)
nov19ToNow = '/keno_201811.csv'

#24/02/2013 <--> 11/11/2018
fev19ToNov10 = '/keno_gagnant_a_vie.csv'

#16/09/1993 <--> 23/02/2013  
mar17ToFev19 = '/keno.csv'

# Les 3 derniers fichiers csv ne sont pas formatés de la meme façon , la colonne des resultats est L au lieu de M
csv_files = [now, nov19ToNow, fev19ToNov10, mar17ToFev19]#, may76ToOct08]

lap_more = count_day = 0
lap = 1
limit_tirages = 6

tops_soir_month = {str(x): 0 for x in range(1,71)}
tops_midi_month = {str(x): 0 for x in range(1,71)}
tops_soir= {str(x): 0 for x in range(1,71)}
tops_midi= {str(x): 0 for x in range(1,71)}