import sys
import numpy as np
import cv2


# 비디오 파일 열기
cap = cv2.VideoCapture('PETS2000.avi')

if not cap.isOpened():
    print('Video open failed!')
    sys.exit()

# 배경 영상 등록
ret, back = cap.read()

if not ret:
    print('Background image registration failed!')
    sys.exit()

# back: uint8 배경, fback: float32 배경
back = cv2.cvtColor(back, cv2.COLOR_BGR2GRAY)
back = cv2.GaussianBlur(back, (0, 0), 1.0) # 노이즈 제거용
fback = back.astype(np.float32)

# 비디오 매 프레임 처리
while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (0, 0), 1.0)

    # fback: float32, back: uint8 배경
    cv2.accumulateWeighted(gray, fback, 0.01) # fback은 입력과 동시에 출력됨
    # 이동 평균계산을 위한 가중치 누적 함수 
    # cv2.accumulateWeighted(src, dst, alpha, mask=None) -> dst
    # src - 입력영상 1또는 3채널 8비트 또는 32비트 실수형
    # dst - 축적영상. 입력영상과 동일채널개수 32비트 또는 64비트 실수형 ->입력과 출력에 모두 필요한 경우 인자로 주어야 함
    # alpha - (입력영상에 대한)가중치
    # mask - 마스크영상
    back = fback.astype(np.uint8) # absdiff함수에서 같은 타입으로 맞춰줘야하기 때문에 

    diff = cv2.absdiff(gray, back)
    _, diff = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    # 레이블링을 이용하여 바운딩 박스 표시
    cnt, _, stats, _ = cv2.connectedComponentsWithStats(diff)

    for i in range(1, cnt):
        x, y, w, h, s = stats[i]

        if s < 100:
            continue

        cv2.rectangle(frame, (x, y, w, h), (0, 0, 255), 2)

    cv2.imshow('frame', frame)
    cv2.imshow('diff', diff)
    cv2.imshow('back', back)

    if cv2.waitKey(30) == 27:
        break

cap.release()
cv2.destroyAllWindows()
