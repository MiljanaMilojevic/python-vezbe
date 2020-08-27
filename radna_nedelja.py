from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Broj radnih sati")
root.geometry("730x260")

class Checkbar(ttk.Frame):
    def __init__(self, parent = None, picks = [], anchor = W, question = ""):
        Frame.__init__(self, parent)
        dayLabel = ttk.Frame(self)
        dayFrame = ttk.Frame(self)
        dayLabel.pack(pady = 10)
        dayFrame.pack(pady = 10, padx = 10)
        questionLabel = ttk.Label(dayLabel, text = question)
        questionLabel.pack()
        self.vars = []
        self.picks = picks
        for pick in picks:
            var = IntVar()
            chk = ttk.Checkbutton(dayFrame, text = pick, variable = var, offvalue=0)
            chk.pack(anchor=anchor, expand=YES)
            self.vars.append(var)

    def clean(self):
        for var in self.vars:
            var.set(0)

    def state(self):
        return [var.get() for var in self.vars]

    def stateRepresent(self):
        picked = [p[0] for p in zip(self.picks, self.vars) if p[1].get() == 1]
        for var in self.vars:
            var.set(0)
        return picked



class Radiobar(ttk.Frame):
    def __init__(self, parent = None, picksRadio = [], anchor = W, questionLabel = ""):
        Frame.__init__(self, parent)
        personLabel = ttk.Frame(self)
        personFrame = ttk.Frame(self)
        personLabel.pack(pady = 15)
        personFrame.pack(pady = 5, padx = 10)
        personQuestionLabel = ttk.Label(personLabel, text = questionLabel)
        personQuestionLabel.pack()
        self.vars = []
        self.picksRadio = picksRadio
        self.var = IntVar()
        i = 1
        for pick in picksRadio:
            rad = ttk.Radiobutton(personFrame, text = pick, variable = self.var, value = i)
            i += 1
            rad.pack(anchor = anchor, expand = YES, side = LEFT, padx = 15)
            self.vars.append(self.var)

    def clean01(self):
        for var in self.vars:
            var.set(0)

    def state(self):
        return self.var.get()




chk = Checkbar(root, ['Ponedeljak', 'Utorak', 'Sreda', 'Cetvrtak', 'Petak'], question="Izaberite radni dan")
rad = Radiobar(root, ['Muski', 'Zenski'], questionLabel="Izaberite pol osobe")

rad.grid(row = 0, column = 0, sticky = N)
chk.grid(row = 1, column = 0, sticky = N)


buttonFrame = ttk.Frame(root, padding = '0.1i')
resultFrame = ttk.Frame(root, padding = '0.1i')

def suma():
    suma = 0
    rezultati = list(chk.state())
    pol = rad.state()
    for dan in rezultati:
        if dan == 1:
            suma += 1
        rezultat = suma*8
        if pol == 1:
            resultFrameLabel["text"] = f"Osoba Muskog pola je radila {rezultat} sati."
        else:
            resultFrameLabel["text"] = f"Osoba Zenskog pola je radila {rezultat} sati."


def obrisi():
    chk.clean()
    rad.clean01()
    resultFrameLabel["text"] = "Izaberite pol i dane kada je osoba radila i pritisnite dugme 'Ukupno'"

btn_ukupno = Button(buttonFrame, text = "Ukupno", width = 15, command = suma)
btn_obrisi = Button(buttonFrame, text = "Obrisi", width = 15, command = obrisi)




btn_ukupno.pack()
btn_obrisi.pack()

resultFrameLabel = Label(resultFrame, text = "Izaberite pol i dane kada je osoba radila i pritisnite dugme 'Ukupno'")
resultFrameLabel.pack()



buttonFrame.grid(row = 1, column = 1, sticky = N)
resultFrame.grid(row = 1, column = 2, sticky = N)

root.mainloop()