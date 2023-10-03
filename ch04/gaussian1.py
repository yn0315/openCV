import sys
import numpy as np
import cv2


src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

dst = cv2.GaussianBlur(src, (0, 0), 3)
# 가우시안 필터링 함수
# cv2.GaussianBlur(src, ksize, sigmaX, dst=None, sigmaY=None,borderType=None) -> dst
# src - 입력영상/ 각 채널별로 처리됨
# dst - 출력영상/ src와 같은 크기 타입
# ksize - 가우시안커널크기 (0,0)을 지정하면 sigma값에 의해 자동결정됨
# sigmaX - x방향 sigma
# sigmaY - y방향 sigma 0이면 sigmaX와 같게 설정
# borderType - 가장자리픽셀 확장방식
dst2 = cv2.blur(src, (7, 7))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.waitKey()

cv2.destroyAllWindows()
