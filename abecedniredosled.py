"""
Napisati program za unos sa tastature liste osoba a zatim sortirati tu listu po prezimenu u leksikografskom poretku.
"""

class Osoba:
    def __init__(self, ime, prezime):
        self.ime = ime
        self.prezime = prezime
    def __repr__(self):
        return f"Osoba {self.ime} {self.prezime}"
        
def AbecedniRedosled(listaOsoba):
    listaAbecedniRedosled = sorted(listaOsoba, key=lambda x: x.prezime, reverse=False)
    return listaAbecedniRedosled
    
osobe = []
nastavi = "y"
while nastavi == "y":
    ime = input("Unesite ime osobe: ")
    prezime = input("Unesite prezime osobe: ")
    o = Osoba(ime, prezime)
    osobe.append(o)
    nastavi = input("za dalje unesite y :")
    
osobeAbecedniRedosled = AbecedniRedosled(osobe)

print("Osobe sa abecednim redosledom su:",osobeAbecedniRedosled)
