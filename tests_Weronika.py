from main import wyslij_sowe

def testuj_wysylanie_sowy():

    true_count = 0
    false_count = 0
    error_margin = 0.05
    num_tests = 100

    for _ in range(num_tests):
        if wyslij_sowe("Adresat", "Treść"):
            true_count += 1
        else:
            false_count += 1

    success_rate = true_count / num_tests

    print(f'success_rate: {success_rate}')

    if (0.85 - error_margin) <= success_rate <= (0.85 + error_margin):
        return "Funkcja działa poprawnie"
    else:
        return "Funkcja niepoprawna"

assert(testuj_wysylanie_sowy() == "Funkcja działa poprawnie")