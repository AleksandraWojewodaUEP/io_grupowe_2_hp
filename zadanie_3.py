def licz_sume(fundusz):
    # Przeliczenie knutów na sykle
    knuty = sum(fundusz.get("knut"))
    knut_sykl = knuty // 21
    knuty = knuty % 21

    # Dodanie knutów do sykli i przeliczenie sykli na galeony 
    sykle = sum(fundusz.get("sykl")) + knut_sykl
    sykl_galeon = sykle // 17
    sykle = sykle % 17

    # Dodanie sykli do galeonów
    galeony = sum(fundusz.get("galeon")) + sykl_galeon

    return {
        "galeon": galeony,
        "sykl": sykle,
        "knut": knuty
    }

# Przykładowe wejście
fundusz = {
    "galeon": [1, 3, 5],
    "sykl": [18, 20, 10],
    "knut": [30, 40, 7]
}

wynik = licz_sume(fundusz)
print(wynik)



