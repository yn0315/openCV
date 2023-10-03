import sys
import random
import numpy as np
import cv2


src = cv2.imread('contours.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

contours, hier = cv2.findContours(src, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
# 외곽선 검출함수
# cv2.findContours(image, mode, method, contours=None, hierarchy=None,offset=None) -> contours, hierarchy
# image - 입력영상 non-zero픽셀을 객체로 간주함
# mode - 외곽선검출모드 cv2.RETR_로 시작하는 상수
# method - 외곽선 근사화 방법 . cv2.CHAIN_APPROX_로 시작하는 상수.
# contours - 검출된 외곽선 좌표  numpy.ndarray로 구성된 리스트
#            len(contours)=전체 외곽선 개수(N)
#            contours[i].shape=(K, 1, 2). contours[i].dtype=numpy.int32.
# hierarchy - 외곽선 계층 정보. numpy.ndarray. shape=(1, N, 4). dtype=numpy.int32
#             hierarchy[0, i, 0] ~ hierarchy[0, i, 3]이 순서대로 next, prev, child, parent
#             외곽선 인덱스를 가리킴. 해당 외곽선이 없으면 -1
# offset - 좌표 값 이동옵셋 기본값은 (0,0)

dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

idx = 0
while idx >= 0: 
    c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    cv2.drawContours(dst, contours, idx, c, 2, cv2.LINE_8, hier) # hier 안주면 바깥쪽 객체 외곽선만 그림
    idx = hier[0, idx, 0] # 첫번째거는 무조건 0 마지막은 0부터 3사이

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
