import cv2 as cv

def wyswietl_i_zapisz(obraz, tytul, nazwa_do_zapisu, wait):
    cv.imwrite(nazwa_do_zapisu, obraz)
    cv.imshow(tytul, obraz)
    cv.waitKey(wait)