import sys
import numpy as np
import cv2


src = cv2.imread('tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

aff = np.array([[1, 0, 200],
                [0, 1, 100]], dtype=np.float32)

# 영상의 어파인변환함수
# cv2.warpAffine(src, M, dsize, dst=None, flags=None, borderMode=None, borderValue=None) -> dst
# src - 입력영상
# M - 2x3 어파인 변환행렬 실수형
# dsize - 결과 영상 크기(w,h)튜플 (0,0)이면 src와 같은 크기로 설정
# dst - 출력영상
# flags - 보간법 기본값은 cv2.INTER_LINEAR
# borderMode - 가장자리 픽셀 확장방식 기본값은 cv2.BORDER_CONSTANT
# borderValue - cv2.BORDER_CONSTANT일 때 사용할 상수값 기본값은 0
dst = cv2.warpAffine(src, aff, (0, 0))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
