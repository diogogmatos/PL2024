
def main():
    file = open("emd.csv")
    modalidades = []
    nr_aptos = 0
    nr_nao_aptos = 0
    # 0-4, 5-9, 10-14, 15-19, 20-24, 25-29, 30-34, 35-39, 40-44, 45-49, 50-54, 55-59, 60-64, 65-69, 70-74, 75-79, 80-84, 85-89, 90-94, 95-99
    escaloes = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    # _id,index,dataEMD,nome/primeiro,nome/último,idade,género,morada,modalidade,clube,email,federado,resultado
    i = 0
    for line in file:
        if i != 0:
            values = line.split(",")

            modalidades.append(values[8])

            idade = int(values[5])
            index = idade // 5
            escaloes[index] += 1
            
            if values[12].__contains__("true"):
                nr_aptos += 1
            else:
                nr_nao_aptos += 1
        i += 1

    unique_modalidades = list(set(modalidades))
    unique_modalidades.sort()

    print("Modalidades:")
    for modalidade in unique_modalidades:
        print("\t" + modalidade)
    print("\nAtletas Aptos: " + str(round((nr_aptos/(nr_aptos+nr_nao_aptos))*100, 2)) + "%")
    print("Atletas Inaptos: " + str(round((nr_nao_aptos/(nr_aptos+nr_nao_aptos))*100, 2)) + "%")
    print("\nEscalões Etários:")
    for i in range(len(escaloes)):
        if escaloes[i] != 0:
            print("\t" + str(i*5) + "-" + str(i*5+4) + ": " + str(escaloes[i]) + f" ({round((escaloes[i]/sum(escaloes))*100, 2)}%)")

main()
