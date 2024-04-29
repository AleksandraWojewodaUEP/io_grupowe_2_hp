from main import wyslij_sowe
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



