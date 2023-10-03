import sys
import numpy as np
import cv2

src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

cv2.imshow('src', src)

for ksize in (3, 5, 7): # 변수에 순서대로 3, 5, 7을 할당하여 실행하라
    dst = cv2.blur(src, (ksize, ksize))
    # 평균값 필터링 함수
    # cv2.blur(src, ksize, dst=None, anchor=None, borderType=None) -> dst
    # src - 입력영상
    # ksize - 평균값필터크기(width, height)형태의 튜플
    # dst - 결과영상/ 입력영상과 같은 크기 & 타입

    desc = 'Mean: {}x{}'.format(ksize, ksize)
    cv2.putText(dst, desc, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                1.0, 255, 1, cv2.LINE_AA)

    cv2.imshow('dst', dst)
    cv2.waitKey() # 키를 누르면 다음 값으로 넘어감

cv2.destroyAllWindows()
