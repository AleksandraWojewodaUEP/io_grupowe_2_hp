from main import waluta_dict_na_str, waluta_str_na_dict, nadaj_sowe, poczta_wyslij_sowy, wyslij_sowe

# Task 5

currencies1 = {
    "knut": 13,
    "galeon": 0,
    "sykl": 0,
}

currencies2 = {
    "sykl": 2,
    "galeon": 13,
    "knut": 13
}

assert (waluta_dict_na_str(currencies1) == "13 knut")
assert (waluta_dict_na_str(currencies2) == "13 galeon 2 sykl 13 knut")

# Task 6
assert (waluta_str_na_dict("13 knut") == {'knut': '13'})
assert (waluta_str_na_dict("22 galeon 15 sykl 4 knut") == {'galeon': '22', 'sykl': '15', 'knut': '4'})

# Task 7
recipient = "Hagrid"
content = "Hi"
confirmation = True
distance = "lokalna"
type = "list"
special = "wyjec"
nadaj_sowe(recipient, content, confirmation, distance, type, special)
import csv
rows = []
with open("poczta_nadania_lista.csv", "r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        rows.append(row)
assert(rows[-1][0] == recipient)
assert(rows[-1][1] == content)
assert(rows[-1][2] == "13 knut")
assert(rows[-1][3] == "TAK")

# Task 8
poczta_wyslij_sowy("poczta_nadania_lista.csv")
from main import licz_sume

# Task 3
dane = {
    "galeon" : [1, 3, 5],
    "sykl" : [18, 20, 10],
    "knut" : [30, 40, 7]
}


assert(licz_sume(dane)) == {
    "galeon" : 12,
    "sykl" : 0,
    "knut" : 14
}

print(licz_sume(dane))

# Task 2
#Test funkcji wyslij_sowe czy sowa doleciała lub niedoleciała
doleciala = True
niedoleciala = False
wynik_lotu = wyslij_sowe('Hagrid','Pozdrowienia.')
assert wynik_lotu == doleciala or wynik_lotu == niedoleciala, "Sowa nie została wysłana."


#Test funkcji wyslij_sowe ile razy sowa doleciała
print ('Rozpoczyna się test skuteczności sowy, trwa on 100 sekund')
doloty = 0
i = 0
while i < 100:
    pojedynczy_wynik = wyslij_sowe('Hagrid','Pozdrowienia.')
    i += 1

    if pojedynczy_wynik == True:
        doloty += 1
    else:
        doloty += 0

assert doloty >= 80 and doloty <= 90, "Skuteczność sowy odstaje od normy powyżej 5%."