import random
def paros_szamok():
    szam:int=int(input("Adj meg egy páros számot: "))
    i:int=0
    while(szam %2!=0):
        if(szam %2==0):
            print(szam)
        else:
            szam:int=int(input("Adj meg egy páros számot: "))
        i+=1
    print(f"{szam}")
    print()

def veletlen_szam():
    lista=[]
    i:int=0
    while(i<13):
        szam:int=int(random.random()*141)+10
        i+=1
        lista.append(szam)
    print(lista)

    i:int=0
    db:int=0
    while(i<len(lista)):
        if(lista[i]%3==0):
            db+=1
        i+=1
    print(f"A számok között {db} db 3-mal osztható van!")

def karakter(text:str,n:int):
    if(len(text)>n):
        karakter:str=text[n]
        nagy_betu= karakter.upper()
        print(f"A szöveg {n}. karaktere {karakter} - {3*nagy_betu}")
    else:
        print(f"Nincsen {n}. karakter!")

def nevet_ker():
    nev:str=input("Adj meg nevet: ")

    i:int=0
    db:int=0
    while(nev!="@"):
        nev:str=input("Adj meg nevet: ")
        db+=1
        i+=1
        if(nev=="@"):
            print(f"A felhasználó {db} nevet adott meg.")
    print()

def ko_papir_ollo():
    









          




