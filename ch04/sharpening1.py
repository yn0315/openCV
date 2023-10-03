import sys
import numpy as np
import cv2

src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

blr = cv2.GaussianBlur(src, (0, 0), 2)
# dst = cv2.subtract(src,blr) # 원본영상에서 블러처리영상 빼기

# subtract로 사용하면 마이너스부분 다 0으로 처리해서 마이너스부분을 보기위해 addWeighted사용
# dst = cv2.addWeighted(src,1,blr,-1,128) 


dst = np.clip(2.0*src - blr, 0, 255).astype(np.uint8)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
