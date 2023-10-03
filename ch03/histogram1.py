import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2

# 히스토그램 - 영상의 픽셀값의 분포를 그래프형태로 나타냄
# 그레이스케일 영상의 히스토그램
src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

hist = cv2.calcHist([src], [0], None, [256], [0, 256])
# 히스토그램 구하기
# cv2.calcHist(images, channels, mask, histSize, ranges, hist=None,accumulate=None) -> hist
# images - 입력영상리스트 / 하나의 영상일 경우에도 리스트로 묶어서 보내야함
# channels - 히스토그램을 구할 채널을 나타내는 리스트
# mask - 마스크영상, 입력 영상전체에서 히스토그램을 구하려면 None 지정
# histSize - 히스토그램 각 차원의 크기(빈의 개수)를 나타내는 리스트
# ranges - 히스토그램 각 차원의 최솟값과 최댓값으로 구성된 리스트
# hist - 계산된 히스토그램(numpy.ndarray)
# accumulate - 기존의 hist히스토그램에 누적하려면 True, 새로 만들려면 False
cv2.imshow('src', src)
cv2.waitKey(1)

plt.plot(hist)
plt.show()

# 컬러 영상의 히스토그램
src = cv2.imread('lenna.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

colors = ['b', 'g', 'r']
bgr_planes = cv2.split(src)

for (p, c) in zip(bgr_planes, colors):
    hist = cv2.calcHist([p], [0], None, [256], [0, 256])
    plt.plot(hist, color=c)

cv2.imshow('src', src)
cv2.waitKey(1)

plt.show()

cv2.destroyAllWindows()
