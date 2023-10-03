import sys
import numpy as np
import cv2

# fast 코너검출
# cv2.FastFeatureDetector_create(, threshold=None, nonmaxSuppression=None,type=None) -> retval
# cv2.FastFeatureDetector.detect(image) -> keypoints
# threshold - 중심 픽셀 값과 주변 픽셀 값과의 차이 임계값. 기본값은 10
# nonmaxSuppresion - 비최대 억제 수행 여부. 기본값은 True.
# type - 코너 검출 방법. 기본값은 cv2.FAST_FEATURE_DETECTOR_TYPE_9_16.
# retval - FastFeatureDetector 객체
# image - (입력) 그레이스케일 영상
# keypoints - (출력) 검출된 코너점 정보. cv2.KeyPoint 객체를 담은 리스트
#             cv2.KeyPoint의 pt 멤버를 이용하여 코너 좌표 추출
#             pt[0]은 x좌표, pt[1]은 y좌표. pt는 float자료형의 튜플

src = cv2.imread('building.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

tm = cv2.TickMeter()

# GFTT
tm.start()

corners = cv2.goodFeaturesToTrack(src, 400, 0.01, 10)

tm.stop()
print('GFTT: {}ms.'.format(tm.getTimeMilli()))

dst1 = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

if corners is not None:
    for i in range(corners.shape[0]):
        pt = (int(corners[i, 0, 0]), int(corners[i, 0, 1]))
        cv2.circle(dst1, pt, 5, (0, 0, 255), 2)

# FAST
tm.reset()
tm.start()

fast = cv2.FastFeatureDetector_create(60) # 클래스 객체를 만들고
keypoints = fast.detect(src) # 함수를 호출

tm.stop()
print('FAST: {}ms.'.format(tm.getTimeMilli()))

dst2 = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

for kp in keypoints:
    pt = (int(kp.pt[0]), int(kp.pt[1]))
    cv2.circle(dst2, pt, 5, (0, 0, 255), 2)

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()

cv2.destroyAllWindows()
