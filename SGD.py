import numpy as np
import csv
import Inizializzazione_per_Gradiente as In

def algoritmo_SGD(matrice, righe, colonne, alfa, err_soglia):

    # inizializzazione dati per algoritmo
    S, righe1, rows, cols, U, V, errr1 = In.inizializzazione_Gradiente(5, matrice, righe, colonne)

    count=0
    convergence = False
    #Algoritmo SGD
    while (convergence == False):
        count = count + 1
        np.random.shuffle(S)  #shuffle delle righe della matrice S

        # Applichiamo le regole di aggiornamento e ridefiniamo le matrici U e V
        for i in range(0, righe1):
            #calcolo dei residui
            e = matrice[S[i][0]][S[i][1]] - np.dot(U[S[i][0], :], V[S[i][1], :].T)

            Uplus = U[S[i][0], :] + alfa * (e * V[S[i][1], :])
            Vplus = V[S[i][1], :] + alfa * (e * U[S[i][0], :])


            U[S[i][0], :] = Uplus
            V[S[i][1], :] = Vplus

        # si stima la matrice tramite prodotto matriciale e si calcola l'errore
        D = np.dot(U, V.T)
        errr = 0.5 * sum((matrice[rows,cols] - D[rows,cols])**2)

        # si verifica la condizione di convergenza
        if abs(errr - errr1) < err_soglia:
            convergence = True
            # salvataggio risultati
            with open('risultati_SGD.csv', 'w', newline='') as file:
                mywriter = csv.writer(file, delimiter=',')
                mywriter.writerows(D)
            file.close()

            return count, errr
        else:
            errr1 = errr





