import sys
import numpy as np
import cv2


src = cv2.imread('lenna.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
# 케스케이드 분류기 : 얼굴검출
# cv2.CascadeClassifier 객체 생성 및 학습 데이터 불러오기
# cv2.CascadeClassifier.load(filename) -> retval
# filename - xml파일이름
# retval - 성공하면 true, 실패하면 false



if classifier.empty():
    print('XML load failed!')
    sys.exit()

faces = classifier.detectMultiScale(src)
# 멀티스케일 객체검출함수
# cv2.CascadeClassifier.detectMultiScale(image, scaleFactor=None,
#                                        minNeighbors=None, flags=None, minSize=None, maxSize=None) -> result
# image - 입력 영상 (cv2.CV_8U)
# scaleFactor - 영상 축소 비율. 기본값은 1.1
# minNeighbors - 얼마나 많은 이웃 사각형이 검출되어야 최종 검출 영역으로 설정할지를 지정. 기본값은 3.
# flags - (현재) 사용되지 않음
# minSize - 최소 객체 크기. (w, h) 튜플
# maxSize - 최대 객체 크기. (w, h) 튜플
# result - 검출된 객체의 사각형 정보(x, y, w, h)를 담은 numpy.ndarray
#          shape=(N, 4). dtype=numpy.int32.

for (x, y, w, h) in faces:
    cv2.rectangle(src, (x, y, w, h), (255, 0, 255), 2)

cv2.imshow('src', src)
cv2.waitKey()
cv2.destroyAllWindows()
