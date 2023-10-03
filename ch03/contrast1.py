import sys
import numpy as np
import cv2


src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

alpha = 1.0 # 높을수록 대비효과 커짐
dst = np.clip((1+alpha)*src - 128*alpha, 0, 255).astype(np.uint8)
# np.clip((1+alpha)*src - 128*alpha, 0에서, 255사이).astype(np.uint8) # 실수형태이므로 astype(np.uint8)을 사용하여 정수형태로 변환
# np.clip - 0보다 작은 값은 0으로 255보다 큰값은 255로 변환해줌

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
