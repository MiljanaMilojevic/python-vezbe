osobe=[("jovan", 196, 96),("ana",155,55),("marko",185,85),("jana",165,55),("zika",195,85),("pera",195,84),("marija",165,54), ("jovana",155,55)]

listaTezina=[]
listaVisina=[]
for osoba in osobe:
    listaTezina.append(osoba[2])
    listaVisina.append(osoba[1])



prosecnaTezina=sum(listaTezina)/len(listaTezina)
prosecnaTezina=round(prosecnaTezina,2)
prosecnaVisina=sum(listaVisina)/len(listaVisina)
prosecnaVisina=round(prosecnaVisina,2)


print(f"Prosecna tezina je {prosecnaTezina}kg.")
print(f"Prosecna tezina je {prosecnaVisina}kg.")

najtezaOsoba=osobe[0]

for osoba in osobe:
    if osoba[2]>najtezaOsoba[2]:
        osoba=najtezaOsoba

print(f'najteza osoba je {najtezaOsoba[0]}, a masa te osobe je {najtezaOsoba[2]} ')

najnizaOsoba=osobe[0]

for persona in osobe:
    if persona[1]<najnizaOsoba[1]:
        najnizaOsoba=persona

print(f'Najniza osoba je {najnizaOsoba[0]} a visoka je {najnizaOsoba[1]}cm ')

najvisaOsoba=osobe[0]
for covek in osobe:
    if covek[2]>najvisaOsoba[2]:
        covek=najvisaOsoba

print(f'Najvisa osoba je {najvisaOsoba[0]}, a teska je {najvisaOsoba[2]} kg ')

# isteTezine=[]
# for osoba in osobe:
#     for osoba2 in osobe:
#         if osoba[2]==osoba2[2]:
#             isteTezine.append((osoba[2],osoba2[2]))
# jedinstveneTezine=set(isteTezine)
# print('Osobe sa istim tezinama imaju po',jedinstveneTezine,'kg')
from operator import itemgetter
import itertools

osobeIsteTezine=[]
osobeIsteVisine=[]
for osoba in osobe:
    if listaTezina.count(osoba[2])>1:# and osoba not in osobeIsteTezine:
        osobeIsteTezine.append(osoba)
    if listaVisina.count(osoba[1])>1:# and osoba not in osobeIsteVisine:
        osobeIsteVisine.append(osoba)

osobeIsteTezine.sort(key=itemgetter(2))
osobeIsteVisine.sort(key=itemgetter(1))


#izvuci osobe koje imaju i istu visinu i istu tezinu
istaVisinaTezina=[]
listaVisinaTezina=[]
for osoba in osobeIsteTezine:
    istaVisinaTezina.append((osoba[1:]))
for osoba in osobeIsteTezine:
    if istaVisinaTezina.count(osoba[1:])>1:
        listaVisinaTezina.append(osoba)

print(listaTezina)
print(osobeIsteTezine)
print(listaVisina)
print(osobeIsteVisine)
print(listaVisinaTezina)




for kg,osobeTezina in itertools.groupby(osobeIsteTezine, itemgetter(2)):
    t=list(osobeTezina)
    print(f"Osobe sa istom tezinom od {kg} kg su: {t}")
    print(f"Od osoba sa istom tezinom od {kg} kg, najvisa je {max(t,key=itemgetter(1))}")
    print(f"Od osoba sa istom tezinom od {kg} kg, najmanja je {min(t, key=itemgetter(1))}")

for cm,osobeVisina in itertools.groupby(osobeIsteVisine, itemgetter(1)):
    v=list(osobeVisina)
    print(f"Osobe sa istom visinom od {cm} cm su: {v}")
    print(f"Od osoba sa istom visinom od {cm} cm, najteza je: {max(v,key=itemgetter(2))}")
    print(f"Od osoba sa istom visinom od {cm} cm, najlaksa je: {min(v,key=itemgetter(2))}")
    