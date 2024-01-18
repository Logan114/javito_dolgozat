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
    auto_es_kora = (f"{kerdes} - {kor} éves")
    print(auto_es_kora)


def ki (auto_lista):
    date = datetime.datetime.now()
    year = int((date.strftime("%Y")))
    ki = open ("ki.txt","a", encoding="UTF-8")
    gy_ev: int = 0
    auto_nev = ""
    for i in range (0,len(auto_lista),1):
        auto_nev = auto_lista[i].nev
        gy_ev:int = int(auto_lista[i].ev)
        kor = year - gy_ev
        ki.write(f"{auto_nev} - {kor} éves\n")
    ki.close

def flotta(auto_lista):
    flotta = len(auto_lista)
    print (f"{flotta} autónk van")

def ertekes(auto_lista):
    evek_lista = []
    legoregebb_nev = ""
    for i in range (0,len(auto_lista),1):
        evek_lista.append(auto_lista[i].ev)
    legoregebb = min(evek_lista)
    for i in range (0,len(auto_lista),1):
        if auto_lista[i].ev == legoregebb:
            legoregebb_nev = auto_lista[i].nev
    print (f"A legöregebb autó: {legoregebb_nev} {legoregebb}")


