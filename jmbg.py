"""
Napisati funkciju koja iz jmbg-a vraca rodjenja osobe,formiran dd-mm-yyyy
"""
def vracaDatumrodjenja(jmbg):
    dd=jmbg[0:2]
    mm=jmbg[2:4]
    gg=jmbg[4:7]

    if jmbg[4]=="9":
        return f"Datum rodjenja je {dd}.{mm}.1{gg}."
    else:
        return f"Datum rodjenja je {dd}.{mm}.2{gg}."


jmbg = input("Unesite jmbg: ")
print (vracaDatumrodjenja(jmbg))