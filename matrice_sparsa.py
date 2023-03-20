import csv
import numpy
import codecs
import campione_per_idUtente

#Inizializziamo delle liste vuote
nuovi_id=[]
nuovi_film=[]
rows=[]
R=[]

def creazione_matrice(data, files, num_utenti):

    campione_per_idUtente.campionamento(data, files, num_utenti)

    # Apriamo in lettura il dataset contenente i dati campionati
    file = codecs.open("dati_campionati.csv")
    file2 = csv.reader(file)

    # salviamo in un vettore il contenuto del file dati_campionati.csv
    for riga in file2:
        rows.append(riga)

    file.close()

    # per ogni riga, salviamo in nuovi_id i codici identificativi deglu utenti e in nuovi_film i codici identificativi
    # dei film
    for i in rows:
        nuovi_id.append(i[1])
        nuovi_film.append(i[0])

    indici2 = list(numpy.unique(nuovi_id))
    film2 = list(numpy.unique(nuovi_film))
    righe = len(indici2)

    # Per ogni codice identificativo dei film creiamo una riga di zero di lunghezza pari al vettore dei codici
    # identificativi degli utenti
    for i in film2:
        R.append([0] * righe)

    # Per ogni riga del file dati_campionati.csv popoliamo la matrice dei rating con il rating per la specifica
    # coppia (film_i, id_j)
    for i in rows:
        R[film2.index(i[0])][indici2.index(i[1])] = i[2]

    with open('matrice_R.csv', 'w', newline='') as file:
        mywriter = csv.writer(file, delimiter=',')
        mywriter.writerows(R)

    file.close()







