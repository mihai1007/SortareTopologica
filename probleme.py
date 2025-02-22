import numpy as np
import functii as f

def p1()->None:
    ok=0
    A = {0, 1, 2, 3}
    n=len(A)
    R = {(0,0), (1,1), (2,2), (3,3)}
    M_a=f.determinareMatrice(R,n)
    ok=ok+f.reflexiva(M_a)
    ok=ok+f.simetrica(M_a)
    ok=ok+f.tranzitivitate(M_a)
    if ok==3:
        print("echivalenta")
    else:
        print("nu este echivalenta")
    ok=0
    R = {(0,0), (0,2), (2,0), (2,2), (2,3), (3,2), (3,3)}
    M_a=f.determinareMatrice(R,n)
    ok=ok+f.reflexiva(M_a)
    ok=ok+f.simetrica(M_a)
    ok=ok+f.tranzitivitate(M_a)
    if ok==3:
        print("echivalenta")
    else:
        print("nu este echivalenta")
    ok=0
    R = {(0,0), (1,1), (1,2), (2,1), (2,2), (3,3)}
    M_a=f.determinareMatrice(R,n)
    ok=ok+f.reflexiva(M_a)
    ok=ok+f.simetrica(M_a)
    ok=ok+f.tranzitivitate(M_a)
    if ok==3:
        print("echivalenta")
    else:
        print("nu este echivalenta")
    ok=0
    R = {(0,0), (1,1), (1,3), (2,2), (2,3), (3,1), (3,2), (3,3)}
    M_a=f.determinareMatrice(R,n)
    ok=ok+f.reflexiva(M_a)
    ok=ok+f.simetrica(M_a)
    ok=ok+f.tranzitivitate(M_a)
    if ok==3:
        print("echivalenta")
    else:
        print("nu este echivalenta")
    ok=0
    R = {(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,2), (3,3)}
    M_a=f.determinareMatrice(R,n)
    ok=ok+f.reflexiva(M_a)
    ok=ok+f.simetrica(M_a)
    ok=ok+f.tranzitivitate(M_a)
    if ok==3:
        print("echivalenta")
    else:
        print("nu este echivalenta")
def p4()->None:
    A = {1, 2, 4, 5, 7, 11, 13}
    relatie=f.determinare_relatie(A)
    matrix_relatie=f.determinareMatrice(relatie,13)
    print(matrix_relatie)
    ok=0
    ok=ok+f.reflexiva(matrix_relatie)
    ok=ok+f.simetrica(matrix_relatie)
    ok=ok+f.tranzitivitate(matrix_relatie)
    if ok==3:
        print("echivalenta")
    else:
        print("nu este echivalenta")

def p2():
    A={1, 2, 3, 4, 5, 6}
    p1=[{1, 2}, {2, 3, 4}, {4, 5, 6}]
    p2=[{1}, {2, 3, 6}, {4}, {5}]
    p3=[{2, 4, 6}, {1, 3, 5}]
    p4=[{1, 4, 5}, {2, 6}]

    if(f.partitie(A,p1)):
        print("partitie")

    if(f.partitie(A,p2)):
        print("partitie")
    
    if(f.partitie(A,p3)):
        print("partitie")

    if(f.partitie(A,p4)):
        print("partitie")
    

def p3():
    A={-3, -2, -1, 0, 1, 2, 3}
    p1=[{-3, -1, 1, 3}, {-2, 0, 2}]
    p2=[{-3, -2, -1, 0}, {0, 1, 2, 3}]
    p3=[{-3, 3}, {-2,2}, {-1, 1}, {0}]
    p4=[{-3, -2, 2, 3}, {-1, 1}]

    if(f.partitie(A,p1)):
        print("partitie")

    if(f.partitie(A,p2)):
        print("partitie")
    
    if(f.partitie(A,p3)):
        print("partitie")

    if(f.partitie(A,p4)):
        print("partitie")

