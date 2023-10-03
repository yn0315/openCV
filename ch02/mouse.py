import sys
import numpy as np
import cv2


oldx = oldy = -1

# 마우스 이벤트 처리함수(콜백함수)형식
# onMouse(event, x, y, flags, param) -> None
# event - 마우스 이벤트 종류/ cv2.EVENT로 시작하는 상수
# x, y -마우스 이벤트 발생좌표
# flags - 마우스 이벤트 발생 시 상태/ cv2.EVENT_FLAG로 시작하는 상수
# param - cv2.setMouseCalback()함수에서 설정한 데이터


def on_mouse(event, x, y, flags, param):
    global oldx, oldy
    global img

    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y
        print('EVENT_LBUTTONDOWN: %d, %d' % (x, y))

    elif event == cv2.EVENT_LBUTTONUP:
        print('EVENT_LBUTTONUP: %d, %d' % (x, y))

    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON: # flags 사용시 & 연산자로 써야함
            # cv2.circle(img,(x,y),5,(0,0,255),-1)
            cv2.line(img, (oldx, oldy), (x, y), (0, 0, 255), 4, cv2.LINE_AA)
            cv2.imshow('image', img)
            oldx, oldy = x, y


# 마우스 이벤트 처리하기
# cv2.setMouseCallback('image', on_mouse, img)
#                       윈도우창이름, 콜백함수이름, param - 전달할 데이터

img = np.ones((480, 640, 3), dtype=np.uint8) * 255

cv2.namedWindow('image')
# nameWindow나 imshow가 호출된 이후에 setMouseCallback을 호출해야함
cv2.setMouseCallback('image', on_mouse, img)

cv2.imshow('image', img)
cv2.waitKey()

cv2.destroyAllWindows()
