import numpy as np
import Inizializzazione_per_Gradiente as In
import csv

def algoritmo_GD(matrice, righe, colonne, alfa, err_soglia):

    #inizializzazione dati per algoritmo
    S, righe1, rows, cols, U, V, errr1 = In.inizializzazione_Gradiente(5, matrice, righe, colonne)

    count=0
    E = np.zeros((righe, colonne))
    convergence=False

    #algoritmo GD
    while(convergence==False):
        count = count + 1

        E[rows, cols] = matrice[rows, cols] - np.dot(U, V.T)[rows, cols]

        Uplus = U+alfa*np.dot(E,V)
        Vplus = V+alfa*np.dot(E.T,U)

        U = Uplus
        V = Vplus

        D = np.dot(U, V.T)

        errr = 0.5*sum((matrice[rows,cols] - D[rows,cols])**2)

        if abs(errr - errr1) < err_soglia:
            convergence = True

            # salvataggio risultati
            with open('risultati_GD.csv', 'w', newline='') as file:
                mywriter = csv.writer(file, delimiter=',')
                mywriter.writerows(D)
            file.close()

            return count, errr
        else:
            errr1 = errr

