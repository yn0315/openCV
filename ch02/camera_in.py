import sys
import cv2


# 카메라 열기
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera open failed!")
    sys.exit()

# 카메라 프레임 크기 출력
print('Frame width:', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('Frame height:', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320) # 프레임크기조정
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT,240)

# 카메라 프레임 처리
while True:
    ret, frame = cap.read() # 프레임을 계속 받아오는 함수
#   ret - 프레임을 받아왔는지 true 또는 false값으로 나타냄
    if not ret:
        break

    edge = cv2.Canny(frame, 50,150) # 윤곽선추출함수 

    inversed = ~frame  # 반전

    cv2.imshow('frame', frame) # 프레임을 화면에 보여줌
    cv2.imshow('edge',edge) # 윤곽선
    cv2.imshow('inversed', inversed)

    if cv2.waitKey(10) == 27:
        break

cap.release() # 작업해제
cv2.destroyAllWindows()
