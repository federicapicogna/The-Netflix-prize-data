Il contenuto della cartella viene descritto nel presente file di testo.

Si ricorda di inserire nella cartella seguente, scaricata, il file combined_data_1.txt che può reperire nel seguente link nella cartella mp_gruppo01, per il corretto funzionamento del programma:
https://drive.google.com/drive/folders/1FhpFI3rC8pM5BIB44rFVn8vUdrXslNJx?usp=sharing

- combined_data_1.txt

	Il file contiene il dataset "Netflix Prize data"


- creazione_dataset.py

	Il modulo contiene la funzione manipolazione_dataset, la quale prende
	in entrata un file .csv aperto in modalità scrittura, e il dataset di 
	interesse in formato .txt. Questa funzione sovrascrive il file .csv 
	dato in input, inserendo al suo interno i dati di interesse riscritti
	in un modo più agevole per l'applicazione di analisi successive.

	Il presente modulo è pensato per essere importato da un modulo che verrà
	presentato di seguito.


- campione_per_idUtente.py

	Il modulo contiene la funzione campionamento, che prende in ingresso il 
	file .csv correttamente definito dalla funzione 
	creazione_dataset.manipolazione_dataset, il file contenente i dati originali
	.txt e il numero di utenti che si desidera campionare. Lo scopo di tale
	funzione è quello di campionare dal dataset originale, in modo casuale, un
	numero prefissato di users e creare un file .csv che raccolga i dati degli
	utenti campionati.

	Il modulo appena descritto è pensato per essere a sua volta importato
	dal modulo riportato di seguito.


- matrice_sparsa.py

	Il modulo contiene la funzione creazione_matrice, che prende in input
	il file .csv precedentemente manipolato, il dataset di interesse in 
	formato .txt e il numero di utenti che si desidera campionare. Attraverso
	questa funzione viene creata una matrice sparsa che presenta un numero
	di colonne pari al numero di utenti campionati e un numero di righe pari
	al numero di oggetti recensiti; all'interno della matrice vengono inseriti
	i voti rilasciati dagli utenti in corrispondenza degli oggetti considerati.
	Nel caso piuttosto comune in cui un utente non abbia recensito un
	particolare film, la componente r_ij viene posta a zero.

	Questo modulo è pensato per essere importato da un modulo principale.


- Inizializzazione_per_Gradiente.py

	Il presente modulo contiene la funzione inizializzazione_Gradiente, la
	quale prende in ingresso il numero di fattori desiderato, la matrice dei
	rating, il numero di righe e colonne di tale matrice. 
	
	Questo modulo è pensato per essere importato dal seguente modulo, e ha
	lo scopo di inizializzare costrutti utili per i due seguenti algoritmi che 
	verranno descritti.


 -GD.py, SGD.py

	Tali moduli includono la funzione algoritmo_GD, e algoritmo_SGD, le quali
	richiedono in input la matrice dei rating da analizzare, il suo numero 
	di righe e colonne, il learning rate (tasso di apprendimento dell'algoritmo) 
	e l'errore soglia (differenza tra valore della funzione di minimo J 
	al passo precedente e corrente) che si desidera usare. 
	Queste funzioni applicano la decomposizione UV 	tramite l'algoritmo della
	 Discesa del Gradiente e della Discesa del Gradiente Stocastico.
	Entrambi i moduli hanno struttura analoga, si differenziano solo per l'uso
	di una matrice di errori nel primo caso, di una sola componente di errore
	nel secondo caso.
	I parametri considerati sia in Inizializzazione_per_Gradiente.py sia
	in GD.py e SGD.py comprendono:
	R:		Matrice di rating (creata tramite matrice_sparsa.py)
	fattori:	Numero di fattori latenti
	alfa:		Learning rate dell'algoritmo
	U,V:		Matrici inizializzate con soli valori uno
	S:		Matrice contenente le posizioni dei valori diversi da zero
			presenti in R
	righe1:		numero di righe di S
	rows,cols:	Prima e seconda colonna di S
	D1:		matrice risultante del prodotto matriciale UV^T
	e:		componente di errore (algoritmo_SGD)
	E:		matrice degli errori (algoritmo_GD)
	errr1:		Valore iniziale della funzione di minimo J
	err_final:	valore di J calcolato a ogni iterazione dell'algoritmo
	
	I moduli sono pensati per essere richiamati da un modulo principale.

