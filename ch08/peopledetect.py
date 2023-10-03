import sys
import random
import numpy as np
import cv2


# 동영상 불러오기
cap = cv2.VideoCapture('vtest.avi')

if not cap.isOpened():
    print('Video open failed!')
    sys.exit()

# 보행자 검출을 위한 HOG 기술자 설정
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
# hog 보행자 검출
# cv2.HOGDescriptor_getDefaultPeopleDetector() -> retval
# retval - 미리 훈련된 특징 벡터. numpy.ndarray. shape=(3781, 1).dtype=numpy.float32

# svm분류기 계수 등록하기
# cv2.HOGDescriptor.setSVMDetector(svmdetector) -> None
# svmdetector - 선형 SVM 분류기를 위한 계수
while True:
    ret, frame = cap.read()

    if not ret:
        break

    # 매 프레임마다 보행자 검출
    detected, _ = hog.detectMultiScale(frame)
    # hog 멀티스케일 객체검출함수
    # cv2.HOGDescriptor.detectMultiScale(img, hitThreshold=None, winStride=None,
    #     padding=None, scale=None, finalThreshold=None, 
    #     useMeanshiftGrouping=None) -> foundLocations, foundWeights
    # img - 입력 영상. cv2.CV_8UC1 또는 cv2.CV_8UC3.
    # hitThreshold - 특징 벡터와 SVM 분류 평면까지의 거리에 대한 임계값
    # winStride - 셀 윈도우 이동 크기. (0, 0) 지정 시 셀 크기와 같게 설정
    # padding - 패딩크기
    # scale - 검색 윈도우 크기 확대 비율. 기본값은 1.05
    # finalThreshold - 검출 결정을 위한 임계값
    # useMeanshiftGrouping - 겹쳐진 검색 윈도우를 합치는 방법 지정 플래그
    # foundLocations -  (출력) 검출된 사각형 영역 정보
    # foundWeights -  (출력) 검출된 사각형 영역에 대한 신뢰도

    # 검출 결과 화면 표시
    for (x, y, w, h) in detected:
        c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        cv2.rectangle(frame, (x, y, w, h), c, 3)

    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()
