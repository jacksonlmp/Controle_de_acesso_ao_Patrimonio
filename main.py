import re
import time
from datetime import date
from crypto import *
from listagem import *

def linhas():
    print('='*38)

linhas()
print('| CONTROLE DE ACESSO AO PATRIMÔNIO |')
linhas()

#========================================== VERIFICAR EXISTENCIA ========
def existenciaPatrimonio(numero):
    try:
        lista = []
        arq = open("patrimonio.txt", "r")

        for linha in arq:
            linhas = linha.split("-")
            linhas.remove("\n")
            lista.append(linhas)

        for i in range(len(lista)):
            arq.close()
            if lista[i][0] == numero:
                return True
        return False
        arq.close()
    except FileNotFoundError:
        return False

def comparaSenha(chave):
    try:
        lista = []
        arq = open("professores.txt", "r")

        for linha in arq:
            linhas = linha.split("-")
            linhas.remove("\n")
            lista.append(linhas)

        for i in range(len(lista)):
            arq.close()
            if lista[i][2] == chave:
                return True
        return False

        arq.close()
    except FileNotFoundError:
        return False

def existenciaUsuario(matricula):
    try:
        lista = []
        arq = open("professores.txt", "r")

        for linha in arq:
            linhas = linha.split("-")
            linhas.remove("\n")
            lista.append(linhas)

        for i in range(len(lista)):
            arq.close()
            if lista[i][0] == matricula:
                return True
        return False
    except FileNotFoundError:
        return False

#====================================== TEMPO ====
def dataEhora():
    tempo = time.localtime()
    data = ('{}/{}/{}-{}:{}'.format(tempo[2],tempo[1],tempo[0],tempo[3],tempo[4]))
    return(data)

#============================================= MENU PRINCIPAL ========
def menuPrincipal():
    linhas()
    print('|[1] para Cadastrar Patrimônio       |')
    print('|[2] para Cadastrar Professor        |')
    print('|[3] para Login                      |')
    print('|[4] para Patrimonios com X horas    |')
    print('|[5] para Patrimonios mais Utilizados|')
    print('|[6] Para Sair                       |')
    linhas()

    k = 0
    while k != 1: #enquanto nada for verdadeiro ele fica pedindo entradas
        op = input("► ")
        try:
            op2 = int(op)
            valores = [op2==1,op2==2,op2==3,op2==4,op2==5,op2==6] #lista com valores para comparacao
            if any(valores) == True:  #se algum dos valores for verdadeiro
                return op2
            else:
                print('⟨ Opção invalida, tente novamente. ⟩')
        except ValueError or UnboundLocalError:
            print('⟨ Opção invalida, tente novamente. ⟩')

#================================================== VALIDAR CARACTERES ====
def semEspecialLetras(caso):
    charRe = re.compile(r'[^a-zA-Z]')
    case = charRe.search(caso)
    return bool(case)

def semEspecialNum(caso):
    charRe = re.compile(r'[|\^&+\-%*/;=!>@#$?{~}´`<¨.,:)(]')
    case = charRe.search(caso)
    return bool(case)

#========================================== FUNCOES PARA VALIDAR ENTRADA ===
def semNumeros(saida):
    print (saida, end = " ")
    caso = input()

    while caso.isdigit() == True or semEspecialNum(caso) == True or caso == '[' or caso == ']': #for uma entrada de inteiros
            print('⟨ Opção invalida, tente novamente. Só é permitido letras. ⟩')
            return semNumeros(saida)
    return caso

def semLetras(saida):
    print (saida, end = " ") #nome do parametro dado para sempre alterar a variável
    caso = input()

    while caso.isdigit() != True or semEspecialLetras(caso) != True: #não for uma entrada de inteiros
        print('⟨ Opção invalida, tente novamente. Só é permitido numeros. ⟩')
        return semLetras(saida)
    return caso
