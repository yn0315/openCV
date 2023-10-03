import sys
import numpy as np
import cv2


src = cv2.imread('cells.png', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

_, dst1 = cv2.threshold(src, 100, 255, cv2.THRESH_BINARY)
_, dst2 = cv2.threshold(src, 210, 255, cv2.THRESH_BINARY)

# 영상의 이진화
# 임계값함수
# cv2.threshold(src, thresh, maxval, type, dst=None) -> retval, dst 
# src - 입력영상, 다채널 8비트 또는 32비트 실수형
# thresh - 사용자 지정 임계값
# maxval - cv2.THRESH_BINARY 또는 cv2.THRESH_BINARY_INV 방법 사용 시 최댓값
#          보통 255로 지정
# type - cv2.THRESH_ 로 시작하는 플래그
#        임계값 함수 동작 지정 또는 자동 임계값 결정 방법 지정
# retval - 사용된 임계값
# dst - 출력 영상. src와 동일 크기, 동일 타입, 같은 채널 수


cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()
