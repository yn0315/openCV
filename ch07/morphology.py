import sys
import numpy as np
import cv2


src = cv2.imread('circuit.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

se = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 3))
# 모폴로지 구조요소(커널)생성
# cv2.getStructuringElement(shape, ksize, anchor=None) -> retval
# shape - 구조요소 모양을 나타내는 플래그
#         cv2.MORPH_RECT - 사각형모양
#         cv2.MORPH_CROSS - 십자가 모양
#         cv2.MORPH_ELLIPSE - 사각형에 내접하는 타원
# ksize - 구조요소크기 / (width, height) 튜플.
# anchor - MORPH_CROSS 모양의 구조 요소에서 고정점 좌표
#          (-1, -1)을 지정하면 구조 요소의 중앙을 고정점으로 사용.
# retval - 0과 1로 구성된 cv2.CV_8UC1 타입 행렬. numpy.ndarray.
#          (1의 위치가 구조 요소 모양을 결정.)

dst1 = cv2.erode(src, se)
# 모폴로지 침식연산
# cv2.erode(src, kernel, dst=None, anchor=None, iterations=None,borderType=None, borderValue=None) -> dst
# src - 입력영상
# kernel - 구조요소 getStructuringElement() 함수에 의해 생성 가능
#          만약 None을 지정하면 3x3 사각형 구성 요소를 사용
# dst - 출력영상 src와 동일한 크기와 타입
# anchor - 고정점 위치 기본값(-1,-1)을 사용하면 중앙점을 사용
# iterations - 반복횟수 기본값은 1
# borderType - 가장자리 픽셀확장방식 / 기본값은 cv2.BORDER_CONSTANT
# borderValue - cv2.BORDER_CONSTANT인 경우, 확장된 가장자리 픽셀을 채울 값.

dst2 = cv2.dilate(src, None)

# 모폴로지 팽창연산
# cv2.dilate(src, kernel, dst=None, anchor=None, iterations=None,borderType=None, borderValue=None) -> dst
# src - 입력영상
# kernel - 구조 요소. getStructuringElement() 함수에 의해 생성 가능
#          만약 None을 지정하면 3x3 사각형 구성 요소를 사용.
# dst - 출력영상 src와 동일한 크기와 타입
# anchor - 고정점 위치 기본값(-1,-1)을 사용하면 중앙점을 사용
# iterations - 반복횟수 기본값은 1
# borderType - 가장자리 픽셀확장방식 / 기본값은 cv2.BORDER_CONSTANT
# borderValue - cv2.BORDER_CONSTANT인 경우, 확장된 가장자리 픽셀을 채울 값.


cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()
