import sys
import numpy as np
import cv2


# 영상 불러오기
src1 = cv2.imread('graf1.png', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('graf3.png', cv2.IMREAD_GRAYSCALE)

if src1 is None or src2 is None:
    print('Image load failed!')
    sys.exit()

# 특징점 알고리즘 객체 생성 (KAZE, AKAZE, ORB 등)
feature = cv2.KAZE_create()
#feature = cv2.AKAZE_create()
#feature = cv2.ORB_create()

# 특징점 검출
kp1 = feature.detect(src1)
kp2 = feature.detect(src2)
# 특징점 검출함수
# cv2.Feature2D.detect(image, mask=None) -> keypoints
# image - 입력영상
# mask - 마스크영상
# keypoints - 검출된 특징점 정보 . cv2.KeyPoint 객체의 리스트

print('# of kp1:', len(kp1))
print('# of kp2:', len(kp2))

# 검출된 특징점 출력 영상 생성
dst1 = cv2.drawKeypoints(src1, kp1, None,
                         flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
dst2 = cv2.drawKeypoints(src2, kp2, None,
                         flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# 검출된 특징점 그리기 함수 
# cv2.drawKeypoints(image, keypoints, outImage, color=None, flags=None) ->outImage
# image - 입력영상
# keypoints - 검출된 특징점 정보. cv2.KeyPoint 객체의 리스트
# outImage - 출력영상
# color - 특징점표현색상 기본값(-1,-1,-1,-1)이며 이 경우 임의의 색상으로 표현
# flags - 특징점 표현방법
#         cv2.DRAW_MATCHES_FLAGS_DEFAULT - 특징점 위치만을 표현하는 작은 크기의 원
#         cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS - 특징점의 크기와 방향을 반영한 원 
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()
