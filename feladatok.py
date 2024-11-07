import random
def paros_szamok():
    i:int=0
    while(i%2!=0):
        szam:int=input("Adj meg egy páros számot: ")
        if(szam%2==0):
            print(szam)
        else:
            szam:int=input("Adj meg egy páros számot: ")
        i+=1
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



          




