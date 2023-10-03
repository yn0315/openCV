import sys
import numpy as np
import cv2

# 비트맵 - 영상데이터를 메모리에 올리는 것
# 컬러 영상 불러오기
src = cv2.imread('candies.png', cv2.IMREAD_COLOR)

if src is None:
    print('Image load failed!')
    sys.exit()

# 컬러 영상 속성 확인
print('src.shape:', src.shape)  # src.shape: (480, 640, 3)
print('src.dtype:', src.dtype)  # src.dtype: uint8

# RGB 색 평면 분할
# 해당 색상부분이 밝게 나타남
b_plane, g_plane, r_plane = cv2.split(src)

#b_plane = src[:, :, 0]
#g_plane = src[:, :, 1]
#r_plane = src[:, :, 2]

# (색상) 채널분리
# cv2.split(m, mv=None) -> dst
# m - 다채널영상 bgr로 구성된 컬러영상
# mv - 출력영상
# dst - 출력영상의 리스트

# (색상) 채널결합
# cv2.merge(mv, dst=None) -> dst
# mv - 입력 영상 리스트 또는 튜플
# dst - 출력영상



cv2.imshow('src', src)
cv2.imshow('B_plane', b_plane)
cv2.imshow('G_plane', g_plane)
cv2.imshow('R_plane', r_plane)
cv2.waitKey()

cv2.destroyAllWindows()
