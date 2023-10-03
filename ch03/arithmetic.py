import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt


src1 = cv2.imread('lenna256.bmp', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('square.bmp', cv2.IMREAD_GRAYSCALE)

if src1 is None or src2 is None:
    print('Image load failed!')
    sys.exit()

# 덧셈연산
dst1 = cv2.add(src1, src2, dtype=cv2.CV_8U)

# 가중치합 - 결과영상의 픽셀값이 특정 범위 안에 들어올 수 있게끔함
# cv2.addWeighted(src1, alpha, src2, beta, gamma, dst=None, dtype=None) -> dst
# src1 - 첫번째 영상
# alpha - 첫번째 영상 가중치
# src2 - 두번째 영상/ 첫번째영상과 같은크기, 같은타입
# beta - 두번째 영상 가중치
# gamma - 결과 영상에 추가적으로 더할 값
# dst - 가중치 합 결과 영상
# dtype - 출력영상(dst)의 타입
dst2 = cv2.addWeighted(src1, 0.5, src2, 0.5, 0.0)
#                           실수1   +   실수2 = 1이면 255를 초과하는 값이 발생하지 않음

# 뺄셈연산 - 순서중요
dst3 = cv2.subtract(src1, src2)

# 차이연산 - 절대값을 사용하여 결과가 마이너스가 나올 수 없음/ 변화가 있는 부분을 찾고자 할 때 사용
dst4 = cv2.absdiff(src1, src2)

plt.subplot(231), plt.axis('off'), plt.imshow(src1, 'gray'), plt.title('src1')
plt.subplot(232), plt.axis('off'), plt.imshow(src2, 'gray'), plt.title('src2')
plt.subplot(233), plt.axis('off'), plt.imshow(dst1, 'gray'), plt.title('add')
plt.subplot(234), plt.axis('off'), plt.imshow(dst2, 'gray'), plt.title('addWeighted')
plt.subplot(235), plt.axis('off'), plt.imshow(dst3, 'gray'), plt.title('subtract')
plt.subplot(236), plt.axis('off'), plt.imshow(dst4, 'gray'), plt.title('absdiff')

plt.show()
