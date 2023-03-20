import numpy as np
import pandas as pd
import csv
import matrice_sparsa
import regole_associative
import SVD
import datetime
import SGD
import GD

start_programma= datetime.datetime.now()

#Si manipola la struttura del dataset grezzo per ottenere il dataset su cui svolgere le analisi.

#si apre un file csv in scrittura
data = open("path/mp_gruppo01/dati.csv", mode="w")
#il dataset grezzo è salvato in files
files = ["combined_data_1.txt"]

#si applica la funzione per la costruzione e salvataggio in un file della matrice sparsa
matrice_sparsa.creazione_matrice(data, files, num_utenti=10000)
data.close()

#Caratteristiche dati
df = pd.read_csv("dati.csv", names=["movie_id", "user_id", "rating", "date"])
print("-------")
print("Caratteristiche dati:")
print(df.nunique())
print(df.head(5))

#E' creata la matrice sparsa su cui verrano eseguite le succesive analisi
R=[]
with open("matrice_R.csv", newline='') as f:
    reader = csv.reader(f)
    for i in reader:
        R.append(i)

R=np.asarray(R, dtype="float64")
R=R.T
righe,colonne=np.shape(R)


#E' applicato l'algoritmo discesa del gradiente
start=datetime.datetime.now()
count, errr= GD.algoritmo_GD(R, righe, colonne, alfa=0.00009, err_soglia=0.05)
end=datetime.datetime.now()
delta=end-start
print("-------")
print("risultati GD:")
print("tempo:", delta)
print("numero iterazioni", count)
print("errore finale", errr)


#E' applicato l'algoritmo discesa del gradiente stocastico
start=datetime.datetime.now()
count, errr= SGD.algoritmo_SGD(R, righe, colonne, alfa=0.00099, err_soglia=0.05)
end=datetime.datetime.now()
delta=end-start
print("-------")
print("risultati SGD:")
print("tempo:", delta)
print("numero iterazioni", count)
print("errore finale", errr)


#E' applicato l'algoritmo SVD
start=datetime.datetime.now()
Z = np.zeros((righe, colonne), dtype="float64")
count, err_final = SVD.SVD_troncata(R, righe, colonne, Z, err_soglia=0.05, fattori=5)
end=datetime.datetime.now()
delta=end-start
print("-------")
print("risultati SVD:")
print("tempo:", delta)
print("numero iterazioni", count)
print("errore finale", err_final)


#Sono calcolate le regole associative
print("-------")
print("risultati Regole Associative:")
start=datetime.datetime.now()
regole_associative.regole_associative(R, righe, colonne)
end=datetime.datetime.now()
delta=end-start
print("tempo:", delta)


end_programma= datetime.datetime.now()
delta_programma= end_programma-start_programma
print("-------")
print("tempo totale di esecusione programma:", delta_programma)


