import sys
import time
import numpy as np
import cv2


img = cv2.imread('hongkong.jpg')

# 연산시간 측정방법
tm = cv2.TickMeter()

tm.reset() # 시간측정 초기화
tm.start() # 시간측정 시작
t1 = time.time() # 이것으로 시간측정해도 됨
# t2 = time.time() # 이것으로 시간측정해도 됨

edge = cv2.Canny(img, 50, 150)

tm.stop() # 시간측정 끝
print('time:', (time.time() - t1) * 1000)
print('Elapsed time: {}ms.'.format(tm.getTimeMilli()))

# 함수 두개를 각자 측정할 경우 두번째 함수 측정 전에 초기화 후 시작해야함
