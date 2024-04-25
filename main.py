import time
import random

def wyslij_sowe(adresat, tresc):
    print(f"Twój list do {adresat} już leci!")
    time.sleep(1)
    if random.uniform(0,1) <= 0.85:
        return True
    else:
        return False

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

def wybierz_sowe_zwroc_koszt(potwierdzenie: bool, odleglosc: str, typ: str, specjalna: str):
    """
    Obliczanie kosztu wysłania sowy.

    :param potwierdzenie: True/False.
    :param odleglosc: lokalna, krajowa, dalekobiezna.
    :param typ: list, paczka.
    :param specjalna: wyjec, list gończy.
    :return: koszt wysłania wybranej sowy.
    """

    koszty = {
        "list": {
            "lokalna": {"knut": 2},
            "krajowa": {"knut": 12},
            "dalekobiezna": {"knut": 20},
        },
        "paczka": {
            "lokalna": {"knut": 7},
            "krajowa": {"sykl": 1, "knut": 2},
            "dalekobiezna": {"sykl": 2, "knut": 1},
        },
        "specjalna": {
            "wyjec": {"knut": 4},
            "list gończy": {"sykl": 1},
        },
        "potwierdzenie": {
            "knut": 7,
        }
    }

    koszt = {"knut": 0, "sykl": 0, "galeon": 0}
    def dodaj_koszty(cennik):
        for waluta, cena in cennik.items():
            koszt[waluta] += cena
    try:
        if potwierdzenie:
            dodaj_koszty(koszty["potwierdzenie"])
        dodaj_koszty(koszty[typ][odleglosc])
        dodaj_koszty(koszty["specjalna"][specjalna])
    except KeyError:
        raise Exception("Podaj prawidłowe dane.")

    return koszt

def waluta_dict_na_str(waluta_dict):
    sorted_dict = {"galeon": waluta_dict["galeon"],
                   "sykl": waluta_dict["sykl"],
                   "knut": waluta_dict["knut"]}

    wynik = []
    for moneta, ilosc in sorted_dict.items():
        if ilosc != 0:
            wynik.append(f"{ilosc} {moneta}")

    return " ".join(wynik)
