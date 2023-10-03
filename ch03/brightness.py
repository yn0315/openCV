import sys
import numpy as np
import cv2

# 영상의 밝기조절
# cv2.add(src1, src2, dst=None, mask=None, dtype=None) -> dst
# src1 - 첫번째 영상 또는 스칼라(입력)
# src2 - 두번째 영상 또는 스칼라(입력)
# dst - 덧셈연산의 결과영상(출력)
# mask - 마스크영상
# dtype - 출력영상의 타입(cv2.CV_8U, cv2.CV_32F등)
# dst를 함수 인자로 전달하려면 dst의 크기가 src1,src2와 같아야하며 타입이 적절해야함



# 그레이스케일 영상 불러오기
src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.add(src, 100)
#dst = np.clip(src + 100., 0, 255).astype(np.uint8) # 위의 add함수와 같은 것

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

# 컬러 영상 불러오기
src = cv2.imread('lenna.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.add(src, (100, 100, 100, 0))
#                   (b,g,r,alpa)
#dst = np.clip(src + 100., 0, 255).astype(np.uint8)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