#========================================= PATRIMONIO ======
def cadastroPatrimonio():
    print("¨CADASTRO DE PATRIMÔNIO¨")
    numero = semLetras("»Numero do Patrimônio:")
    patrimonio = existenciaPatrimonio(numero)

    if patrimonio == True:
        print('⟨ Patrimonio ja Registrado. ⟩')

    else:
        descricao = semNumeros("»Descrição do Patrimônio:")
        arquivo = open('patrimonio.txt', 'a')
        arquivo.write(numero + '-' + descricao+"-disponivel")
        arquivo.write('-\n')
        arquivo.close()
        linhas()
        print('Cadastro efetuado com sucesso.')
        linhas()

def alterarPatrimonio(numero, op):
    try:
        if op == "recebimento":

            lista = []

            arq = open("patrimonio.txt", "r")

            for linha in arq:
                linhas = linha.split("-")
                linhas.remove("\n")
                lista.append(linhas)

                for j in range(len(lista)):
                    if lista[j][0] == numero:
                        lista[j][2] = "indisponivel"

            arq.close()

            arq = open("patrimonio.txt", "w")

            for k in range(len(lista)):
                for l in lista[k]:
                    arq.write(l)
                    arq.write("-")
                arq.write("\n")

            arq.close()

        elif op == "devolucao":

            lista = []

            arq = open("patrimonio.txt", "r")

            for linha2 in arq:
                linhas2 = linha2.split("-")
                linhas2.remove("\n")
                lista.append(linhas2)

                for i in range(len(lista)):
                    if lista[i][0] == numero:
                        lista[i][2] = "disponivel"

            arquivo = open("patrimonio.txt", "w")

            for m in range(len(lista)):
                for p in lista[m]:
                    arquivo.write(p)
                    arquivo.write("-")
                arquivo.write("\n")

            arquivo.close()

    except FileNotFoundError:
        print("⟨ Nenhum patrimonio cadastrado. ⟩")

#===========================================PROFESSOR ======
def cadastroProfessor():
    print("¨CADASTRO DE PROFESSOR¨")
    arquivo = open('professores.txt','a')
    matricula = semLetras("»Numero da Matricula:")
    existe = existenciaUsuario(matricula)

    if existe == False:
        nome = semNumeros("»Nome do Professor:")
        chave = input('»Chave de acesso: ')
        while len(chave) == 0 or chave.isspace() == True or len(chave) < 3:
            print('⟨ Forma de chave invalida ou insuficiente, tente novamente. ⟩')
            chave = input('»Chave de acesso: ')

        chave = chaveCrypto(chave)

        arquivo.write(matricula + '-'+nome+"-"+chave)
        arquivo.write('-\n')
        arquivo.close()
        linhas()
        print('Cadastro efetuado com sucesso!')
        linhas()
    else:
        print("⟨ Matricula ja existe. ⟩")

#==================================Dias PATRIMONIO
def diasPatrimonio():
    dias = semLetras('»Dias:')
    dias = int(dias)
    try:
        arq = open('acesso.txt','r')
        lista = []
        for linha in arq:
            linhas = linha.split("-")
            linhas.remove("\n")
            lista.append(linhas)

        data = linhas[3]
        data2 = data.split('/')
        dataAtual = date.today()
        dale = dataAtual.strftime("%d/%m/%Y").split('/')

        diferenca = int(dale[0]) - dias

        return abs(diferenca)

    except FileNotFoundError:
        print("⟨ Nenhum patrimonio retirado. ⟩")

def contains(subseq, inseq): #contador para saber se tem o patrimonio na lista
    if len(inseq)>0:
        for i in range(len(inseq)):
            if subseq == inseq[i][2]:
                return True
        return False
    else:
        return False

def modify(subseq,inseq):  #modificar o contador já que o patrimonio já existe acrescentando +1
    if len(inseq)>0:
        for i in range(len(inseq)):
            if subseq == inseq[i][2]:
                inseq[i][5] = int(inseq[i][5])+1

