import sys
import numpy as np
import cv2

def getGrayHistImage(hist):
    imgHist = np.full((100, 256), 255, dtype=np.uint8)

    histMax = np.max(hist)
    for x in range(256):
        pt1 = (x, 100)
        pt2 = (x, 100 - int(hist[x, 0] * 100 / histMax))
        cv2.line(imgHist, pt1, pt2, 0)

    return imgHist



src = cv2.imread('Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

gmin, gmax, _, _ = cv2.minMaxLoc(src)

# 정규화함수 - 히스토그램 스트레칭효과
dst = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX)
# dst = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX, dtype = np.uint8) 컬러영상에서 그레이스케일로 출력하고 싶을 경우

# numpy로 계산하는 방법
# dst = ((src - gmin) * 255. / (gmax - gmin)).astype(np.uint8)
# cv2.normalize(src, dst, alpha=None, beta=None, norm_type=None, dtype=None,mask=None) -> dst
# src - 입력영상
# dst - 출력영상 None 주면 됨 
# alpha - 원소값 범위 정규화인 경우 최솟값/ 노름정규화인경우 목표노름값
# beta - 원소값 범위 정규화인 경우 최댓값
# norm_type - 정규화 타입 NORM_INF, NORM_L1, NORM_L2, NORM_MINMAX.
# dtype - 출력영상의 타입
# mask - 마스크영상

hist = cv2.calcHist([src], [0], None, [256], [0, 256])
histImg = getGrayHistImage(hist)
hist2 = cv2.calcHist([dst], [0], None, [256], [0, 256])
histImg2 = getGrayHistImage(hist2)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('histImg', histImg)
cv2.imshow('histImg2', histImg2)
cv2.waitKey()

cv2.destroyAllWindows()
