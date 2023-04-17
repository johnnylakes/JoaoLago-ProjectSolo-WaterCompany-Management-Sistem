
#localização das info clientes:
nomeCliente = 0
nifCliente = 1
moradaCliente = 2
telemovelCliente = 3
contaCliente = 4


mesFatura = 0
consumoFatura = 1
calibreFatura = 2
tarifaSocialFatura = 3
totalFatura = 4








#Funções auxiliares:
def NewClient(nome,Nif,morada,telemovel,conta):
    newClient = [nome,Nif,morada,telemovel,conta]
    return newClient

def calculoVarSemTarifaSocial(consumo):

    if consumo <= 5:
        p = 0.7354

    elif 6 <= consumo <= 15:
        p = 1.0509

    elif 16 <= consumo <= 25:
        p = 2.0859
        
    else:
        p = 2.6059

    print(round(p * consumo,4))
    return round(p * consumo,4)

def calculoVarTarifaSocial(consumo):

    if consumo <= 15:
        p = 0.7354

    elif 16 <= consumo <= 25:
        p = 2.0845

    else:
        p = 2.6059

    print(round(p * consumo,4))
    return round(p * consumo,4)



def calculoTarifaFixa(calibre):

    if calibre <= 25:
         p = 4.8385

    elif  25 < calibre <= 30:
        p = 19.5959

    elif  30 < calibre <= 50:
        p = 41.1514

    elif 50 < calibre <= 100:
        p = 111.9318

    return p

def definirComTarifaEscalão(consumo):
    if consumo <= 15:
        escalao = 1

    elif 16 <= consumo <= 25:
        escalao = 2

    else:
        escalao = 3

    return escalao

def definirSemTarifaEscalão(consumo):

    if consumo <= 5:
        escalao = 1

    elif 6 <= consumo <= 15:
        escalao = 2

    elif 16 <= consumo <= 25:
        escalao = 3
    else:

        escalao = 4
    return escalao
    
    

def checkIfElementInList(lista,elemento):

    if elemento in lista:
        #print(lista)
        return lista
    elif elemento in lista:
        return  []
    

        
    
def AlterarInfo(info,Cliente,newInfo):
    if info.casefold() == "nome":
        infoIndx = 0

    elif info.casefold() == "nif":
        infoIndx = 1

    elif info.casefold() == "morada":
        infoIndx = 2

    elif info.casefold() == "telemovel":
        infoIndx = 3
    
    elif info.casefold() == "conta":
        infoIndx = 4
    
    elif info.casefold() == "fatura":
        infoIndx = 5

    Cliente[infoIndx] = newInfo

    #print(Cliente)
    return Cliente


def checaContaExiste(conta,baseDados):
    check = True
    for contas in baseDados:
        if conta in contas:
            check = True
            #print(check)
            return check
            
        else:
            check = False
    #print(check)
    return check
    

def AlteraDadosFatura(info,FaturaCliente,NewData):
    if info.casefold() == "mes":
        infoIndx = 0
        FaturaCliente[infoIndx] = NewData

    elif info.casefold() == "consumo":
        infoIndx = 1
        FaturaCliente[infoIndx] = NewData

    elif info.casefold() == "calibre":
        infoIndx = 2
        FaturaCliente[infoIndx] = NewData

    elif info.casefold() == "tarifa social":
        infoIndx = 3
        FaturaCliente[infoIndx] = NewData

    elif info.casefold() == "total":
        infoIndx = 4
        FaturaCliente[infoIndx] = NewData

    return FaturaCliente



def ListaDisplayAllFaturas(dic):
    list = dic.items()
    for i in list:
        for j in i:
            print(j)


def addInfoFaturasBase(baseDados,fatura,ClientKey):
    if baseDados.get(ClientKey) == None:
        baseDados[ClientKey] = []
        return baseDados.get(ClientKey).append(fatura)
    else:
        return baseDados.get(ClientKey).append(fatura)


def checkIfElementInListofLists(key,ListofLists):
    for List in ListofLists:
        if key in List:
            return List
        
    return []




