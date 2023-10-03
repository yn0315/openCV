import sys
import numpy as np
import cv2


# 입력 이미지 불러오기
src = cv2.imread('dial.jpg')

if src is None:
    print('Image open failed!')
    sys.exit()

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
blr = cv2.GaussianBlur(gray, (0, 0), 1.0)


def on_trackbar(pos):
    rmin = cv2.getTrackbarPos('minRadius', 'img')
    rmax = cv2.getTrackbarPos('maxRadius', 'img')
    th = cv2.getTrackbarPos('threshold', 'img')

    circles = cv2.HoughCircles(blr, cv2.HOUGH_GRADIENT, 1, 50,
                               param1=120, param2=th, minRadius=rmin, maxRadius=rmax)

    dst = src.copy()
    if circles is not None:
        for i in range(circles.shape[1]):
            cx, cy, radius = np.uint16(circles[0][i])
            cv2.circle(dst, (cx, cy), radius, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow('img', dst)

# 블러처리를 한번하고 원 검출하는 게 좋음
# 허프변환 원 검출함수
# cv2.HoughCircles(image, method, dp, minDist, circles=None, param1=None,param2=None, minRadius=None, maxRadius=None) -> circles
# image - 입력영상 /에지 아닌 일반영상
# method - openCV4.2이하에서는 는 cv2.HOUGH_GRADIENT만 지정 가능
# dp - 입력 영상과 축적 배열의 크기 비율. 1이면 동일 크기
#      2이면 축적 배열의 가로, 세로 크기가 입력 영상의 반
# minDist - 검출된 원 중심점들의 최소거리
# circles - (cx, cy, r) 정보를 담은 numpy.ndarray. shape=(1, N, 3), dtype=np.float32
# param1 - Canny 에지 검출기의 높은 임계값
# param2 - 축적 배열에서 원 검출을 위한 임계값
# minRadius, maxRadius - 검출할 원의 최소, 최대 반지름

# cv2.HOUGH_GRADIENT_ALT 방법이 원 검출 더 잘됨

# 트랙바 생성
cv2.imshow('img', src)
cv2.createTrackbar('minRadius', 'img', 0, 100, on_trackbar)
cv2.createTrackbar('maxRadius', 'img', 0, 150, on_trackbar)
cv2.createTrackbar('threshold', 'img', 0, 100, on_trackbar)
cv2.setTrackbarPos('minRadius', 'img', 10)
cv2.setTrackbarPos('maxRadius', 'img', 80)
cv2.setTrackbarPos('threshold', 'img', 40)
cv2.waitKey()

cv2.destroyAllWindows()
