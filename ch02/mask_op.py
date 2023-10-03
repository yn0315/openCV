import sys
import cv2


# 마스크 영상을 이용한 영상 합성
# src = cv2.imread('airplane.bmp', cv2.IMREAD_COLOR)
src = cv2.imread('opencv-logo-white.png', cv2.IMREAD_UNCHANGED) # png파일일경우 unchanged사용
#mask = cv2.imread('mask_plane.bmp', cv2.IMREAD_GRAYSCALE)

mask = src[:,:, -1] # 맨 마지막 채널을 가져와서 마스크영상으로 쓰겠다/ 투명이미지의 맨 마지막 채널은 마스크영상으로 사용됨
src = src[:,:,0:3] # 0,1,2 채널 가져와서 src 영상으로 쓰겠다

dst = cv2.imread('field.bmp', cv2.IMREAD_COLOR)

h, w = src.shape[:2]
crop = dst[0:h,0:w] # 픽셀값공유/ dst영상의 일부분인데 로고영상과 같은 크기의 일부분을 잘라와서 픽셀값공유

if src is None or mask is None or dst is None:
    print('Image load failed!')
    sys.exit()

cv2.copyTo(src,mask,crop)

# cv2.copyTo(src, mask, dst) # 입력영상에서 마스크부분만 복사해서 리턴
# dst[mask > 0] = src[mask > 0] - numpy의 boolean인덱싱방법

# 마스크 연산을 지원하는 픽셀값 복사함수
# cv2.copyTo(src,mask,dst=None) -> dst
# src - 입력영상
# mask - 마스크영상 cv2.CV_8U. (numpy.uint8)
#        0이 아닌 픽셀에 대해서만 복사 연산을 수행
# dst - 출력영상 /만약 src와 크기 및 타입이 같은 dst를 입력으로 지정하면
#       dst를 새로 생성하지 않고 연산을 수행
#       그렇지않으면 dst를 새로 생성하여 연산을 수행한 후 반환함

# cv2.imshow('src', src)
# cv2.imshow('dst', dst)
# cv2.imshow('mask', mask)
cv2.waitKey()
cv2.destroyAllWindows()

# 알파 채널을 마스크 영상으로 이용
src = cv2.imread('cat.bmp', cv2.IMREAD_COLOR)
logo = cv2.imread('opencv-logo-white.png', cv2.IMREAD_UNCHANGED)

if src is None or logo is None:
    print('Image load failed!')
    sys.exit()

mask = logo[:, :, 3]    # mask는 알파 채널로 만든 마스크 영상
logo = logo[:, :, :-1]  # logo는 b, g, r 3채널로 구성된 컬러 영상
# print(logo.shape,"logo.shape")
h, w = mask.shape[:2]
crop = src[10:10+h, 10:10+w]  # logo, mask와 같은 크기의 부분 영상 추출

cv2.copyTo(logo, mask, crop)
#crop[mask > 0] = logo[mask > 0]

# cv2.imshow('src', src)
cv2.imshow('logo', logo)
# cv2.imshow('mask', mask)
cv2.waitKey()
cv2.destroyAllWindows()
