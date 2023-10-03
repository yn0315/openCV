import sys
import numpy as np
import cv2


img_names = ['img1.jpg', 'img2.jpg', 'img3.jpg']

imgs = []
for name in img_names:
    img = cv2.imread(name)

    if img is None:
        print('Image load failed!')
        sys.exit()

    imgs.append(img)

stitcher = cv2.Stitcher_create()
# 이미지 스티칭 객체생성
# cv2.Stitcher_create(, mode=None) -> retval
# mode - 스티칭 모드. cv2.PANORAMA 또는 cv2.SCANS 중 하나 선택.
#        기본값은 cv2.PANORAMA
# retval - cv2.Stitcher 클래스 객체

status, dst = stitcher.stitch(imgs)
# 이미지 스티칭 함수
# cv2.Stitcher.stitch(images, pano=None) -> retval, pano
# images - 입력 영상 리스트
# retval - 성공하면 cv2.Stitcher_OK.
# pano - 파노라마 영상

if status != cv2.Stitcher_OK:
    print('Stitch failed!')
    sys.exit()

cv2.imwrite('output.jpg', dst)

cv2.namedWindow('dst', cv2.WINDOW_NORMAL)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
