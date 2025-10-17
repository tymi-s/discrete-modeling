import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
from sciemnienie_obrazu import *
from wyswietl import *
############################################################SKALA SZAROŚCI 1:
obraz1  =cv.imread('obraz.png')

#konwersja do szarości:
obraz_szary = cv.cvtColor(obraz1,cv.COLOR_BGR2GRAY)




#wyświetlenie:
wyswietl_i_zapisz(obraz_szary,"SZARY1","szary1.png",0)



############################################################SKALA SZAROŚCI 2:

obraz2 = cv.imread('obraz.png')
B,G,R = cv.split(obraz2) # czyli podzial obrazu na trzy

szary = 0.299 * R + 0.587 * G + 0.114 * B
szary = szary.astype(np.uint8)

wyswietl_i_zapisz(szary,"SZARY2","szary2.png",0)

############################################################ CZERWONY:

split = cv.imread('obraz.png')
B,G,R = cv.split(split)

red =1 * R + 0 * G + 0* B
red = red.astype(np.uint8)


# czarne kanały dla B i G
zeros = np.zeros_like(red)

#obraz RGB, gdzie tylko R ma wartości
red_img = cv.merge([zeros, zeros, red])

wyswietl_i_zapisz(red_img,"RED","red.png",0)


wyswietl_i_zapisz(obraz1,"ORYGINAL","sciemniony.png",0)
############################################################ SCIEMNIANIE:

procent1 = 50
sciemniony = sciemnienie_obrazu('obraz.png',procent1,"sciemnianie")
wyswietl_i_zapisz(sciemniony,"SCIEMNIONY","sciemniony.png",0)



############################################################ ROZJAŚNIANIE:

procent2 = 10
inc = 0
for i in range(5):
    rozjasniony = sciemnienie_obrazu('obraz.png', procent2+inc, "rozjasnianie")
    wyswietl_i_zapisz(rozjasniony,"SERIA ROZJASNIANIA","sciemniony.png",0)
    inc = inc +10


cv.destroyAllWindows()