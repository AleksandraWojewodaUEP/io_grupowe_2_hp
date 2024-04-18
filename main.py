import time
import random

def wyslij_sowe(adresat, tresc):
    print(f"Twój list do {adresat} już leci!")
    time.sleep(1)
    if random.uniform(0,1) <= 0.85:
        return True
    else:
        return False

# print(wyslij_sowe("Hagrid", "Wpadamy na herabtkę"))

def licz_sume(dane):
  
    if 'galeon' not in dane or 'sykl' not in dane or 'knut' not in dane:
        return "Brak wymaganych danych"

    ilosc_galeon = dane.get('galeon', 0)
    ilosc_sykl = dane.get('sykl', 0)
    ilosc_knut = dane.get('knut', 0)

    suma_knut = ilosc_galeon * 17 * 21 + ilosc_sykl * 21 + ilosc_knut

    suma_galeon = suma_knut // (17 * 21)
    suma_knut %= (17 * 21)
    suma_sykl = suma_knut // 21
    suma_knut %= 21

    return {'galeon': suma_galeon, 'sykl': suma_sykl, 'knut': suma_knut}

dane = {'galeon': 0, 'sykl': 100, 'knut': 106}
wynik = licz_sume(dane)
print(wynik)
