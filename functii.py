import numpy as np
def determinareMatrice(lista,cardinal):
    M=np.zeros((cardinal,cardinal))
    M=M.astype(int)
    for elem in lista:
        a=elem[0]
        b=elem[1]
        #condurache gabriel
        M[a-1][b-1]=1
    return M

def Citire_Matrice():
    l=int(input("cate linii:"))
    c=int(input("cate coloane:"))

    matrix=[]

    for i in range(l):
        a=[]
        for j in range(c):
            a.append(int(input))
        matrix.append(a)
    
    return matrix

def Afisare_matrice(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(M[i][j], end = ' ')
        print()

def reflexiva(M):
    if len(M)==len(M[0]):
        for i in range(len(M)):
            if M[i][i]==0:
                print("nu este reflexiva")
                return 0
        print("este reflexiva")
    else:
        print("nu se poate stabili")
        return -1
    return 1

def antireflexiva(M):
    if len(M)==len(M[0]):
        for i in range(len(M)):
            if M[i][i]==1:
                print("nu este antireflexiva")
                return 0
        print(" este antireflexiva")
    else:
        print("nu se poate stabili")
        return -1
    return 1

def antisimetrica(M):
    if len(M)==len(M[0]):
        ok=0
        for i in range(len(M)):
            if M[i][i]==1:
                ok=1
    else:
        print("nu se poate stabili")
        return -1
    if ok:
        print("este antisimetrica")
        return 1
    else:
        print("nu este antisimetrica")
        return 0

def simetrica(M):
    if len(M)==len(M[0]):
        for i in range(len(M)):
            for j in range(i+1,len(M)):
                if M[i][j]!=M[j][i]:
                    print("nu este simetrica")
                    return 0
        print("este simetrica")
        return 1
    else:
        print("nu se poate stabili")
        return -1

def tranzitivitate(M):
    ok=0
    lista_tranzitivitate=[]
    if len(M)==len(M[0]):
        for i in range (len(M)):
            for j in range(len(M[0])):
                if M[i][j]==1:
                    for k in range (len(M[0])):
                        if M[j][k]==1:
                                if M[i][k]==1:
                                    ok=1
                                    if (i+1,k+1) not in lista_tranzitivitate:
                                        lista_tranzitivitate.append((i+1,k+1))
    else :
        print("nu se poate stabili")
        return -1
    if ok==1:
        print("este tranzitiva")
      #  print(lista_tranzitivitate)
        return 1
    else:
        print("nu este tranzitiva")
        return 0
    
def proprietate(x,y)->bool:
    return (x-y)%3

def determinare_relatie(A)->list:
    R1=[]
    for a in A:
        for b in A:
            if proprietate(a,b):
                R1.append((a,b))
    return R1

def partitie(A,set_partitie)->bool:
    for p1 in set_partitie:
        if len(p1)==0:
            print("o partitie este vida")
            return 0
        
    for p2 in set_partitie:
        if p2.issubset(A)==0:
            print("o partitie nu corespunde multimii A")
            return 0
        
    elemente_vazute = set()
    for subset in set_partitie:
        for element in subset:
            if element in elemente_vazute:
                print("partitiile nu sunt disjuncte")
                return 0
            elemente_vazute.add(element)
    
    multimiea_partitiilor = set().union(*set_partitie)
    if multimiea_partitiilor != A:
        print("reuniunea partiilor nu da A")
        return 0
    
    return 1
def O1(x,y):
    return x==y

def O2(x,y):
    return x!=y

def O3(x,y):
    return x>=y

def determinare_relatie_O1(A)->list:
    R1=[]
    for a in A:
        for b in A:
            if O1(a,b):
                R1.append((a,b))
    return R1

def determinare_relatie_O2(A)->list:
    R1=[]
    for a in A:
        for b in A:
            if O2(a,b):
                R1.append((a,b))
    return R1

def determinare_relatie_O3(A)->list:
    R1=[]
    for a in A:
        for b in A:
            if O3(a,b):
                R1.append((a,b))
    return R1

def afisare_diagrama_hesse(graf):
    for nod in graf:
        lista_nod=graf[nod]
        print("Nodul %c este acoperit de:" %nod, end=' ')
        
        for nd in lista_nod:
            print("%c"%nd, end=' ')
        print()

def elemente_maximale(graf):
    count=0
    lista_elemente_maximale=[]
    for nod in graf:
        if len(graf[nod])==0:
            count=count+1
            lista_elemente_maximale.append(nod)
    if count==0:
        print("nu existe elemente maximale")
    elif count==1:
        print("elementul maximal este:",lista_elemente_maximale)
    else:
        print("elementele maximale sunt",lista_elemente_maximale)

def elemente_minimale(graf):
    count=0
    lista_elemente_minimale=[]
    for nod in graf:
        aparitii=0
        for nod_1 in graf:
            if nod in graf[nod_1]:
                aparitii=aparitii+1
        if aparitii==0:
            count=count+1
            lista_elemente_minimale.append(nod)
    if count==0:
        print("nu exista elemente minimale")
    elif count==1:
        print("elementul minimal este:",lista_elemente_minimale)
    else:
        print("elementele minimale sunt:",lista_elemente_minimale)

def sortare_topologica(graf)->list:
    lista_sortata_topologic=[]
    nr_elemente_minimale=0
    liste_elememente_minimale=[]
    while graf:
        nr_elemente_minimale,liste_elememente_minimale=elemente_minimale_ajutor(graf)
        if nr_elemente_minimale==1:
            lista_sortata_topologic.append(liste_elememente_minimale[0])
            graf.pop(liste_elememente_minimale[0])
        else:
            print("alegeti un element minimal pe care vreti sa-l stergeti:",liste_elememente_minimale)
            ok=1
            while ok:
                x=input()
                if x in liste_elememente_minimale:
                    lista_sortata_topologic.append(x)
                    graf.pop(x)
                    ok=0
                else:
                    print("ati ales gresit, introduceti alt element din lista elementelor minimale:")
                    print(liste_elememente_minimale)
    return lista_sortata_topologic



def elemente_minimale_ajutor(graf):
    count=0
    lista_elemente_minimale=[]
    for nod in graf:
        aparitii=0
        for nod_1 in graf:
            if nod in graf[nod_1]:
                aparitii=aparitii+1
        if aparitii==0:
            count=count+1
            lista_elemente_minimale.append(nod)
    if count==0:
        print("nu exista elemente minimale")
    else:
        return count, lista_elemente_minimale

def add(a, b)->int:
    return a+b