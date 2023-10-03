import sys
import numpy as np
import cv2


src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# kernel = np.array([
#     [-1,0,1],
#     [-2,0,2],
#     [-1,0,1]],
#     dtype=np.float32)

# dx = cv2.filter2D(src, -1, kernel, delta = 128)


dx = cv2.Sobel(src, -1, 1, 0, delta=128)
dy = cv2.Sobel(src, -1, 0, 1, delta=128)

# 소벨핉를 이용한 미분함수
# cv2.Sobel(src, ddepth, dx, dy, dst=None, ksize=None, scale=None,delta=None, borderType=None) -> dst
# src - 입력영상
# ddepth - 출력영상 데이터타입 -1이면 입력영상과 같은 데이터타입을 사용
# dx - x방향 미분차수
# dy - y방향 미분차수
# dst - 출력영상(행렬)
# ksize - 커널크기 기본값은 3
# scale - 연산결과에 추가적으로 곱할 값 기본값은 1
# delta - 연산결과에 추가적으로 더할 값 기본값은 0
# borderType - 가장자리 픽셀확장방식 기본값은 cv2.BORDER_DEFAULT
# 대부분 dx = 1 dy= 0 ksize = 3또는 dx = 0 dy = 1 ksize = 3으로 지정
cv2.imshow('src', src)
cv2.imshow('dx', dx)
cv2.imshow('dy', dy)
cv2.waitKey()

cv2.destroyAllWindows()
