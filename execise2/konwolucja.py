import numpy as np
import cv2 as cv
def konwolucja(obraz, filtr):
    h, w = obraz.shape[:2]
    filtr_h, filtr_w = filtr.shape
    ramka_h, ramka_w = filtr_h // 2, filtr_w // 2

    if len(obraz.shape) == 3:
        obraz = cv.cvtColor(obraz, cv.COLOR_BGR2GRAY)


    obraz = obraz.astype(np.float32)

    ramka = np.pad(obraz, ((ramka_h, ramka_h), (ramka_w, ramka_w)),
                   mode='edge')

    koniec = np.zeros((h, w), dtype=np.float32)

    for i in range(h):
        for j in range(w):
            region = ramka[i:i + filtr_h, j:j + filtr_w]
            #suma iloczynów
            wartosc = np.sum(region * filtr)
            koniec[i, j] = wartosc

    # highpass
    koniec = koniec + 128
    koniec = np.clip(koniec, 0, 255)

    return koniec.astype(np.uint8)