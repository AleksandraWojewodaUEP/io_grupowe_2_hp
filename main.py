

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

    if potwierdzenie:
        dodaj_koszty(koszty["potwierdzenie"])
    dodaj_koszty(koszty[typ][odleglosc])
    dodaj_koszty(koszty["specjalna"][specjalna])

    return koszt
