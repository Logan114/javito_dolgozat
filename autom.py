from auto_class import Auto
import datetime

file = open("auto.txt","r", encoding="UTF-8")
file_lista = file.readlines()[1:]
auto_lista = []
for i in range (0,len(file_lista),1):
    jelen_sor = file_lista[i]
    tisztitott_sor = jelen_sor.strip().split(":")
    nev = tisztitott_sor[0]
    ev = tisztitott_sor[1]
    auto = Auto(nev,ev)
    auto_lista.append(auto)

def kor(auto_lista,kerdes:str):
    gyartasiev:int = int(0)
    date = datetime.datetime.now()
    year = int((date.strftime("%Y")))
    for i in range (0,len(auto_lista),1):
        if auto_lista[i].nev == kerdes:
            gyartasiev = int(auto_lista[i].ev)
    kor = year - gyartasiev
    print (f"{kerdes}, {kor} éves")

