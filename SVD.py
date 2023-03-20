import numpy as np
from sklearn.utils.extmath import randomized_svd
import csv
import inizializzazione_matrice_SVD


#Nella seguente funzione è applicata l'SVD troncata alla matrice dei rating, dopo averne inizializzato i valori mancanti
#l'output dell'algoritmo è salvato in un file CSV
def SVD_troncata(matrice, righe, colonne, Z, err_soglia, fattori):

    #è inizializzata la matrice dei rating sostituendo ai valori mancanti il valore della media per user
    inizializzazione_matrice_SVD.inizializzazione_matrice(matrice, righe, colonne, Z)
    Matrice_densa = Z

    #sono salvate le posizioni in corrispondenza delle quali non è stata osservata una valutazione
    zero_pos = np.argwhere(matrice == 0)
    z_righe, z_colonne = np.shape(zero_pos)
    rows = zero_pos[:, 0]
    cols = zero_pos[:, 1]

    #è inizializzato l'errore a zero e la convergenza è posta uguale a "False" così che si possano fare delle iterazioni
    #fino a quando non si raggiunge convergenza sfruttando il ciclo while
    err1 = 0
    convergence = False
    count=0

    #alla prima iterazione l'SVD è calcolata per la matrice con le medie, dalla seconda iterazione in poi è applicata
    #alla matrice che contiene le stime dei valori mancanti al posto delle medie
    while (convergence == False):

        count=count+1

        U, d, V_t = randomized_svd(Matrice_densa, n_components=fattori)

        #è calcolata l'approssimazione della matrice
        Matrice_densa_svd = np.dot(np.dot(U, np.diag(d)), V_t)

        # è verificato l'errore per la convergenza, si utilizzano le stime degli elementi nulli nella matrice di partenza,
        # si calcola l'errore come norma di frobenius confrontando i valori stimati degli elementi nulli e gli stessi dell'iterazione
        err_final1 = (Matrice_densa_svd[rows, cols] - Matrice_densa[rows, cols]) ** 2
        err_final = 0.5 * np.sum(err_final1)

        # se l'errore è inferiore alla soglia scelta la convergenza è stata raggiunta, che si raggiunga la convergenza
        #o meno i valori stimati sono sostituiti nelle posizioni di valori nulli della matrice dell'iterazione precedente
        if abs(err_final - err1) < err_soglia:
            for i in range(z_righe):
                Matrice_densa[zero_pos[i][0]][zero_pos[i][1]] = abs(Matrice_densa_svd[zero_pos[i][0]][zero_pos[i][1]])
            convergence = True
            #salvataggio risultati:
            with open('risultati_SVD.csv', 'w', newline='') as file:
                mywriter = csv.writer(file, delimiter=',')
                mywriter.writerows(Matrice_densa)
            file.close()

            return count, err_final
        else:
            for i in range(z_righe):
                Matrice_densa[zero_pos[i][0]][zero_pos[i][1]] = abs(Matrice_densa_svd[zero_pos[i][0]][zero_pos[i][1]])
            err1 = err_final






