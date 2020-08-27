"""
Napravi listu dictionary-a koji se sastoje od imena, prezimena i godina osobe
a zatim od tih osoba naci one koji su stariji od 20
"""

nastavi="y"
osobe=[]
while nastavi=="y":
    ime=input("Unesi ime osobe: ")
    prezime=input("Unesi prezime osobe: ")
    godine=int(input("Unesi godine osobe: "))
    osobe.append({"ime":ime, "prezime":prezime, "godine":godine})
    nastavi = input("Za dalje unesite y ")

starijiOd20=[]
for osoba in osobe:
    if osoba["godine"]>20:
        starijiOd20.append(osoba)

print("Lista osoba je", osobe)
print("Lista osoba starijih od 20 su:", starijiOd20)