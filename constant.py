# This Python file uses the following encoding: utf-8
nbr_tirage = 60 #(997)

#Chemin où sont placées les fichiers csv
path = './euro'

cinq = '/euromillions_202002.csv'

quatre = '/euromillions_201902.csv' #

trois = '/euromillions_4.csv'

deux = '/euromillions_3.csv' #

un = '/euromillions_2.csv' #

zero = '/euromillions.csv'

# Les 3 derniers fichiers csv ne sont pas formatés de la meme façon , la colonne des resultats est L au lieu de M
csv_files = [zero, un, deux ,trois, quatre, cinq]

lap_more = count_day = 0
lap = 1
limit_tirages = 6

tops_midi= {str(x): 0 for x in range(1,51)}