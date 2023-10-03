import sys
import numpy as np
import cv2


src = cv2.imread('tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

h, w = src.shape[:2]

map2, map1 = np.indices((h, w), dtype=np.float32) # 행렬의 x,y좌표값의 인덱스정보를 반환해줌
map2 = map2 + 10 * np.sin(map1 / 32)

dst = cv2.remap(src, map1, map2, cv2.INTER_CUBIC, borderMode=cv2.BORDER_DEFAULT)
# 리매핑 함수
# cv2.remap(src, map1, map2, interpolation, dst=None, borderMode=None,borderValue=None) -> dst
# src - 입력영상
# map1 - 결과영상의 (x,y)좌표가 참조할 입력영상의 x좌표
# map2 - 결과영상의 (x,y)좌표가 참조할 입력영상의 y좌표
# interpolation - 보간법
# dst - 출력영상

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
