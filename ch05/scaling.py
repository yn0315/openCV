import sys
import numpy as np
import cv2


src = cv2.imread('rose.bmp') # src.shape=(320, 480)

if src is None:
    print('Image load failed!')
    sys.exit()

dst1 = cv2.resize(src, (0, 0), fx=4, fy=4, interpolation=cv2.INTER_NEAREST)
dst2 = cv2.resize(src, (1920, 1280))  # cv2.INTER_LINEAR
dst3 = cv2.resize(src, (1920, 1280), interpolation=cv2.INTER_CUBIC)
dst4 = cv2.resize(src, (1920, 1280), interpolation=cv2.INTER_LANCZOS4)

# 영상의 크기변환
# cv2.resize(src, dsize, dst=None, fx=None, fy=None, interpolation=None) -> dst

# src - 입력영상
# dsize - 결과영상크기(w,h)튜플, (0,0)이면 fx와 fy값을 이용하여 결정
# dst - 출력영상
# fx,fy - x와 y방향 스케일비율(dsize값이 0일 때 유효)
# interpolation - 보간법지정/ 기본값은 cv2.INTER_LINEAR/중요/결과영상의 퀄리티

# 영상의 대칭변환
# cv2.flip(src, flipCode, dst=None) -> dst
# src - 입력영상
# flipCode - 대칭방향지정
#            양수(1) - 좌우대칭
#            0 - 상하대칭
#            음수(-1) 좌우&상하대칭
cv2.imshow('src', src)
cv2.imshow('dst1', dst1[500:900, 400:800])
cv2.imshow('dst2', dst2[500:900, 400:800])
cv2.imshow('dst3', dst3[500:900, 400:800])
cv2.imshow('dst4', dst4[500:900, 400:800])
cv2.waitKey()
cv2.destroyAllWindows()
