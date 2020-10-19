# author:Hongkun Xu 
# datetime:2020/03/10 15:11
# software: PyCharm
"""
説明：　图片美化
"""
import cv2
import numpy as np


def beautify(img):
    # 显示原始图片
    cv2.namedWindow("Original", cv2.WINDOW_KEEPRATIO | cv2.WINDOW_NORMAL)
    cv2.imshow("Original", img)

    # hsv图片
    # hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 灰度图片
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 二值化
    ret, result = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)

    # 显示结果图片
    cv2.namedWindow("Result", cv2.WINDOW_KEEPRATIO | cv2.WINDOW_NORMAL)
    cv2.imshow('Result', result)

    # # 黑色范围
    # lower_black = np.array([120, 120, 120], dtype=np.uint8)
    # upper_black = np.array([255, 255, 255], dtype=np.uint8)
    #
    # # 查找黑色
    # mask = cv2.inRange(img, lower_black, upper_black)
    #
    # # 遮罩
    # res = cv2.bitwise_and(img, img, mask=mask)
    #
    # cv2.namedWindow("res", cv2.WINDOW_KEEPRATIO | cv2.WINDOW_NORMAL)
    # cv2.imshow('res', res)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    FILE_PATH = "Evenlight.jpg"
    img = cv2.imread(FILE_PATH)
    beautify(img)