def comparaDiasPatrimonio():
    try:
        arq = open('acesso.txt','r')
        lista = []

        for linha in arq:
            linhas = linha.split('-')
            linhas.remove('\n')
            lista.append(linhas)

        diasDiferenca = diasPatrimonio()

        print(' MATRICULA ||    NOME    || PATRIMONIO || DESCRIÇÃO || VEZES PEGO ')
        listacnt=[]
        for i in range(len(lista)):
            tempo = lista[i][3].split('/')[0] # pegando o dia
            if not contains(lista[i][2],listacnt) and lista[i][1] == "recebimento":
                if int(tempo) >= diasDiferenca:
                    listacnt.append(lista[i])
            elif lista[i][1] == "recebimento":
                modify(lista[i][2],listacnt)

        for j in range(len(listacnt)):
            nome = acharNome(listacnt[j][0])
            descricao = acharDescricao(listacnt[j][2])
            print("  "+listacnt[j][0] +"      -   "+nome+"      -     "+ listacnt[j][2] +"      -      "+ descricao+ '      -     '+ str(listacnt[j][5]))

    except FileNotFoundError:
        print("⟨ Nenhum patrimonio retirado. ⟩")


#=================================== ACESSO====

def acesso():
    print("¨ACESSO¨")
    matricula = semLetras("»Numero da Matricula:")
    existe = existenciaUsuario(matricula)

    if existe == True:
        k = 0
        cont = 0
        chave = input('»Chave de Acesso: ')
        chave = chaveCrypto(chave)
        existeChave = comparaSenha(chave)
        while existeChave != True:
            print('⟨ Chave de acesso invalida, tente novamente. ⟩')
            chave = input('»Chave de Acesso: ')
            chave = chaveCrypto(chave)
            existeChave = comparaSenha(chave)

        while k != 10:
            opcao = input("[1]Devolução de Patrimônio\n[2]Recebimento de Patrimônio\n[3]Lista de Patrimonios Disponíveis\n[4]Lista de patrimonios Indisponíveis\n[5]Sair\n► ")
            try:
                opcao = int(opcao)
                if opcao == 1:
                    op = "devolucao"
                    tempo = dataEhora()
                    k = 10

                elif opcao == 2:
                    op = "recebimento"
                    tempo = dataEhora()
                    k = 10

                elif opcao == 3:
                    linhas()
                    disponiveis()
                    linhas()

                elif opcao == 4:
                    linhas()
                    indisponiveis()
                    linhas()

                elif opcao == 5:
                    return opcao
                else:
                    print('⟨ Opção invalida, tente novamente. ⟩')
            except ValueError or UnboundLocalError:
                    print('⟨ Opção invalida, tente novamente. ⟩')

        patrimonio = semLetras("»Numero do Patrimônio:")
        existePatrimonio = existenciaPatrimonio(patrimonio)

        if existePatrimonio == True:
            podePegar = naoPegar(patrimonio, op)

            if podePegar == True:

                alterarPatrimonio(patrimonio, op)

                arq = open("acesso.txt", "a")
                arq.write(matricula+"-"+op+"-"+patrimonio+"-"+tempo+"-"+'1')
                arq.write("-\n")
                arq.close()

                linhas()
                print("Acesso Realizado com sucesso!")
                linhas()

            else:
                print("⟨ Não foi possivel realizar a operação. ⟩")
        else:
            print("⟨ Patrimonio não existe. ⟩")

    else:
        print("⟨ Matricula não existe. ⟩")


#======================================Opçoes do MENU
opcao = menuPrincipal()

while opcao != 6:
    if opcao == 1:
        cadastroPatrimonio()
        opcao =  menuPrincipal()

    elif opcao == 2:
        cadastroProfessor()
        opcao = menuPrincipal()

    elif opcao == 3:
        acesso()
        opcao = menuPrincipal()
    elif opcao == 4:
        print("⊰Listagem dos professores que ficaram com o patrimônio")
        print("por mais de X horas nos últimos Y dias.⊱".center(55))
        horas = semLetras("»Horas:")
        dias = diasPatrimonio()
        saberTempodedevo(horas, dias)
        opcao = menuPrincipal()
    elif opcao == 5:
        print("⊰Listagem dos patrimônios mais utilizados nos últimos Y dias.⊱")
        comparaDiasPatrimonio()
        opcao = menuPrincipal()


print("-"*38)
print('Obrigado, volte sempre!'.center(35))
print("-"*38)
