import time
import random

def wyslij_sowe(adresat, tresc):
    print(f"Twój list do {adresat} już leci!")
    time.sleep(1)
    if random.uniform(0,1) <= 0.85:
        return True
    else:
        return False

