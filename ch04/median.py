import sys
import numpy as np
import cv2

src = cv2.imread('noise.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# 잡음제거필터
# cv2.medianBlur(src, ksize, dst=None) -> dst
# src - 입력영상
# ksize - 커널크기/ 1보다 큰 홀수를 지정
# dst - 출력영상/ src와 같은크기 타입
dst = cv2.medianBlur(src, 3)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
