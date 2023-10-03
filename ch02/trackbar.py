import numpy as np
import cv2


def on_level_change(pos):# pos - 위치값
    value = pos * 16 # 이것만 쓰면 255 이상 값이 나와서 검은 색이 됨
    if value >= 255:
        value = 255 # 255 이상일 경우 255로 고정

    img[:] = value
    
    # img[:,:] = value 위처럼 써도 됨
    cv2.imshow('image', img)


img = np.zeros((480, 640), np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('level', 'image', 0, 16, on_level_change)
# 트랙바 생성함수
# cv2.createTrackbar(trackbarName, windowName, value, count, onChange) -> None
# value - 트랙바 위치 초기값
# count - 트랙바 최댓값, 최솟값은 항상 0
# onChange - 트랙바 위치가 변경될 때마다 호출할 콜백함수 이름
#            트랙바 이벤트 콜백함수는 다음형식을 따름
#            onChange(pos) -> None
cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
