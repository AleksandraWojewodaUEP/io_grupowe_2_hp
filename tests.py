from main import waluta_dict_na_str

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

assert(waluta_dict_na_str(currencies1) == "13 knut")
assert(waluta_dict_na_str(currencies2) == "13 galeon 2 sykl 13 knut")