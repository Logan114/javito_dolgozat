random_lista = []
from random import randint
for i in range (0,50):
    szam = randint(1,100)
    random_lista.append(szam)


def hettel_oszthato(lista):
    oszthato_szamok = 0
    print(lista)
    for i in range(0,len(lista),1):
        if lista[i] % 7 == 0:
            oszthato_szamok += 1
    print (f"\nA listában {oszthato_szamok} héttel oszható szám van")

hettel_oszthato(random_lista)