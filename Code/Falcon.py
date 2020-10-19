# author: Hongkun Xu
# datetime:2020/02/20 8:41
# software: PyCharm
"""
説明： 根据存折上的红色直线裁剪有效识别范围
"""

import cv2
import numpy as np
import copy
from pprint import pprint
from Tools import DetectPoints
from Evenlight import unevenLightCompensate


def imgeAdjustmentLightness(img):
    """
    功能: 增强图片中的红色部分

    Args:
        img: 图片对象

    Returns:　处理后的图片对象

    """
    B, G, R = cv2.split(img)
    b = copy.deepcopy(B)
    g = copy.deepcopy(G)
    r = copy.deepcopy(R)
    for row in range(len(r)):
        for col in range(len(r[row])):
            if r[row][col] > 230:
                r[row][col] = 255
    merged = cv2.merge([b, g, r])
    cv2.namedWindow("after adjust lightness", cv2.WINDOW_KEEPRATIO | cv2.WINDOW_NORMAL)
    cv2.imshow("after adjust lightness", merged)
    return merged

def CropPicture(FILE_PATH):
    """
    功能:　根据存折上下两条红线对图片进行裁剪
    条件: 1. 存折必须占据图片中的大部分位置，方向为不能过于倾斜
         2. 存折上下红线必须清晰明了，颜色在红色阈值范围内

    Args:
        FILE_PATH: 要裁剪的图像文件地址

    Returns:　None

    """
    # 红色阈值  ※ OpenCV里的HSV范围与标准的HSV范围不同
    lower_red_0 = np.array([0, 56, 50])
    upper_red_0 = np.array([10, 255, 255])
    lower_red_1 = np.array([150, 56, 50])
    upper_red_1 = np.array([179, 255, 255])

    # 载入图片
    img = cv2.imread(FILE_PATH)
    # img = imgeAdjustmentLightness(img)

    # 高斯模糊
    # 参数: 对象， 核， 标准差
    img = cv2.GaussianBlur(img, (5, 5), 1)

    # 显示原始图片
    cv2.namedWindow("Original", cv2.WINDOW_KEEPRATIO | cv2.WINDOW_NORMAL)
    cv2.imshow("Original", img)

    # HSV格式图像
    hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 检测红色部分
    mask_0 = cv2.inRange(hsv_image, lower_red_0, upper_red_0)
    mask_1 = cv2.inRange(hsv_image, lower_red_1, upper_red_1)

    # 合并两个mask
    th = cv2.bitwise_or(mask_0, mask_1)
    cv2.namedWindow("HSV image", cv2.WINDOW_KEEPRATIO | cv2.WINDOW_NORMAL)
    cv2.imshow("HSV image", th)

    # 反转灰度
    # gray_src = cv2.bitwise_not(gray)

    # 二值化处理
    binary_src = cv2.adaptiveThreshold(th, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, -2)

    # 显示二值化处理后图片
    cv2.namedWindow("result image", cv2.WINDOW_KEEPRATIO | cv2.WINDOW_NORMAL)
    cv2.imshow("result image", binary_src)

    # 提取垂直线
    # vline = cv2.getStructuringElement(cv2.MORPH_RECT, (1, (src.shape[0] / 16)), (-1, -1))

    # 一个5×5，元素值全为1的卷积核
    kernel = np.ones((5, 5), np.uint8)

    # 形态学变换
    # 第一个参数是待处理图像
    # 第二个参数是定义的卷积核
    # 第三个参数是膨胀次数，默认为1
    dilate = cv2.dilate(binary_src, kernel, iterations=2)
    ero = cv2.erode(dilate, kernel, iterations=1)
    dilate = cv2.dilate(ero, kernel, iterations=2)
    ero = cv2.erode(dilate, kernel, iterations=1)
    dilate = cv2.dilate(ero, kernel, iterations=2)
    ero = cv2.erode(dilate, kernel, iterations=3)
    dilate = cv2.dilate(ero, kernel, iterations=2)
    ero = cv2.erode(dilate, kernel, iterations=1)
    dilate = cv2.dilate(ero, kernel, iterations=2)
    ero = cv2.erode(dilate, kernel, iterations=1)
    dilate = cv2.dilate(ero, kernel, iterations=2)
    ero = cv2.erode(dilate, kernel, iterations=1)
    dilate = cv2.dilate(ero, kernel, iterations=5)
    ero = cv2.erode(dilate, kernel, iterations=1)
    dilate = cv2.dilate(ero, kernel, iterations=1)

    # 内置函数腐蚀和膨胀，第二个参数指定的是操作类型
    # opening = cv2.morphologyEx(binary_src, cv2.MORPH_OPEN, kernel)

    # 显示形态学变换后的图片
    cv2.namedWindow("opening", cv2.WINDOW_KEEPRATIO | cv2.WINDOW_NORMAL)
    cv2.imshow('opening', dilate)

    # 提取水平线
    hline = cv2.getStructuringElement(cv2.MORPH_RECT, ((dilate.shape[1] // 8), 2), (-1, -1))
    dst = cv2.morphologyEx(dilate, cv2.MORPH_OPEN, hline)

    # 四个基准点
    LeftTop, RightTop, LeftBottom, RightBottom = DetectPoints(dst)
    # DetectPoints(dst)

    # 验证裁剪范围用图像
    dst = cv2.bitwise_not(dst)
    cv2.namedWindow("CheckResult", cv2.WINDOW_KEEPRATIO | cv2.WINDOW_NORMAL)
    cv2.imshow('CheckResult', dst)
    cv2.imwrite("CheckResult.jpg", dst)

    # 图像长度和宽度
    height = dst.shape[0]
    width = dst.shape[1]
    print(height, width)

    #################################### 方案A: 透视变换 #####################################
    # ※比较危险，一旦四个顶点计算出错则前功尽弃
    # [(y1, x1),(y2, x2),(y3, x3),(y4, x4)]

    # 画面中的四个顶点坐标
    pts1 = np.float32([[201, 503], [2844, 444],  [108, 3437],  [3010, 3353]])
    pts1 = np.float32([[LeftTop, RightTop, LeftBottom, RightBottom]])
    # 新的坐标
    pts2 = np.float32([[0, 0], [height, 0], [0, width],  [height, width]])
    # 生成变换矩阵
    M = cv2.getPerspectiveTransform(pts1, pts2)
    # 透视变换
    perspective = cv2.warpPerspective(img, M, (height, width))
    # 显示透视变换后的图片
    cv2.namedWindow("perspective", cv2.WINDOW_KEEPRATIO | cv2.WINDOW_NORMAL)
    cv2.imshow('perspective', perspective)

    ################################## 方案B: 裁剪长方形区域 ###################################
    # ※比较安全，但裁剪区域内可能有倾斜，为之后的图像识别和数据读取带来很大误差

    # # 裁剪坐标为[y0:y1, x0:x1]
    # PADDING = 0
    # cropped = img[MinStartLine - PADDING:MaxFinishLine + PADDING, StartCol - PADDING:FinishCol + PADDING]
    # cropped = img[444:3437, 108:3010]
    # # 显示裁剪后的图片
    # cv2.namedWindow("cropped", cv2.WINDOW_KEEPRATIO | cv2.WINDOW_NORMAL)
    # cv2.imshow('cropped', cropped)

    # 图像后期处理
    # TODO 图像平滑: 去除背景中的噪点

    # 文本增强
    blur_img = cv2.GaussianBlur(perspective, (0, 0), 5)
    TextEnhancement = cv2.addWeighted(perspective, 1.5, blur_img, -0.5, 0)

    # 拉伸图片
    Stretch = cv2.resize(TextEnhancement, dsize=None, fx=1, fy=1.2)
    cv2.namedWindow("Stretch", cv2.WINDOW_KEEPRATIO | cv2.WINDOW_NORMAL)
    cv2.imshow('Stretch', Stretch)

    # 灰度图像
    # gray = cv2.cvtColor(Stretch, cv2.COLOR_BGR2GRAY)
    # cv2.namedWindow("gray", cv2.WINDOW_KEEPRATIO | cv2.WINDOW_NORMAL)
    # cv2.imshow('gray', gray)

    # 设定阈值
    # threshold = 120

    # 设置块大小
    blockSize = 196

    # 均匀光照
    EvenLight = unevenLightCompensate(Stretch, blockSize)
    cv2.namedWindow("EvenLight", cv2.WINDOW_KEEPRATIO | cv2.WINDOW_NORMAL)
    cv2.imshow('EvenLight', EvenLight)

    # 灰度图片
    EvenLightgray = cv2.cvtColor(EvenLight, cv2.COLOR_BGR2GRAY)

    # 二值化
    ret, result = cv2.threshold(EvenLightgray, 0, 255, cv2.THRESH_OTSU)

    # 显示结果图片
    cv2.namedWindow("Result", cv2.WINDOW_KEEPRATIO | cv2.WINDOW_NORMAL)
    cv2.imshow('Result', result)

    # cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 写入裁剪后的图片
    cv2.imwrite("result.jpg", Stretch)
    return result


if __name__ == "__main__":

    # 文件路径
    # FILE_PATH = "test4.jpg"
    FILE_PATH = "test2.jpg"
    CropPicture(FILE_PATH)


