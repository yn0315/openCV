import sys
import numpy as np
import cv2


# CrCb 살색 히스토그램 구하기
ref = cv2.imread('kids1.png', cv2.IMREAD_COLOR)
mask = cv2.imread('kids1_mask.bmp', cv2.IMREAD_GRAYSCALE)

if ref is None or mask is None:
    print('Image load failed!')
    sys.exit()

ref_ycrcb = cv2.cvtColor(ref, cv2.COLOR_BGR2YCrCb)

channels = [1, 2]
ranges = [0, 256, 0, 256]
hist = cv2.calcHist([ref_ycrcb], channels, mask, [128, 128], ranges)

hist_norm = cv2.normalize(cv2.log(hist + 1), None, 0, 255, 
                          cv2.NORM_MINMAX, cv2.CV_8U)

# 입력 영상에 히스토그램 역투영 적용
src = cv2.imread('kids2.png', cv2.IMREAD_COLOR)

if src is None:
    print('Image load failed!')
    sys.exit()

src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

backproj = cv2.calcBackProject([src_ycrcb], channels, hist, ranges, 1)
# 히스토그램 역투영함수
# cv2.calcBackProject(images, channels, hist, ranges, scale, dst=None) -> dst
# images - 입력영상리스트
# channels - 역투영 계산에 사용할 채널 번호 리스트
# hist - 입력 히스토그램(numpy.ndarray)
# ranges - 히스토그램 각 차원의 최솟값과 최댓값으로 구성된 리스트
# scale - 출력 역투영 행렬에 추가적으로 곱할 값/ 1 넣어주면 됨
# dst - 출력 역투영 영상, 입력영상과 동일크기 / cv2.CV_8U

cv2.imshow('src', src)
cv2.imshow('hist_norm', hist_norm)
cv2.imshow('backproj', backproj)
cv2.waitKey()
cv2.destroyAllWindows()
