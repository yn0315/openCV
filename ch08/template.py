import sys
import numpy as np
import cv2


# 입력 영상 & 템플릿 영상 불러오기
src = cv2.imread('circuit.bmp', cv2.IMREAD_GRAYSCALE)
templ = cv2.imread('crystal.bmp', cv2.IMREAD_GRAYSCALE)

if src is None or templ is None:
    print('Image load failed!')
    sys.exit()

# 입력 영상 밝기 50증가, 가우시안 잡음(sigma=10) 추가
noise = np.zeros(src.shape, np.int32)
cv2.randn(noise, 50, 10)
src = cv2.add(src, noise, dtype=cv2.CV_8UC3)

# 템플릿 매칭 & 결과 분석
res = cv2.matchTemplate(src, templ, cv2.TM_CCOEFF_NORMED)
# 템플릿 매칭 함수
# cv2.matchTemplate(image, templ, method, result=None, mask=None) -> result
# image - 입력 영상. 8비트 또는 32비트.
# templ - 템플릿 영상. image보다 같거나 작은 크기, 같은 타입.
# method - 비교 방법. cv2.TM_으로 시작하는 플래그 지정
# result - 비교 결과 행렬. numpy.ndarray. dtype=numpy.float32
#          image의 크기가 W x H 이고, templ의 크기가 w x h 이면
#          result 크기는 (W - w + 1) X (H - h +1).

res_norm = cv2.normalize(res, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

_, maxv, _, maxloc = cv2.minMaxLoc(res)
print('maxv:', maxv)
print('maxloc:', maxloc)

# 매칭 결과를 빨간색 사각형으로 표시
th, tw = templ.shape[:2]
dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)
cv2.rectangle(dst, maxloc, (maxloc[0] + tw, maxloc[1] + th), (0, 0, 255), 2)

# 결과 영상 화면 출력
cv2.imshow('res_norm', res_norm)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
