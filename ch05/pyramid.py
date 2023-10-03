import sys
import numpy as np
import cv2


src = cv2.imread('cat.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()


rc = (250, 120, 200, 200)  # rectangle tuple

# 원본 영상에 그리기
cpy = src.copy()
cv2.rectangle(cpy, rc, (0, 0, 255), 2)
cv2.imshow('src', cpy)
cv2.waitKey()

# 피라미드 영상에 그리기
for i in range(1, 4):
    src = cv2.pyrDown(src)
    # 영상 피라미드 다운샘플링
    # cv2.pyrDown(src, dst=None, dstsize=None, borderType=None) -> dst
    # src - 입력영상
    # dst - 출력영상
    # dstsize - 출력영상크기/따로 지정하지 않으면 입력영상의 가로,세로크기의 1/2로 설정
    # borderType - 가장자리 픽셀 확장방식
    # 참고 - 먼저 5x5크기의 가우시안필터를 적용
    #        이후 짝수 행과 열을 제거하여 작은 크기의 영상을 생성

    # 영상 피라미드 업샘플링
    # cv2.pyrUp(src, dst=None, dstsize=None, borderType=None) -> dst
    # src - 입력영상
    # dst - 출력영상
    # dstsize - 출력영상크기/ 따로 지정하지 않으면 입력영상의 가로,세로크기의 2배설정
    # borderType - 가장자리 픽셀 확장방식
    cpy = src.copy()
    cv2.rectangle(cpy, rc, (0, 0, 255), 2, shift=i) # shift 축소값 /사용권장하진 않음
    cv2.imshow('src', cpy)
    cv2.waitKey()
    cv2.destroyWindow('src')

cv2.destroyAllWindows()