def p5():
    A = {-3, -2, -1, 0, 1, 2, 3}
    n=len(A)
    R_1=f.determinare_relatie_O1(A)
    R_2=f.determinare_relatie_O2(A)
    R_3=f.determinare_relatie_O3(A)
    M_1=f.determinareMatrice(R_1,n)
    M_2=f.determinareMatrice(R_2,n)
    M_3=f.determinareMatrice(R_3,n)
    ok=0
    ok=ok+f.reflexiva(M_1)
    ok=ok+f.antisimetrica(M_1)
    ok=ok+f.tranzitivitate(M_1)
    if ok==3:
        print("partial ordonata")
    else:
        print("nu este partial ordonata")
    ok=0
    ok=ok+f.reflexiva(M_2)
    ok=ok+f.antisimetrica(M_2)
    ok=ok+f.tranzitivitate(M_2)
    if ok==3:
        print("partial ordonata")
    else:
        print("nu este partial ordonata")
        ok=0
    ok=ok+f.reflexiva(M_3)
    ok=ok+f.antisimetrica(M_3)
    ok=ok+f.tranzitivitate(M_3)
    if ok==3:
        print("partial ordonata")
    else:
        print("nu este partial ordonata")

def p6():
    A = {0, 1, 2, 3}
    n=len(A)
    R_1 = {(0,0), (1,1), (2,2), (3,3)}
    R_2 = {(0,0), (1,1), (2,0), (2,2), (2,3), (3,2), (3,3)}
    R_3 = {(0,0), (1,1), (1,2), (2,2), (3,3)}
    R_4 = {(0,0), (1,1), (1,2), (1,3), (2,2), (2,3), (3,3)}
    R_5 = {(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,2), (3,3)}
    R_6 = {(0,0), (1,1), (1,2), (1,3), (2,0), (2,2), (2,3), (3,0), (3,3)}

    M_1=f.determinareMatrice(R_1,n)
    M_2=f.determinareMatrice(R_2,n)
    M_3=f.determinareMatrice(R_3,n)
    M_4=f.determinareMatrice(R_4,n)
    M_5=f.determinareMatrice(R_5,n)
    M_6=f.determinareMatrice(R_6,n)

    print("a")
    ok=0
    ok=ok+f.reflexiva(M_1)
    ok=ok+f.antisimetrica(M_1)
    ok=ok+f.tranzitivitate(M_1)
    if ok==3:
        print("partial ordonata")
    else:
        print("nu este partial ordonata")

    print("b")
    ok=0
    ok=ok+f.reflexiva(M_2)
    ok=ok+f.antisimetrica(M_2)
    ok=ok+f.tranzitivitate(M_2)
    if ok==3:
        print("partial ordonata")
    else:
        print("nu este partial ordonata")
        
    print("c")
    ok=0
    ok=ok+f.reflexiva(M_3)
    ok=ok+f.antisimetrica(M_3)
    ok=ok+f.tranzitivitate(M_3)
    if ok==3:
        print("partial ordonata")
    else:
        print("nu este partial ordonata")

    print("d")
    ok=0
    ok=ok+f.reflexiva(M_4)
    ok=ok+f.antisimetrica(M_4)
    ok=ok+f.tranzitivitate(M_4)
    if ok==3:
        print("partial ordonata")
    else:
        print("nu este partial ordonata")
    
    print("e")
    ok=0
    ok=ok+f.reflexiva(M_5)
    ok=ok+f.antisimetrica(M_5)
    ok=ok+f.tranzitivitate(M_5)
    if ok==3:
        print("partial ordonata")
    else:
        print("nu este partial ordonata")

    print("f")
    ok=0
    ok=ok+f.reflexiva(M_6)
    ok=ok+f.antisimetrica(M_6)
    ok=ok+f.tranzitivitate(M_6)
    if ok==3:
        print("partial ordonata")
    else:
        print("nu este partial ordonata")

