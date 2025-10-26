import numpy as np
import cv2 as cv
def dylatacja(obraz,filtr):

    h,w = obraz.shape[:2]
    filtr_h,filtr_w = filtr.shape
    ramka_h,ramka_w = filtr_h//2,filtr_w//2

    if len(obraz.shape) ==3:
        obraz = cv.cvtColor(obraz, cv.COLOR_BGR2GRAY)

    ramka = np.pad(obraz, ((ramka_h, ramka_h), (ramka_w, ramka_w)), mode='constant', constant_values=0)

    koniec = np.zeros_like(obraz)

    # obraz kolorowy:
    for i in range(h):
        for j in range(w):

            region = ramka[i:i + filtr_h, j:j + filtr_w]
            max_val = 0

            # uwzglednienie wag dla gaussa
            for si in range(filtr_h):
                for sj in range(filtr_w):
                    val = region[si, sj] * filtr[si, sj]
                    max_val = max(max_val, val)

            koniec[i, j] = int(np.clip(max_val, 0, 255))


    return koniec

