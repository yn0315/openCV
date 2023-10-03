import sys
import math
import numpy as np
import cv2


src = cv2.imread('tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

rad = 20 * math.pi / 180 # 반시계방향으로 20도를 radian단위로 바꾼것/ 시계방향은 음수로
aff = np.array([[math.cos(rad), math.sin(rad), 0],
                [-math.sin(rad), math.cos(rad), 0]], dtype=np.float32)

dst = cv2.warpAffine(src, aff, (0, 0))
# 영상의 어파인 변환함수
# cv2.warpAffine(src, M, dsize, dst=None, flags=None,borderMode=None, borderValue=None) -> dst
# src - 입력영상
# M - 2x3 어파인 변환행렬 실수형
# dsize - 결과영상크기(w,h)튜플, (0,0)이면 src와 같은 크기로 설정
# dst - 출력영상
# flags - 보간법 기본값은 cv2.INTER_LINEAR
# borderMode - 가장자리픽셀확장방식 기본값 cv2.BORDER_CONSTANT
# borderValue - cv2.BORDER_CONSTANT일때 사용할 상수값/ 기본값은 0

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
