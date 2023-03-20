import numpy as np

#Con la seguente funzione sono inizializzate le entrate mancanti della matrice dei rating con la media per riga calcolata
#sulla base dei soli valori osservati, quindi inseriamo nei rating una componente per utente
def inizializzazione_matrice(matrice, righe, colonne, Z):

    #per ogni riga della matrice dei rating R si estrae il numero di valori diversi da zero e tale valore è salvato in dim,
    #sono sommati poi i valori osservati e il valore è salvato in sum
    for i in range(0, righe):
        dim=len(np.argwhere(matrice[i] !=0))
        sum=np.sum(matrice[i, np.argwhere(matrice[i] !=0)])
        media=sum/dim
        #scorrendo le colonne della matrice dei rating, se il valore non è stato osservato si pone uguale alla media per
        #user la voce nella medesima posizione della matrice di zeri Z, altrimenti se il valore è stato osservato viene
        # salvato nella medesima posizione nella matrice di zeri Z
        for j in range(0, colonne):
            if matrice[i,j] ==0:
                Z[i,j]=media
            else:
                Z[i,j] =matrice[i,j]


