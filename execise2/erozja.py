import numpy as np
import cv2 as cv
def erozja(obraz,filtr):

    h,w = obraz.shape[:2]
    filtr_h,filtr_w = filtr.shape
    ramka_h,ramka_w = filtr_h//2,filtr_w//2

    if len(obraz.shape) ==3:
        obraz = cv.cvtColor(obraz, cv.COLOR_BGR2GRAY)
    ramka = np.pad(obraz, ((ramka_h, ramka_h), (ramka_w, ramka_w)), mode='constant', constant_values=255)

    koniec = np.zeros_like(obraz)

    # obraz kolorowy:
    for i in range(h):
        for j in range(w):

            region = ramka[i:i + filtr_h, j:j + filtr_w]
            min_val = 255

            # uwzglednienie wag dla gaussa
            for si in range(filtr_h):
                for sj in range(filtr_w):
                    if filtr[si, sj] > 0:
                        val = region[si, sj] * filtr[si, sj]
                        min_val = min(min_val, val)

            koniec[i, j] = int(np.clip(min_val, 0, 255))


    return koniec

