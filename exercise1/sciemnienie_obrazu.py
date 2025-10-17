from dis import RETURN_CONST

import cv2 as cv
def sciemnienie_obrazu(nazwa,procent,opcja):

    if(procent <1 or procent >100):
        print("\n\nWPROWADZ PROCENT Z PRZEDZIAŁU (0-100)!\n")
        return 0

    if(opcja == "sciemnianie"):
        alpha = 1 - (procent/100)
        sciemnieniony = cv.imread(nazwa)
        sciemnieniony = cv.convertScaleAbs(sciemnieniony, alpha=alpha,beta=0)
        print(f"SCIEMNIONO OBRAZ O {procent} PROCENT!")
        return sciemnieniony

    elif (opcja == "rozjasnianie"):
        alpha = 1 + (procent / 100)
        rozjasniony = cv.imread(nazwa)
        rozjasniony = cv.convertScaleAbs(rozjasniony, alpha=alpha, beta=0)
        print(f"ROZJASNIONO OBRAZ O {procent} PROCENT!")
        return rozjasniony

    print("BŁĄD!!!")
    return 0
