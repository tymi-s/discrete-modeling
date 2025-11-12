ZIELONY = '\033[92m'
CZERWONY = '\033[91m'
RESET = '\033[0m'

def wyswietl_kolorowo(automat, numer_iteracji):
    kolorowy = ''.join([f"{ZIELONY}{x}{RESET}" if x == 1 else f"{CZERWONY}{x}{RESET}" for x in automat])
    print(f"automat po iteracji numer {numer_iteracji}: {kolorowy}")
