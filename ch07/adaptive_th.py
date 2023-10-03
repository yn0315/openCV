import sys
import numpy as np
import cv2


src = cv2.imread('sudoku.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()


def on_trackbar(pos):
    bsize = pos
    if bsize % 2 == 0:
        bsize = bsize - 1
    if bsize < 3:
        bsize = 3

    dst = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                cv2.THRESH_BINARY, bsize, 5)

    cv2.imshow('dst', dst)


# openCV 적응형 이진화
# cv2.adaptiveThreshold(src, maxValue, adaptiveMethod,thresholdType, blockSize, C, dst=None) -> dst
# src - 입력영상 그레이스케일영상
# maxValue - 임계값 함수 최댓값 보통 255
# adaptiveMethod - 블록평균계산방법지정 cv2.ADAPTIVE_THRESH_MEAN_C는 산술평균
#                   cv2.ADAPTIVE_THRESH_GAUSSIAN_C는 가우시안 가중치 평균
# thresholdType - cv2.THRESH_BINARY 또는 cv2.THRESH_BINARY_INV 지정
# blockSize - 블록크기 3이상의 홀수
# C - 블록 내 평균값 또는 블록 내 가중 평균값에서 뺄 값.
#     (x, y) 픽셀의 임계값으로 𝑇 𝑥, 𝑦 = 𝜇𝐵 𝑥, 𝑦 − 𝐶 를 사용


cv2.imshow('src', src)
cv2.namedWindow('dst')
cv2.createTrackbar('Block Size', 'dst', 0, 200, on_trackbar)
cv2.setTrackbarPos('Block Size', 'dst', 11)

cv2.waitKey()
cv2.destroyAllWindows()
