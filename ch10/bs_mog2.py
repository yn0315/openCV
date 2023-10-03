import sys
import numpy as np
import cv2


# 비디오 파일 열기
cap = cv2.VideoCapture('PETS2000.avi')

if not cap.isOpened():
    print('Video open failed!')
    sys.exit()

# 배경 차분 알고리즘 객체 생성
bs = cv2.createBackgroundSubtractorMOG2()
#bs = cv2.createBackgroundSubtractorKNN()
#bs.setDetectShadows(False)

# backgroundSubtractorMOG2 클래스 생성 함수
# cv2.createBackgroundSubtractorMOG2(, history=None, varThreshold=None,detectShadows=None) -> dst
# history - 히스토리 길이 기본값 500
# varThreshold - 픽셀과 모델 사이의 마할라노비스거리 제곱에 대한 임계값
#                해당 픽셀이 배경모델에 의해 잘 표현되는지를 판단
#                기본값 16
# detecshadows - 그림자검출여부 기본값 true





# 비디오 매 프레임 처리
while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    fgmask = bs.apply(gray)
    # 전면 객체 마스크 생성함수
    # cv2.BackgroundSubtractor.apply(image, fgmask=None, learningRate=None) -> fgmask
    # image - (입력) 다음 비디오프레임
    # fgmask - (출력) 전경마스크영상 8비트 이진영상
    # learningRate - 배경모델 학습속도지정(0~1사이의 실수) 기본값 -1
    #                0 - 배경모델 갱신하지 않음
    #                1 - 매 프레임마다 배경모델을 새로 만듦
    #                음수 - 자동으로 결정됨

    back = bs.getBackgroundImage()
    # 배경영상 반환함수
    # cv2.BackgroundSubtractor.getBackgroundImage(, backgroundImage=None)-> backgroundImage
    # backgroundimage - (출력) 학습된 배경영상 

    # 레이블링을 이용하여 바운딩 박스 표시
    cnt, _, stats, _ = cv2.connectedComponentsWithStats(fgmask)

    for i in range(1, cnt):
        x, y, w, h, s = stats[i]

        if s < 80:
            continue

        cv2.rectangle(frame, (x, y, w, h), (0, 0, 255), 2)

    cv2.imshow('frame', frame)
    cv2.imshow('back', back)
    cv2.imshow('fgmask', fgmask)

    if cv2.waitKey(20) == 27:
        break

cap.release()
cv2.destroyAllWindows()
