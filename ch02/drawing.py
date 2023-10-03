import numpy as np
import cv2

img = np.full((400, 400,3), 255, np.uint8) # 컬러/ 흰배경
#     np.full(shape,fill-value, dtype)

cv2.line(img, (50, 50), (200, 50), (0, 0, 255), 5, cv2.LINE_AA)
# 직선그리기
# cv2.line(img, pt1, pt2, color, thickness=None, lineType=None, shift=None) -> img
# img - 그림을 그릴 영상
# pt1,pt2 - 직선의 시작점과 끝점
# color - 선 색상 또는 밝기 (b,g,r)튜플 또는 정수값
# thikness - 선두께 기본값 1
# lineType - 선 타입/cv2.LINE_4, cv2.LINE_8(기본값), cv2.LINE_AA 중 선택
# shift - 그리기 좌표값의 축소비율 / 기본값은 0
cv2.line(img, (50, 60), (150, 160), (0, 0, 128))

cv2.rectangle(img, (50, 200, 150, 100), (0, 255, 0), 2)
#                  rec - (x,y,가로,세로)
cv2.rectangle(img, (70, 220), (180, 280), (0, 128, 0), -1)
#                   좌측상단좌표, 사각형의 크기
# 사각형 그리기
# cv2.rectangle(img, pt1, pt2, color, thickness=None, lineType=None,shift=None) -> img
# pt1,pt2 - 좌측상단의 좌표, 우측하단의 좌표
# rec - 사각형의 위치정보(x,y,w,h) 튜플
# color - 선색상 또는 밝기(b,g,r) 튜플 또는 정수값
# thickness - 선두께 기본값 1, -1을 지정하면 내부를 채움


cv2.circle(img, (300, 100), 30, (255, 255, 0), -1, cv2.LINE_AA)
cv2.circle(img, (300, 100), 60, (255, 0, 0), 3, cv2.LINE_AA)

# 원그리기
# cv2.circle(img, center, radius, color, thickness=None, lineType=None,shift=None) -> img
# center - 원의 중심좌표 (x,y)튜플
# radius - 원의 반지름


pts = np.array([[250, 200], [300, 200], [350, 300], [250, 300]]) # 시계방향
cv2.polylines(img, [pts], True, (255, 0, 255), 2)
# 다각형그리기
# cv2.polylines(img, pts, isClosed, color, thickness=None, lineType=None, shift=None) -> img
# pts - 다각형 외곽 점들의 좌표배열 numpy.ndarray의 리스트
#       (e.g.) [np.array([[10,10],[50,50],[10,50]], dtype=np.int32)]
# isClosed - 폐곡선 여부 true(시작점과 끝점이 붙음, 닫힌도형) or false(시작점과 끝점이 안 붙음)
#  


text = 'Hello? OpenCV ' + cv2.__version__
cv2.putText(img, text, (50, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.8, 
            (0, 0, 255), 1, cv2.LINE_AA)

# 문자열출력
# cv2.putText(img, text, org, fontFace, fontScale, color, thickness=None,lineType=None, bottomLeftOrigin=None) -> img
# text - 출력할 문자열
# org - 영상에서 문자열을 출력할 위치의 좌측하단좌표(x,y)튜플
# fontFace - 폰트종류/cv2.FONT_HERSHEY_ 로 시작하는 상수 중 선택
# fontScale - 폰트크기 확대/축소비율 1(기본값)보다 크면확대
# bottomLeftOrigin - true이면 영상의 좌측하단을 원점으로 간주, 기본값은 false


cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()

