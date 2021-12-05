from tkinter import *
from PIL import ImageTk, Image

ekran = Tk()
ekran.title("Resim Albümü")
ekran.geometry("670x700")
ekran.configure(bg= "pink")
ekran.iconbitmap("ico/cicek.ico")

baslik = Label(ekran, text="Vektör Çiçekler")
baslik.config(font=("Times New Roman", 18), fg="white", bg="purple")
baslik.grid(row=0, column=0, padx= 5, pady=5)

resimler = ["img/cicek.png", "img/cicek_02.png", "img/cicek_03.png"]

resim = 0

def goster():
    gorsel = ImageTk.PhotoImage(Image.open(resimler[resim]))
    cerceve = Label(image=gorsel)
    cerceve.image = gorsel
    cerceve.grid(row=1, column=0, padx= 5, pady=5)

goster()

def sonraki():
    global resim
    if resim < len(resimler)-1:
        resim +=1
    else:
        resim = 0
    print(resim)
    goster()

ileri = Button(text="İleri", command=sonraki)
ileri.grid(row=2, column=0, padx= 5, pady= 5)
ileri.config(font=("Times New Roman", 18), fg="white", bg="purple")

def önceki():
    global resim
    if resim < len(resimler)-1:
        resim -=1
    else:
        resim = 0
    print(resim)
    goster()

geri = Button(text="Geri", command=önceki)
geri.grid(row=3, column=0, padx=5, pady=5)
aciklama =Label(ekran, text= "Çiçekler")
geri.config(font=("Times New Roman", 18), fg="white", bg="purple")

cikis = Button(ekran, text="Çıkış!", command=ekran.quit, fg="white", bg="purple")
cikis.grid(row=5, column=0)

ekran.mainloop()
