import sys
import numpy as np
import cv2


# 비디오 파일 열기
cap = cv2.VideoCapture('camshift.avi')

if not cap.isOpened():
    print('Video open failed!')
    sys.exit()

# 초기 사각형 영역: (x, y, w, h)
x, y, w, h = 135, 220, 100, 100
rc = (x, y, w, h)

ret, frame = cap.read()

if not ret:
    print('frame read failed!')
    sys.exit()

roi = frame[y:y+h, x:x+w]
roi_hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

# HS 히스토그램 계산
channels = [0, 1]
ranges = [0, 180, 0, 256]
hist = cv2.calcHist([roi_hsv], channels, None, [90, 128], ranges)

# CamShift 알고리즘 종료 기준
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

# 비디오 매 프레임 처리
while True:
    ret, frame = cap.read()

    if not ret:
        break

    # HS 히스토그램에 대한 역투영
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    backproj = cv2.calcBackProject([frame_hsv], channels, hist, ranges, 1)

    # CamShift
    ret, rc = cv2.CamShift(backproj, rc, term_crit)
    # 캠시프트 추적함수
    # cv2.CamShift(probImage, window, criteria) -> retval, window
    # probimage - 관심객체에 대한 히스토그램 역투영영상(확률영상)
    # window  - 초기검색영역 윈도우 & 결과영역반환
    # criteria - 알고리즘 종료기준(type, maxCount, epsilon) 튜플
    #            (e.g.) term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)\
    #            최대 10번반복, 정확도가 1이하이면(이동크기가 1픽셀보다 작으면) 종료
    
    # retval - 추적하는 객체의 모양을 나타내는 회전된 사각형 정보를 반환
    #          ((cx, cy), (width, height), angle) .

    # 추적 결과 화면 출력
    cv2.rectangle(frame, rc, (0, 0, 255), 2)
    cv2.ellipse(frame, ret, (0, 255, 0), 2) # 타원 그리는 함수
    cv2.imshow('frame', frame)

    if cv2.waitKey(60) == 27:
        break

cap.release()
cv2.destroyAllWindows()
