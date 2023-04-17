import pandas as pd
from auxMod import *
from tabulate import *
import pickle
'''
Programa Principal
'''
ação = 0

baseDadosClientes = []
baseDadosFaturas = {}

while ação != 8:

    '''
    Menu de escolha
    '''
    print("================================================================================")
    print("Seja bem vindo ao sistema de gestão de clintes para compania de aguas do grupo:")
    print("================================================================================")
    print("Faturação do consumo de agua")
    print("================================================================================")
    print("Escolha uma das opções abaixo:")
    print("================================================================================")
    print("1 - Carregar informação anterior.")
    print("2 - Registrar um novo cliente.")
    print("3 - Alterar o registro de clientes.")
    print("4 - Consultar registros anteriores.")
    print("5 - Gestão de Faturação.")
    print("6 - Obter resgistros anteriores.")
    print("7 - Gravar informação das bases de dados")
    print("8 - Fechar o programa.")
    print("================================================================================")
    try:
        ação = int(input("Escolha uma opção acima."))
    except ValueError:
        print("O valor introduzido é invalido tente novamente!")

    if ação == 1:
       
        inFileClientes = "BaseDadosClientes.pickle"
       
        
       
        inFileFaturas = "BaseDadosFaturas.pickle"
       
        try:
            with open(inFileClientes,"rb") as clienteBase:
                baseDadosClientes = pickle.load(clienteBase)
        except FileNotFoundError:
            print("Ainda não há uma base registrada.") 
        try:
            with open(inFileFaturas,"rb") as faturaBase:
                baseDadosFaturas = pickle.load(faturaBase)
        except FileNotFoundError:
            print("Ainda não há uma base registrada.")

    elif ação == 2:
        #Introduz um novo cliente
        print("===========================================================================")
        print("Introduza as informações referentes ao cliente:")
        try:
            nome = str(input("Escreva o nome do cliente:"))
        except ValueError:
            nome = str(input("Valor invalido tente novamente, escolha um valor valido:"))
        try:
            Nif = int(input("Escreva o NIF do cliente:"))
        except ValueError:
            Nif = int(input("Valor invalido tente novamente, escolha um valor valido:"))

        try:
            morada = str(input("Escreva a morada do cliente:"))
        except ValueError:
            morada = str(input("Valor invalido tente novamente, escolha um valor valido:"))
        try:
            telemovel = int(input("Escreva o telemovel do cliente:"))
        except ValueError:
            telemovel = int(input("Valor invalido tente novamente, escolha um valor valido:"))
        try:
            conta = int(input("Escreva a conta do cliente:"))
        except ValueError:
            conta = int(input("Valor invalido tente novamente, escolha um valor valido:"))
        clienteInfo = NewClient(nome, Nif, morada, telemovel, conta)
        print("============================================================================")
        print(f"Foi adicionado a base de dados o respectivo cliente:{clienteInfo}")
        baseDadosClientes.append(clienteInfo)

    elif ação == 3:
        print("============================================================================")
        clienteKey3 = int(input("Escreva o numero de conta do cliente para localizar o registro do cliente que deseja fazer alterações a sua info:"))
        contaCheck3 = checaContaExiste(clienteKey3,baseDadosClientes)
        if contaCheck3 == False:
            print("A conta introduzida não consta na base de dados, tente novamente.")
        elif contaCheck3 == True:
            TargetCliente = checkIfElementInListofLists(clienteKey3,baseDadosClientes)
            for i in baseDadosClientes:
                TargetIndex3 = baseDadosClientes.index(i)
            print(TargetCliente)
            print(f"Escolha a ação que deseja fazer na informação do cliente escolhido:{TargetCliente}")
            ação2 = input("Deseja deletar ou alterar o registro?")
            
            if ação2.casefold() == "alterar":
                print("Menu de Alteração de Registros")
                print("================================")
                print("Nome.")
                print("NIF.")
                print("Morada.")
                print("Telemovel.")
                print("Conta.")
                print("Fatura.")
                print("================================")
                TargetData = input("Qual a informação que deseja alterar?")
                NewData = input("Digite a nova informação a ser adicionada:")
                TargetCliente = AlterarInfo(TargetData,TargetCliente,NewData)
                print(baseDadosClientes)
                print(TargetCliente)
                print(clienteKey3)

            elif ação2.casefold() == "deletar":
                print(f"O registro:{TargetCliente} foi retirado da Base.")
                baseDadosClientes.pop(TargetIndex3)
        print("===============================================================================")

    elif ação == 4:
        print("===============================================================================")
        TargetInfo4 = int(input("Escreva o numero de conta do cliente para localizar o seu registro:"))
        contaCheck4 = checaContaExiste(TargetInfo4,baseDadosClientes)
        TargetCliente4 = checkIfElementInListofLists(TargetInfo4,baseDadosClientes)
        for i in baseDadosClientes:
            TargetIndex4 = baseDadosClientes.index(i)
        if contaCheck4 == False:
            print("O numero da conta ou Nif introduzido não corresponde a nenhum dos clientes na base.")
        elif contaCheck4 == True:
            print(f"O cliente com Nif:{TargetCliente4[nifCliente]} e numero de conta:{TargetCliente4[contaCliente]} possui o seguinte registro:{TargetCliente4}")
        print("===============================================================================")

    elif ação == 5:
        print("===============================================================================")
        print("Sistema de Gestão de Faturação:")
        print("==============================================================================")
        passe = input("Digite [T] para acessar as faturas de todos os cliente [C] para um cliente especifico:")
        if passe.casefold() == "t":
                print("=============================================================================")
                print("Faturas de Todos os Clientes")
                print("=============================================================================")
                print("Nº Clientes", "Mes", "Consumo(m^3)", "Calibre(mm)","Tarifa Social","Total(Euros)")
                dataFrame = pd.DataFrame.from_dict(baseDadosFaturas, orient = "index")
                print(dataFrame)
                print("=============================================================================")
        elif passe.casefold() == "c":
            clienteKey = int(input("Introduza a conta do cliente que deseja adicionar ou verificar a fatura :"))
            print("==============================================================================")
            contaCheck = checaContaExiste(clienteKey,baseDadosClientes)
            if contaCheck == False:
                print("A conta introduzida não consta na base de dados, tente novamente.")
            elif contaCheck == True:
                print("===============================================================================")
                print("Menu de Gestão de faturas:")
                print("===============================================================================")
                print("1 - Adicionar uma nova fatura a um cliente:")
                print("2 - Remover ou alterar uma fatura de um cliente:")
                print("3 - Consultar faturas de um cliente especifico:")
                try:
                    ação4 = int(input("Escolha uma opção acima:"))
                except ValueError:
                    print("O valor escolhido não é valido tente novamente.")
                if ação4 == 1:
                    print("Introduza as informações referentes ao calculo da fatura:")
                    mes = input("Introduza o mes referente a fatura seguindo a seguinte ordem:")
                    consumo = int(input("Introduza a quantia consumida de agua.(m^3):"))
                    calibre = int(input("Introduza o calibre:(mm)"))
                    tarifaSocial = input("Possui Tarifa-Social?")
                    if tarifaSocial.casefold() == "sim":
                        total = f"R${calculoVarTarifaSocial(consumo)}"
                    elif tarifaSocial.casefold() == "nao" or "não":
                        total = calculoVarSemTarifaSocial(consumo) + calculoTarifaFixa(calibre)
                    FaturaInfo = [mes,consumo,calibre,tarifaSocial,total]
                    print(f"A fatura do cliente de numero:{clienteKey} foi criada:{FaturaInfo}")
                    addInfoFaturasBase(baseDadosFaturas,FaturaInfo,clienteKey)
                    print(f"Seu historico de faturas é:{baseDadosFaturas.get(clienteKey)}")
                    print(baseDadosFaturas)

                elif ação4 == 2:
                    FaturaKey = input("Introduza o mes da fatura desejada.")
                #for fatura in baseDadosFaturas.get(clienteKey):
                    TargetFatura = checkIfElementInListofLists(FaturaKey,baseDadosFaturas.get(clienteKey))
                    FaturaIndx = baseDadosFaturas.get(clienteKey).index(TargetFatura)
                    if TargetFatura == []:
                        print("Ainda não há faturas desse mes atribuida ao cliente.")
                    elif TargetFatura != []:
                        açãoInterna = input("Deseja alterar ou deletar uma fatura?.")

                    if açãoInterna.casefold() == "alterar":
                        print("Menu de Alteração de Informação das faturas:")
                        print("========================================================================")
                        print("Mes:")
                        print("Consumo:")
                        print("Calibre")
                        print("Tarifa Social:")
                        print("Total:")
                        print("=========================================================================")
                        TargetData4 = input("Qual Informação deseja alterar?")
                        NewData4 = input("Digite a nova informação a ser adicionada:")
                        TargetFatura = AlteraDadosFatura(TargetData4,TargetFatura, NewData4)
                        print("=========================================================================")
                        print(f"A fatura foi alterada para:{TargetFatura}")
                        print("=========================================================================")
                
                    elif açãoInterna.casefold() == "deletar":
                        print("=========================================================================")
                        print(f"A Fatura:{TargetFatura} foi deletada.")
                        print("=========================================================================")
                        baseDadosFaturas.get(clienteKey).pop(FaturaIndx)
                        print(f"Faturas Cliente:{clienteKey}")
                        print(baseDadosFaturas.get(clienteKey))
                        print("=========================================================================")
            
                elif ação4 == 3:
                    print("=============================================================================")
                    print(f"As Faturas do Cliente:{clienteKey} são:")
                    print("=============================================================================")
                    colunas = ["Mes","Consumo(m^3)","Calibre(mm)","Tarifa Social","Total(Euros)"]
                    df1 = pd.DataFrame(baseDadosFaturas.get(clienteKey))
                    df1.columns = ["Mes","Consumo(m^3)","Calibre(mm)","Tarifa Social","Total"]
                    print(df1)
                    print("=============================================================================")

           


    elif ação == 6:
        print("===============================================================================")
        print("Tabela de registros:") 
        print("Nome","--","Nif","--","Morada","--","Telemovel","--","Conta")
        for i in baseDadosClientes:
            print(i)
        print("===============================================================================")

    elif ação == 7:
        outFileClientes = "BaseDadosClientes.pickle"
        outFileFaturas = "BaseDadosFaturas.pickle"

        with open(outFileClientes, 'wb') as clientesOutBase:
            pickle.dump(baseDadosClientes, clientesOutBase, protocol=pickle.HIGHEST_PROTOCOL)

        with open(outFileFaturas, 'wb') as faturasOutBase:
            pickle.dump(baseDadosFaturas, faturasOutBase, protocol=pickle.HIGHEST_PROTOCOL)


