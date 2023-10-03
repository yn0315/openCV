import sys
import numpy as np
import cv2

src = cv2.imread('lenna.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

# 양방향 필터링 함수
dst = cv2.bilateralFilter(src, -1, 10, 5)
# cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace, dst=None,borderType=None) -> dst
# src - 입력영상 8비트 또는 실수형/ 1채널 또는 3채널
# d - 필터링에 사용될 이웃 픽셀의 거리(지름)
#     음수(-1)를 입력하면 sigmaSpace값에 의해 자동 결정됨/ 가급적이면 -1로
# sigmaColor - 색 공간에서 필터의 표준편차 / 엣지냐 아니냐를 판단하는 기준값
# sigmaSpace - 좌표공간에서 필터의 표준편차
# dst - 출력영상 src와 같은 크기, 같은 타입
# borderType - 가장자리 픽셀처리방식

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
