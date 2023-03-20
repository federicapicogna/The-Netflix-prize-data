#creiamo il dataset che andremo ad utilizzare, risistemato e tenendo conto solo di combined_data_1

#Con il seguente ciclo for rimuoviamo la linea con la struttura "movie_id:" e aggiungiamo una nuova colonna con il codice
#identificativo del film senza la struttura con i due punti, successivamente si combinano tutti i dati nel
#file in un unico file csv

def manipolazione_dataset(data, files):
 for file in files:
    print("Opening file: {}".format(file))
    with open(file) as f:
        for line in f:
            line = line.strip()
            if line.endswith(':'):
                movie_id = line.replace(':', '')
            else:
                data.write(movie_id + ',' + line)
                data.write('\n')


