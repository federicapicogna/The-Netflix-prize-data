import csv
import numpy as np
import random
import creazione_dataset

#Inizializzazione:
nuovi_id = []
chosen_row = []
nuovi_id_unici = []
recensioni = []
recensioni_campionate = []

#Nella seguente funzione viene effettuato un campionamento di 10.000 codici identificativi dal dataset originale.
def campionamento(data, files, num_utenti):

 index = []
 creazione_dataset.manipolazione_dataset(data, files)

 with open("dati.csv", newline='') as f:
    reader = csv.reader(f)
    #è estratta la colonna contenente i codici identificativi degli user
    for i in reader:
        nuovi_id.append(int(i[1]))
    #sono eliminate le ripetizioni dei codici identificativi
    nuovi_id_unici = np.unique(nuovi_id)
    #sono selezionati in modo randomico 10.000 utenti
    chosen_row = random.sample(list(nuovi_id_unici), k=num_utenti)
    chosen_row = sorted(chosen_row)

    #Dal dataset originale sono estratte tutte le posizioni dove compare ciascun codice identificativo
    for i in range(0, len(chosen_row)):
        posizioni = np.where(nuovi_id == chosen_row[i])
        index = np.append(index, posizioni)
    index = np.asarray(index, dtype="int64")

 the_file = open("dati.csv", "r")
 reader = csv.reader(the_file)

 #sono estratte tutte le righe del dataset completo
 for row in reader:
     recensioni.append(row)

#sono salvate le righe corrispondenti alle posizioni individuate precedentemente
 for i in index:
     recensioni_campionate.append(recensioni[i])

 with open('dati_campionati.csv', 'w', newline='') as file:
     mywriter = csv.writer(file, delimiter=',')
     mywriter.writerows(recensioni_campionate)

 the_file.close()