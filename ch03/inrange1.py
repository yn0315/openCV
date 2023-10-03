import sys
import numpy as np
import cv2


src = cv2.imread('candies.png')
#src = cv2.imread('candies2.png')

if src is None:
    print('Image load failed!')
    sys.exit()

src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

dst1 = cv2.inRange(src, (0, 128, 0), (100, 255, 100)) # bgr순서로 src, 하한값,상한값
dst2 = cv2.inRange(src_hsv, (50, 150, 0), (80, 255, 255))

# 특정 색상 영역 추출
# cv2.inRange(src, lowerb, upperb, dst=None) -> dst
# src- 입력행렬
# lowerb - 하한값행렬 또는 스칼라
# upperb - 상한값행렬 또는 스칼라
# dst - 입력영상과 같은 크기의 마스크 영상 (numpy.uint8)
#       범위 안에 들어가는 픽셀은 255, 나머지는 0으로 설정

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()

cv2.destroyAllWindows()
