import sys
import numpy as np
import cv2

src = cv2.imread('rose.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

src_f = src_ycrcb[:, :, 0].astype(np.float32) # 밝기부분
blr = cv2.GaussianBlur(src_f, (0, 0), 2.0) # 실수형태로 처리한 후 
src_ycrcb[:, :, 0] = np.clip(2. * src_f - blr, 0, 255).astype(np.uint8) # 마지막 출력부분에서만 int타입으로 바꿔주는게 나음

dst = cv2.cvtColor(src_ycrcb, cv2.COLOR_YCrCb2BGR)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
