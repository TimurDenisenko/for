from random import *
from time import *
#5
try:
    print("")
    print("5 Harjutus")
    toa=int(input("Kui palju toa on korteris? "))
    for i in range(1,toa+1,1):
        grad=float(input(f"Mis on temperatuur toas {i} "))
        if grad>=18:
            print("Suurepärane temperatuur!")
        else:
            print("Lülitage patareid sisse!")
except:
    print("Palun kirjuta õige temperatuur!")

#6
try:
    print("")
    print("6 Harjutus")
    a=b=c=0
    kogus=randint(1,20)
    print(f"Kokku on {kogus} inimest")
    for i in range(1,kogus+1,1):
        pikkus=randint(56,250)
        sleep(1)
        if pikkus<=150:
            print(f"{i} inimene on lühike, kasvu on {pikkus}")
            a+=1
        elif pikkus>150 and pikkus<=180:
            print(f"{i} inimene on keskmine, kasvu on {pikkus}")
            b+=1
        else:
            print(f"{i} inimene on pikk, kasvu on {pikkus}")
            c+=1
except:
    print("Midagi on vale")
summ=a+b+c 
print(f" {a} lühikese inimest,\n {b} keskmise inimest,\n {c} pikka inimest")

#6.1
try:
    print("")
    print("6.1 Harjutus")
    a=b=c=0
    kogus=randint(1,20)
    print(f"Kokku on {kogus} inimest")
    while kogus>0:
        pikkus=randint(56,250)
        sleep(1)
        if pikkus<=150:
            print(f"lühike, kasvu on {pikkus}")
            a+=1
        elif pikkus>150 and pikkus<=180:
            print(f"keskmine, kasvu on {pikkus}")
            b+=1
        else:
            print(f"pikk, kasvu on {pikkus}")
            c+=1
        kogus-=1
    summ=a+b+c 
    print(f" {a} lühikese inimest,\n {b} keskmise inimest,\n {c} pikka inimest")
except:
    print("Midagi on vale")

#9
print("")
print("9 harjutus")
w = 10
while w>0:
    a=input("Kirjutage 1 külje pikkus - ")
    while a.isdigit()==False:
        a=input("Kirjutage 1 külje pikkus - ")
    if float(a)>0:
        b=input("Kirjutage 2 külje pikkus - ")
        while b.isdigit()==False:
            b=input("Kirjutage 2 külje pikkus - ")
        if float(b)<0:
            print("Kirjuta õige number")
        else:
            if a==b:
                print("See on ruut!")
                break
            else:
                print("See ei ole ruut!")
    else:
        print("Palun kirjuta õige number")
