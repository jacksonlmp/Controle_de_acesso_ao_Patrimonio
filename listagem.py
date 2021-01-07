def acharNome(matricula):
    lista = []
    arq = open("professores.txt", "r")

    for linha in arq:
        linhas = linha.split("-")
        linhas.remove("\n")
        lista.append(linhas)

        for i in range(len(lista)):
            if lista[i][0] == matricula:
                return lista[i][1]
    arq.close()

def acharDescricao(patrimonio):
    try:
        lista = []
        arq = open("patrimonio.txt", "r")
        for linha in arq:
            linhas = linha.split("-")
            linhas.remove("\n")
            lista.append(linhas)
            for i in range(len(lista)):
                if lista[i][0] == patrimonio:
                    return lista[i][1]
        arq.close()
    except FileNotFoundError:
        print("⟨ Nenhum patrimonio cadastrado. ⟩")


def indisponiveis():
    try:
        lista = []
        arq = open("patrimonio.txt", "r")

        print("|| Patrimonios Indisponíveis ||".center(35))
        print("NUMERO ||  DESCRIÇÃO   ||  RESPONSÁVEL  || MATRICULA")

        for linha in arq:
            linhas = linha.split("-")
            linhas.remove("\n")
            lista.append(linhas)

            if linhas[2] == "indisponivel":
                try:
                    arquivo = open("acesso.txt", "r")

                    for linha2 in arquivo:
                        linhas2 = linha2.split("-")
                        linhas2.remove("\n")

                        if linhas2[2] == linhas[0]:
                            nome = acharNome(linhas2[0])
                            print("  ",linhas[0],"   -   ", linhas[1], "   -   ", nome, "   -   ", linhas2[0])

                except FileNotFoundError:
                    print("⟨ Nenhum patrimonio foi retirado e/ou devolvido. ⟩")

    except FileNotFoundError:
        print("⟨ Nenhum patrimonio cadastrado. ⟩")

def disponiveis():
    try:
        arq = open("patrimonio.txt", "r")

        print("|| Patrimonios Disponíveis ||".center(35))
        print("NUMERO ||  DESCRIÇÃO")

        for linha in arq:
            linhas = linha.split("-")
            linhas.remove("\n")

            if linhas[2] == "disponivel":
                print("  "+ linhas[0] + "   -   "+linhas[1])


    except FileNotFoundError:
        print("⟨ Nenhum patrimonio cadastrado. ⟩")

def saberTempodedevo(tempo, diaInserido):
    try:
        print(" MATRICULA  ||    NOME    || PATRIMONIO || DESCRIÇÃO ")
        dicto = {}
        lista = []
        arq = open("acesso.txt", "r")

        for linha in arq:
            linhas = linha.split("-")
            linhas.remove("\n")
            lista.append(linhas)

            if linhas[1] == "recebimento":
                valor = linhas[0]
                data_inicial = linhas[3]
                hora_inicial = linhas[4]
                data1 = data_inicial.split("/")
                hora1 = hora_inicial.split(":")

            if valor == linhas[0] and linhas[1] == "devolucao":
                data_final = linhas[3]
                hora_final = linhas[4]
                data2 = data_final.split("/")
                hora2 = hora_final.split(":")

                dias = int(data2[0]) - int(data1[0])
                meses = int(data2[1]) - int(data1[1])
                hora = int(hora2[0]) - int(hora1[0])
                minutos = (int(hora2[1]) - int(hora1[1]))+1

                if hora >= int(tempo) and dias <= diaInserido:
                    print("   "+valor+"   -   "+acharNome(valor)+"   -   "+linhas[2]+"   -   "+acharDescricao(linhas[2]))

    except FileNotFoundError:
        print("⟨ Nenhum patrimonio foi retirado e/ou devolvido. ⟩")

def naoPegar(numero, op):
    try:
        if op == "devolucao":
            arq = open("patrimonio.txt", "r")

            for linha in arq:
                linhas = linha.split("-")
                linhas.remove("\n")


                if linhas[0] == numero and linhas[2] == "disponivel":
                    return False
            return True
        elif op == "recebimento":
            arq = open("patrimonio.txt", "r")

            for linha in arq:
                linhas = linha.split("-")
                linhas.remove("\n")

                if linhas[0] == numero and linhas[2] == "indisponivel":
                    return False
            return True
    except FileNotFoundError:
        print("⟨ Nenhum patrimonio cadastrado. ⟩")
