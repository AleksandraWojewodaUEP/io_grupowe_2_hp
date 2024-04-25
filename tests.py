from main import licz_sume

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