- Inizializzazione_matrice_SVD.py

	Il modulo racchiude la funzione inizializzazione_matrice, che riceve
	in entrata la matrice dei rating da analizzare, il suo numero di righe
	e colonne, una matrice di zeri di dimensioni pari a quelle fornite alla
	funzione. Questa funzione permette di calcolare le medie per riga della
	matrice dei rating e popola correttamente la matrice di zeri fornita in
	entrata.

	Questo modulo è pensato per essere importato dal seguente modulo.

- SVD.py

	Il presente modulo contiene la funzione SVD_troncata, che prende in input
	la matrice dei rating, il suo numero di righe e colonne, la matrice di zeri
	che verrà poi trasformata in matrice densa richiamando la funzione 
	sopra descritta, l'errore soglia desiderato e il numero di fattori latenti 
	che si preferisce utilizzare. Questa funzione applica la decomposizione
	SVD della matrice dei rating. 
	I parametri considerati sia in Inizializzazione_matrice_SVD.py che in SVD.py
	sono:
	R:		Matrice dei rating
	fattori:	Numero di fattori latenti
	zero_pos:	matrice contenente le posizioni dei valori pari a 0 presenti
			in R
	rows,cols:	Prima e seconda colonna di zero_pos
	Matrice_densa:	Matrice popolata o dai rating osservati presenti nella
			matrice dei rating o dalla sua media di riga
	U,d,V^T:	matrici derivanti dalla decomposizione SVD calcolata 
			rispetto alla Matrice_densa attraverso l'apposita funzione 
			randomized_svd della libreria sklearn
	errr1:		Valore iniziale della funzione di minimo J, posto a zero
	err_final:	valore di J calcolato a ogni iterazione dell'algoritmo

	I moduli sono pensati per essere richiamati da un modulo principale.


- regole_associative.py

	Il modulo include l'omonima funzione regole_associative, che riceve in
	ingresso la matrice dei rating, il suo numero di righe e colonne, e stampa
	le regole associative trovate entro la matrice, il loro supporto, il livello
	di confidence e lift.
	Nel presente modulo, in corrispondenza della riga 8 è possibile modificare:
	1. le misure della lift sostituendo al valore assegnato in "min_lift=1" 
	il valore voluto ;
	2. della confidence sostituendo al valore assegnato in 
	"min_confidence=0.8" il valore voluto;
	3. del supporto sostituendo al valore assegnato in "min_support=0.8" il 
	valore voluto;
	4. il minimo valore di item che si vogliono in una regola sostituendo al 
	valore assegnato in "min_length=2" il valore voluto. 

	Il modulo è pensato per essere richiamato da un modulo principale.

- main.py
	
	Modulo principale nel quale vengono importati i moduli precedentemente
	elencati e descritti. Si consiglia di eseguire questo modulo da terminale,
	in modo da poter visualizzare una prima versione dei dati di interesse,
	i tempi di esecuzione di ogni modulo inserito, 
	il numero di iterazioni necessarie per la convergenza degli algoritmi
	di GD,SGD e SVD e il valore della funzione di minimo J ottenuta nello step
	finale, il numero di regole associative trovate e le regole associative
	vere e proprie. Per il corretto funzionamento di questo modulo è necessario
	modificare la riga 15, sostituendo a “path” la dicitura 
	"path/mp_gruppo01/dati.csv", ovvero il percorso per raggiungere la cartella
	mp_gruppo01, in modo che il file formato .csv venga creato nel modo giusto.
 	E’ possibile sostituire:
	1.nella riga 19 il numero di utenti che si vogliono campionare sostituendo 
	al valore assegnato in "num_utenti=10000" quello voluto;
	2. nelle righe 44 e 56 i valori relativi al learning rate e all'errore di
	 convergenza;
	3. nella riga 69 il valore dell'errore di convergenza e al numero di
	fattori che si vogliono identificare.

	Per eseguire correttamente il programma è necessario estrarre tutti i file 
	nella stessa cartella che è stata scaricata (è necessario scaricare mp_gruppo01 per intera).
	Da terminale è necessario posizionarsi nella cartella mp_gruppo01 ed 
	eseguire il programma inviando il main tramite l’istruzione 'python main.py', 
	dopo aver effettuato le sostituzioni necessarie per il corretto 
	funzionamento. 
	

	I risultati, ottenuti con un campione casuale di 10000 utenti e
	commentati nella relazione finale, sono reperibili nella cartella 
	risultati_mp_gruppo01.
	






