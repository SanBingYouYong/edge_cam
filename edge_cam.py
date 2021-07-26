import cv2 as cv
import numpy as np


def detect_canny_only(frame):
    image = np.copy(frame)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # blurred = cv.GaussianBlur(gray, (7, 7), 0)
    # ret, binary = cv.threshold(blurred, 200, 255, cv.THRESH_BINARY)
    # kernel = cv.getStructuringElement(cv.MORPH_RECT, (7, 7))
    # dilated = cv.dilate(binary, kernel)
    # eroded = cv.erode(dilated, kernel)
    # canny = cv.Canny(eroded, 50, 200)
    # cv.imshow("edges", canny)
    canny = cv.Canny(gray, 75, 255)
    cv.imshow("edges", canny)

def detect_canny_conts(frame):
    image = np.copy(frame)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # blurred = cv.GaussianBlur(gray, (7, 7), 0)
    # ret, binary = cv.threshold(gray, 150, 200, cv.THRESH_BINARY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    # dilated = cv.dilate(binary, kernel)
    # eroded = cv.erode(dilated, kernel)
    canny = cv.Canny(gray, 50, 200)
    dst = cv.bitwise_and(image, image, mask=canny)
    dilated = cv.dilate(dst, kernel)
    # cv.imshow("edges", canny)
    # contours, hierarchy = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    # cv.drawContours(image, contours, -1, (0, 0, 255), 1)
    cv.imshow("edges", dilated)

def read_cam():
    source = cv.VideoCapture(0)
    while True:
        ret, frame = source.read()
        if frame is None:
            cv.waitKey(0)
            break
        flag = cv.waitKey(1)
        # detect_canny_only(frame)
        detect_canny_conts(frame)
        if flag == 27:
            break
    source.release()
    cv.destroyAllWindows


if __name__ == "__main__":
    read_cam()