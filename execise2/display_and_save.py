import cv2 as cv
def display_and_save(obiekt,nazwa_do_zapisu,napis,wait):
    cv.imshow(napis,obiekt)
    cv.waitKey(wait)
    cv.imwrite(nazwa_do_zapisu,obiekt)
    cv.destroyAllWindows()
