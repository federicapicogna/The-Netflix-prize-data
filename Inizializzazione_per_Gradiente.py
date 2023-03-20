import numpy as np

def inizializzazione_Gradiente(fattori, matrice, righe, colonne):

    k = fattori

    # definizione di S, matrice di riferimento per le posizioni dei valori osservati (diversi da zero) in "matrice"
    S = np.transpose(np.nonzero(matrice))
    righe1, colonne1 = np.shape(S)

    # salviamo i valori della prima colonna di S in rows e della seconda colonna di S in cols
    rows = S[:, 0]
    cols = S[:, 1]

    # inizializzazione delle matrici U e V con valori 1, di dimensione righe*k e colonne*k rispettivamente
    U = np.ones((righe, k))
    V = np.ones((colonne, k))

    # inizializzazione per la prima iterazione:

    # matrice definita tramite prodotto matriciale di U e V.T, inizializzate a 1
    D1 = np.dot(U, V.T)

    # errore tra matrice osservata e matrice stimata
    errr1 = 0.5 * sum((matrice[rows,cols] - D1[rows,cols])**2)

    return S, righe1, rows, cols, U, V, errr1
