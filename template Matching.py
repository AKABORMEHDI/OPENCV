import numpy as np
import cv2

img = cv2.resize(cv2.imread('venv/the cars.jpg', 0), (0, 0), fx=0.8, fy=0.8)
template = cv2.resize(cv2.imread('venv/car.jpg', 0), (0, 0), fx=0.8, fy=0.8)
h, w = template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()

    result = cv2.matchTemplate(img2, template, method)#is going to help us to find the areas in our base img match with our template
    # img and than we can draw the rectangle
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]: #this two methods is to find the minimum location
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h)# w and h is dimonsion of our template img
    cv2.rectangle(img2, location, bottom_right, 225, 5)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()