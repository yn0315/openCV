import sys
import cv2


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera open failed!")
    sys.exit()

w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*'DIVX') # *'DIVX' == 'D', 'I', 'V', 'X'

delay = round(1000 / fps) # 프레임당 시간간격

out = cv2.VideoWriter('output.avi', fourcc, fps, (w, h))
# videowriter - 동영상파일 저장할 수 있는 클래스
# 저장을 위한 동영상파일 열기
# cv2.VideoWriter(filename, fourcc, fps, frameSize, isColor=None) -> retval
# forcc - 동영상파일의 코덱,압축방식,색상,픽셀 포맷 등을 정의하는 정수값
# fps - 초당 프레임수
# isColor - 컬러영상이면 true 아니면 false/ 그레이스케일 영상저장하려면 컬러로 변환 후 저장해야함

if not out.isOpened():
    print('File open failed!')
    cap.release()
    sys.exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    #inversed = ~frame

    # out.write(inversed)
    edge = cv2.Canny(frame,50,150) #그레이스케일이라 저장안됨
    edge_color= cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR) # 컬러로 변환해라
    # out.write(frame)
    out.write(edge_color)

    cv2.imshow('frame', frame)
    cv2.imshow('edge', edge)
    # cv2.imshow('inversed', inversed)

    if cv2.waitKey(delay) == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
