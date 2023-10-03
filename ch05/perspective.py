import sys
import numpy as np
import cv2


src = cv2.imread('namecard.jpg')

if src is None:
    print('Image load failed!')
    sys.exit()

w, h = 720, 400
srcQuad = np.array([[325, 307], [760, 369], [718, 611], [231, 515]], np.float32) # 시계방향으로 명함 꼭지점의 좌표들
dstQuad = np.array([[0, 0], [w-1, 0], [w-1, h-1], [0, h-1]], np.float32)

pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)

# 어파인 변환행렬 구하기
# cv2.getAffineTransform(src, dst) -> retval
# src - 3개의 원본좌표점(numpy.ndarray.shape =(3,2))
# dst - 3개의 결과좌표점(numpy.ndarray.shpe = (3,2))
# retval - 2x3 투시변환행렬

# 투시변환행렬구하기
# cv2.getPerspectiveTransform(src, dst, solveMethod=None) -> retval
# src - 4개의 원본좌표점(numpy.ndarray.shape = (4,2))
# dst - 4개의 결과좌표점(numpy.ndarray.shape = (4,2))
# retval - 3x3 투시변환행렬


dst = cv2.warpPerspective(src, pers, (w, h))
# 영상의 투시변환함수
# cv2.warpPerspective(src, M, dsize, dst=None, flags=None,borderMode=None, borderValue=None) -> dst
# src - 입력영상
# M - 3x3 투시변환행렬 실수형
# dsize - 결과영상크기 (w,h)튜플, (0,0)이면 src와 같은 크기로 설정
# dst - 출력영상
# flags - 보간법 기본값은 cv2.INTER_LINEAR
# borderMode - 가장자리 픽셀 확장 방식. 기본값은 cv2.BORDER_CONSTANT
# borderValue - cv2.BORDER_CONSTANT일 때 사용할 상수 값. 기본값은 0.

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
