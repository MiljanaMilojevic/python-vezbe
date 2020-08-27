def prosecnaVisina(listaOsoba):
    '''
    svaka osoba je predstavljena dictionaryem 
    {"ime":ime, "prezime":prezime, "visina":visina}
    '''
    ukupnaVisina = 0
    for osoba in listaOsoba:
        ukupnaVisina += osoba["visina"]

    return ukupnaVisina / len(listaOsoba)

nastavi="y"
osobe = []
while nastavi == "y":
    ime = input("Unesite ime osobe: ")
    prezime = input("Unesite prezime osobe: ")
    visina = int(input("Unesite visinu osobe: "))
    osobe.append({"ime":ime, "prezime":prezime, "visina":visina})
    nastavi = input("Za dalje unesite y ")
print(osobe)
print("Prosecna visina osoba je: ", prosecnaVisina(osobe))