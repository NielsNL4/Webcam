import cv2
import numpy as np

def show_webcam(mirror=False):
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()

        if mirror:
            img = cv2.flip(img, 1)

        blur = cv2.GaussianBlur(img, (5,5),10)
        canny = cv2.Canny(blur,40,150)
        cv2.imshow('my webcam', canny)
        if cv2.waitKey(1) == 27:
            break  # esc to quit
    cv2.destroyAllWindows()


def main():
    show_webcam(mirror=True)

def canny(image):
    blur = cv2.GaussianBlur(image, (5,5),0)
    canny = cv2.Canny(blur,200,250)
    return canny

if __name__ == '__main__':
    main()
