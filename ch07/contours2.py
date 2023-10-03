import sys
import random
import numpy as np
import cv2


src = cv2.imread('milkdrop.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

_, src_bin = cv2.threshold(src, 0, 255, cv2.THRESH_OTSU)

contours, _ = cv2.findContours(src_bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

h, w = src.shape[:2]
dst = np.zeros((h, w, 3), np.uint8)

for i in range(len(contours)): # 객체의 갯수
    c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    cv2.drawContours(dst, contours, i, c, 1, cv2.LINE_AA)
# 외곽선 그리기
# cv2.drawContours(image, contours, contourIdx, color, thickness=None,lineType=None, hierarchy=None, maxLevel=None, offset=None)-> image
# image - 입출력영상
# contours - (cv2.findContours() 함수로 구한) 외곽선 좌표 정
# contourdx - 외곽선 인덱스. 음수(-1)를 지정하면 모든 외곽선을 그린다.
# color - 외곽선 색상
# thickness - 외곽선 두께 thinkness < 0이면 내부를 채운다.
# lineType - LINE_4, LINE_8, LINE_AA 중 하나 지정
# hierarchy - 외곽선 계층 정보.
# maxLevel - 그리기를 수행할 최대 외곽선 레벨. maxLevel = 0 이면 contourIdx로 지정된 외곽선만 그린다.
cv2.imshow('src', src)
cv2.imshow('src_bin', src_bin)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
