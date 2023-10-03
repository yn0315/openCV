import sys
import numpy as np
import cv2


src = cv2.imread('tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

cp = (src.shape[1] / 2, src.shape[0] / 2)
#       가로크기/2, 세로크기/2 의 점의 좌표
rot = cv2.getRotationMatrix2D(cp, 20, 0.5) # 센터포인트를 기준으로 회전
# 영상의 회전 변환 행렬 구하기
# cv2.getRotationMatrix2D(center, angle, scale) -> retval
# center - 회전중심좌표(x,y)튜플
# angle - (반시계방향) 회전각도(degree) 음수는 시계방향
# scale - 추가적인 확대비율
# retval - 2x3 어파인 변환행렬 실수형

dst = cv2.warpAffine(src, rot, (0, 0))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
