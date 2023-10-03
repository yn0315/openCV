import sys
import numpy as np
import cv2


src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dx = cv2.Sobel(src, cv2.CV_32F, 1, 0)
dy = cv2.Sobel(src, cv2.CV_32F, 0, 1)

mag = cv2.magnitude(dx, dy) # 실수형태임
# 2d 벡터의 크기 계산함수
# cv2.magnitude(x, y)
# x - 2D 벡터의 x 좌표 행렬. 실수형
# y - 2D 벡터의 y 좌표 행렬. x와 같은 크기. 실수형

# 2d 벡터의 방향 계산함수
# cv2.phase(x, y, angle=None, angleInDegrees=None) -> angle
# x - 2D 벡터의 x 좌표 행렬. 실수형
# y - 2D 벡터의 y 좌표 행렬. x와 같은 크기. 실수형
# angle - 2D 벡터의 크기 행렬. x와 같은 크기, 같은 타입
#         angle(𝐼𝐼) = atan2(y 𝐼𝐼 , x 𝐼𝐼 )
#         만약 x(I)=y(I)=0이면 angle은 0으로 설정됨
# angleInDegrees - True이면 각도 단위, False이면 래디언 단위

mag = np.clip(mag, 0, 255).astype(np.uint8)

dst = np.zeros(src.shape[:2], np.uint8)
dst[mag > 120] = 255
#_, dst = cv2.threshold(mag, 120, 255, cv2.THRESH_BINARY)

cv2.imshow('src', src)
cv2.imshow('mag', mag)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
