import cv2
import sys

print('hello, OpenCV', cv2.__version__) # 버전 불러오기

img = cv2.imread('cat.bmp',cv2.IMREAD_GRAYSCALE) #이미지 불러오기

# 이미지 불러오기
# cv2.imread(filename, flags=None) -> retval(return value)

# flags 영상파일 불러오기 옵션플래그
# cv2.IMREAD_COLOR -BGR컬러영상으로 읽기/ 이게 기본 설정
#                   SHAPE = (rows, cols,3)

# cv2.IMREAD_GRAYSCALE - 그레이스케일영상으로 읽기
#                        SHAPE = (rows, cols)

# cv2.IMREAD_UNCHANGED - 영상파일속성 그대로 읽기
#                        {e.g.} 투명한 png 파일 : SHAPE = (rows, cols, 4)

# retval - 불러온 영상데이터(numpy.ndarray)

#영상파일 저장하기
# cv2.imwrite(filename, img, params-None) -> retval   # 영상파일 저장하기
# img - 저장할 영상 데이터(numpy.ndarray)
# params - 파일 저장옵션 지정(속성 & 값의 정수 쌍)
#          {e.g} [cv2.IMWRITE_JPEG_QUALITY,90] - JPG압축률을 90%로 지정
# retval - 정상적으로 저장하면 true, 실패하면 false

if img is None: #이미지를 못 불러왔을 시
    print('Image load failed!')
    sys.exit()

cv2.imwrite('cat_gray.png',img)

cv2.namedWindow('image',cv2.WINDOW_NORMAL) # 마우스로 크기조절가능/영상이 너무 클 때 사용

# 새창 띄우기
# cv2.namedWindow(winname, flags=None) -> None
# winname - 창 고유이름(문자열)
# flags - 창 속성 지정 플래그
#         cv2.WINDOW_NORMAL = 영상 크기를 창 크기에 맞게 지정
#         cv2.WINDOW_AUTOSIZE = 창 크기를 영상 크기에 맞게 변경(기본값)


cv2.imshow('image',img) # 어떤 창에 어떤영상데이터를 보여줄꺼냐/ image창에 img영상을 보여줄것이다
# 영상출력하기
# cv2.imshow(winname, mat) -> None
# winname: 영상을 출력할 대상 창 이름
# mat: 출력할 영상 데이터 (numpy.ndarray)
# 

cv2.waitKey() # 키보드 입력을 기다리면서 영상을 보여주는 역할
# 키보드 입력 대기
# cv2.waitKey(delay = None) -> retval
# delay - 밀리초 단위 대기시간, 기본값은 0 무한히 기다림
# retval - 눌린 키값(아스키코드), 키가 눌리지 않으면 -1.
# 특정 키 입력을 확인하려면 ord()함수를 이용
# while True:
#   if cv2.waitKey() == ord('q'):
#       break
# cv2.waitKey(3000) - 3초후에 자동으로 꺼짐

cv2.destroyAllWindows() #모든 창을 닫아라 창 닫을 때 x자 누르는 것보다 아무키나 누르는 것이 정상종료됨
# 창닫기
# cv2.destroywindow(winname) -> None 해당 창만 닫힘
# cv2.destroyAllWindows() -> None 모든 창 닫힘

