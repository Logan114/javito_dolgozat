def keveres(min,max):
    szinkodok = input ("Adja meg a szinkódokat:")
    if len(szinkodok) < min:
        print("Nem megfelelő hossz")
    elif len(szinkodok)>max:
        print("Bonyolult kiszámolni")
    else:
        print("Megfelelő hossz")

keveres_fajta = input("Milyen módszerben szeretne keverni?")
if keveres_fajta == "RGB" or "rgb":
    keveres(5,11)
elif keveres_fajta == "HEX" or "hex":
    keveres(6,6)
elif keveres_fajta == "HSL" or "hsl":
    keveres(7,13)