def p7():
    M_a=[[1,0,1],[1,1,0],[0,0,1]]
    M_b=[[1,0,0],[0,1,0],[1,0,1]]
    M_c=[[1,0,1,0],[0,1,1,0],[0,0,1,1],[1,1,0,1]]
    M_d=[[1,1,1],[1,1,0],[0,0,1]]
    M_e=[[1,1,1],[0,1,0],[0,0,1]]
    M_f=[[1,1,1,0],[0,1,1,0],[0,0,1,1],[1,1,0,1]]

    print("a")
    ok=0
    ok=ok+f.reflexiva(M_a)
    ok=ok+f.antisimetrica(M_a)
    ok=ok+f.tranzitivitate(M_a)
    if ok==3:
        print("partial ordonata")
    else:
        print("nu este partial ordonata")
    
    print("b")
    ok=0
    ok=ok+f.reflexiva(M_b)
    ok=ok+f.antisimetrica(M_b)
    ok=ok+f.tranzitivitate(M_b)
    if ok==3:
        print("partial ordonata")
    else:
        print("nu este partial ordonata")

    print("c")
    ok=0
    ok=ok+f.reflexiva(M_c)
    ok=ok+f.antisimetrica(M_c)
    ok=ok+f.tranzitivitate(M_c)
    if ok==3:
        print("partial ordonata")
    else:
        print("nu este partial ordonata")

    print("d")
    ok=0
    ok=ok+f.reflexiva(M_d)
    ok=ok+f.antisimetrica(M_d)
    ok=ok+f.tranzitivitate(M_d)
    if ok==3:
        print("partial ordonata")
    else:
        print("nu este partial ordonata")

    print("e")
    ok=0
    ok=ok+f.reflexiva(M_e)
    ok=ok+f.antisimetrica(M_e)
    ok=ok+f.tranzitivitate(M_e)
    if ok==3:
        print("partial ordonata")
    else:
        print("nu este partial ordonata")

    print("f")
    ok=0
    ok=ok+f.reflexiva(M_f)
    ok=ok+f.antisimetrica(M_f)
    ok=ok+f.tranzitivitate(M_f)
    if ok==3:
        print("partial ordonata")
    else:
        print("nu este partial ordonata")

def p8():
    graf_a={
        'a':['d'], 'b':['d','e'], 'c':['f'], 'd':['i','h'], 'e':['h'], 'f':['g'], 'i':['j'], 'h':['j','k'], 'g':['k'], 'j':['l'], 'k':['m'], 'l':[], 'm':[]
        }
    graf_b={
        'a':['b','c'],'b':['d','e'],'c':['e'],'d':['f'],'e':['f'],'f':['g'],'g':[]
        }
    graf_c={
        'a':['b','c'],'b':['d','g'],'c':['e'],'d':['f'],'e':['f','g'],'f':['h'],'g':['h'],'h':[]
    }
    graf_d={
        'a':['b','c'],'b':['d','g'],'c':['e'],'d':['f'],'e':['g'],'f':['h'],'g':['h'],'h':['i'],'i':[]
    }
    print("a")
    f.afisare_diagrama_hesse(graf_a)
    f.elemente_maximale(graf_a)
    f.elemente_minimale(graf_a)
    print("b")
    f.afisare_diagrama_hesse(graf_b)
    f.elemente_maximale(graf_b)
    f.elemente_minimale(graf_b)
    print("c")
    f.afisare_diagrama_hesse(graf_c)
    f.elemente_maximale(graf_c)
    f.elemente_minimale(graf_c)
    print("d")
    f.afisare_diagrama_hesse(graf_d)
    f.elemente_maximale(graf_d)
    f.elemente_minimale(graf_d)

def p9():
    graf_a={
        'a':['d'], 'b':['d','e'], 'c':['f'], 'd':['i','h'], 'e':['h'], 'f':['g'], 'i':['j'], 'h':['j','k'], 'g':['k'], 'j':['l'], 'k':['m'], 'l':[], 'm':[]
        }
    lista=f.sortare_topologica(graf_a)
    print(lista)
