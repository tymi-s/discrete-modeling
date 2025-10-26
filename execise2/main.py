import cv2 as cv
import numpy as np
from erozja import *
from dylatacja import *
from display_and_save import *
from tworzenie_obrazu_strukturalnego import *
from otwarcie import *
from domkniecie import *
from konwolucja import *
obraz = cv.imread("gauss.bmp")


############################################################################DYLATACJA
# filtr1= tworzenie_obrazu_strukturalnego(rozmiar=7,ksztalt="gauss")
# print(f"\ntak wyglada filtr1:\n{filtr1}")
#
# #2 przypadki modyfikacji gaussa
# gauss_wzmocniony1 =filtr1*2.0
# gauss_wzmocniony2 =filtr1*4.0
#
# print(f"\ntak wyglada filter gaussa wzmocniony1:\n{gauss_wzmocniony1}")
# print(f"\ntak wyglada filter gaussa wzmocniony1:\n{gauss_wzmocniony2}")
#
# dylatacja1 = dylatacja(obraz,filtr1)
# dylatacja2= dylatacja(obraz,gauss_wzmocniony1)
# dylatacja3 = dylatacja(obraz,gauss_wzmocniony2)
#
# display_and_save(dylatacja1,"dylatacja4.bmp","dylatacja1",0)
# display_and_save(dylatacja2,"dylatacja5.bmp","dylatacja2",0)
# display_and_save(dylatacja3,"dylatacja6.bmp","dylatacja3",0)



##############################################################################################EROZJA

# filtr2 = tworzenie_obrazu_strukturalnego(rozmiar=15,ksztalt="gauss")
# print(f"\ntak wyglada filtr2:\n{filtr2}")
# display_and_save(obraz,"erozja1.bmp","erozja",0)
# erozja1 = erozja(obraz,filtr2)


###########################################################################################OTWARCIE DOMKNIECIE:

# filtr3 = tworzenie_obrazu_strukturalnego(rozmiar = 7,ksztalt="kwadrat")
# otwarcie = otwarcie(obraz,filtr3)
# domkniecie=domkniecie(obraz,filtr3)
# display_and_save(otwarcie,"otwarcie.bmp","otwarcie",0)
# display_and_save(domkniecie,"domkniecie.bmp","domkniecie",0)



############################################################################OPERACJE MORFOLOGICZNE NA WLASNYM:
# obraz2 = cv.imread("ksiezyc.bmp")
#
# filtr4 = tworzenie_obrazu_strukturalnego(rozmiar = 7,ksztalt="krzyz")
# tmp1=erozja(obraz2,filtr4)
# tmp2=erozja(obraz2,filtr4)
# res1= dylatacja(obraz2,filtr4)
# display_and_save(res1,"sekwencja1.bmp","erozja,erozja,dylatacja",0)
#
# filtr5 = tworzenie_obrazu_strukturalnego(rozmiar = 8,ksztalt="kwadrat")
# tmp3=dylatacja(obraz2,filtr5)
# tmp4=erozja(obraz2,filtr5)
# res2= dylatacja(obraz2,filtr5)
# display_and_save(res2,"sekwencja2.bmp","dylatacja,erozja,dylatacja",0)
#
# filtr6 = tworzenie_obrazu_strukturalnego(rozmiar = 4,ksztalt="gauss")
# tmp5=erozja(obraz2,filtr6)
# tmp6=dylatacja(obraz2,filtr6)
# tmp7= dylatacja(obraz2,filtr6)
# res3= dylatacja(obraz2,filtr6)
# display_and_save(res3,"sekwencja3.bmp","erozja,dylatacja,dylatacja,erozja",0)

######################################################################################WŁASNY UPPERPASS:

filtr7 = tworzenie_obrazu_strukturalnego(rozmiar = 7,ksztalt="upperpass")
print(filtr7)
upper1=konwolucja(obraz,filtr7)
display_and_save(upper1,"upperpass_dylatacja.bmp","upperpass",0)
upper2= konwolucja(obraz,filtr7)
display_and_save(upper2 ,"upperpass_erozja.bmp","upperpass",0)














