import sys
import math
import numpy as np
import cv2


# 카메라 열기
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Camera open failed!')
    sys.exit()

w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
w2 = w // 2
h2 = h // 2

ret, frame = cap.read()

if not ret:
    print('Frame read failed!')
    sys.exit()

frame = cv2.flip(frame, 1)  # 좌우 대칭 거울을 보듯이 만들기 위해
gray1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
gray1 = cv2.resize(gray1, (w2, h2), interpolation=cv2.INTER_AREA)

# 매 프레임에 대해 옵티컬플로우 계산
while True:
    ret, frame = cap.read()

    if not ret:
        print('Frame read failed!')
        break

    frame = cv2.flip(frame, 1)  # 좌우 대칭
    gray2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.resize(gray2, (w2, h2), interpolation=cv2.INTER_AREA)

    # 밀집 옵티컬플로우 계산
    flow = cv2.calcOpticalFlowFarneback(gray1, gray2, None, 0.5, 3, 15, 3, 5, 1.1, 0)
    # 밀집 옵티컬플로우 계산함수
    # cv2.calcOpticalFlowFarneback(prev, next, flow, pyr_scale, levels, winsize,
    #                              iterations, poly_n, poly_sigma, flags) -> flow
    # prev,next - 이전영상과 현재영상 그레이스케일영상 
    # flow - (출력) 계산된 옵티컬플로우 . np.ndarray. shape=(h, w, 2), dtype=np.float32. 
    # pyr_scale - 피라미드 영상을 만들 때 축소비율(e.g) 0.5
    # levels - 피라미드 영상개수(e.g) 3
    # winsize - 평균 윈도우 크기(e.g) 13
    # iterations - 각 피라미드 레벨에서 알고리즘 반복횟수(e.g) 10
    # poly_n - 다항식 확장을 위한 이웃 픽셀크기 보통 5 또는 7
    # poly_sigma - 가우시안 표준편차 . poly_n = 5 이면 1.1, poly_n = 7 이면 1.5
    # flags - 0, cv2.OPTFLOW_USE_INITIAL_FLOW, cv2.OPTFLOW_FARNEBACK_GAUSSIAN.

    
    vx, vy = flow[..., 0], flow[..., 1]
    mag, ang = cv2.cartToPolar(vx, vy)

    '''
    # 움직임 벡터 시각화
    hsv = np.zeros((h2, w2, 3), dtype=np.uint8)
    hsv[..., 0] = ang*180/np.pi/2
    hsv[..., 1] = 255
    hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    cv2.imshow('flow', bgr)
    '''

    # 움직임이 충분히 큰 영역 선택
    motion_mask = np.zeros((h2, w2), dtype=np.uint8)
    motion_mask[mag > 2.0] = 255

    mx = cv2.mean(vx, mask=motion_mask)[0]
    my = cv2.mean(vy, mask=motion_mask)[0]
    m_mag = math.sqrt(mx*mx + my*my)

    if m_mag > 4.0:
        m_ang = math.atan2(my, mx) * 180 / math.pi
        m_ang += 180

        pt1 = (100, 100)

        if m_ang >= 45 and m_ang < 135: # 위쪽
            pt2 = (100, 30)
        elif m_ang >= 135 and m_ang < 225: 
            pt2 = (170, 100)
        elif m_ang >= 225 and m_ang < 315:
            pt2 = (100, 170)
        else:
            pt2 = (30, 100)

        cv2.arrowedLine(frame, pt1, pt2, (0, 0, 255),
                        7, cv2.LINE_AA, tipLength=0.7)

    # 결과 영상 화면 출력
    cv2.imshow('frame', frame)
    #cv2.imshow('motion_mask', motion_mask)

    if cv2.waitKey(1) == 27:
        break

    # 현재 프레임을 이전 프레임으로 복사
    gray1 = gray2

cap.release()
cv2.destroyAllWindows()
