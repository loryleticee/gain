# This Python file uses the following encoding: utf-8
nbr_tirage = 60 #(997)

#Chemin où sont placées les fichiers csv
path = './keno'

#12/01/2019 <--> 30/04/2020 ####### novembre 2019 à maintenant (Retelecharger le ficher à chaque nouveau tirage)
may76ToOct08 = '/loto.csv'

#24/02/2013 <--> 11/11/2018
Oct08ToMar17 = '/nouveau_loto.csv'

#16/09/1993 <--> 23/02/2013  
mar17ToFev19 = '/loto2017.csv'

fev19ToNov19 = '/loto_201902.csv'

nov19ToNow = '/loto_201911.csv'

# Les 3 derniers fichiers csv ne sont pas formatés de la meme façon , la colonne des resultats est L au lieu de M
csv_files = [Oct08ToMar17, mar17ToFev19, fev19ToNov19, nov19ToNow]

lap_more = count_day = 0
lap = 1
limit_tirages = 6

tops_midi= {str(x): 0 for x in range(1,51)}