import apyori

def regole_associative(matrice, righe, colonne):
    records = []
    for i in range(0, righe):
        records.append([str(matrice[i][j]) for j in range(0, colonne)])

    association_rules = apyori.apriori(records, min_suppport=0.8, min_confidence=0.8, min_lift=1, min_length=2)
    association_results = list(association_rules)

    # numero di regole associative definite
    print(len(association_results))

    # stampiamo la prima regola associativa
    print(association_results[0])

    # sistemiamo la visualizzazione
    for item in association_results:
        print(item[0], '-->', item[2][0][1], 'support: ', item[1], 'confidence: ', item[2][0][2],
              'lift: ', item[2][0][3])


