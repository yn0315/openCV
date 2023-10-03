import sys
import numpy as np
import cv2


src = cv2.imread('building.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.Canny(src, 50, 150)
# 캐니 에지 검출함수
# cv2.Canny(image, threshold1, threshold2, edges=None, apertureSize=None,L2gradient=None) -> edges
# image - 입력영상
# threshold1 - 하단임계값
# threshold2 - 상단임계값 -> threshold1 : threshold2 = 1:2 또는 1:3
# edges - 에지영상
# apertureSize - 소벨연산을 위한 커널크기 기본값3
# L2gradient - True이면 L2 norm 사용, False이면 L1 norm 사용. 기본값은 False 
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
