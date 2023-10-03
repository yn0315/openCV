import sys
import numpy as np
import cv2


oldx, oldy = -1, -1


def on_mouse(event, x, y, flags, _):
    global oldx, oldy

    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        oldx, oldy = -1, -1

    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.line(img, (oldx, oldy), (x, y), (255, 255, 255), 40, cv2.LINE_AA)
            oldx, oldy = x, y
            cv2.imshow('img', img)


# 학습 & 레이블 행렬 생성

digits = cv2.imread('digits.png', cv2.IMREAD_GRAYSCALE)

if digits is None:
    print('Image load failed!')
    sys.exit()

h, w = digits.shape[:2]

cells = [np.hsplit(row, w//20) for row in np.vsplit(digits, h//20)]
cells = np.array(cells)
train_images = cells.reshape(-1, 400).astype(np.float32)
train_labels = np.repeat(np.arange(10), len(train_images)/10)

# KNN 학습

knn = cv2.ml.KNearest_create()
# knn알고리즘 객체생성
# cv2.ml.KNearest_create() -> retval
# retval - cv2.ml_KNearest객체
knn.train(train_images, cv2.ml.ROW_SAMPLE, train_labels)

# 사용자 입력 영상에 대해 예측

img = np.zeros((400, 400), np.uint8)

cv2.imshow('img', img)
cv2.setMouseCallback('img', on_mouse)

while True:
    key = cv2.waitKey()

    if key == 27:
        break
    elif key == ord(' '):
        test_image = cv2.resize(img, (20, 20), interpolation=cv2.INTER_AREA)
        test_image = test_image.reshape(-1, 400).astype(np.float32)

        ret, _, _, _ = knn.findNearest(test_image, 5)

        # knn알고리즘으로 입력데이터의 클래스 예측
        # cv.ml_KNearest.findNearest(samples, k, results=None, 
        #                            neighborResponses=None, dist=None , flags=None)
        #                            -> retval, results, neighborResponses, dist
        # samples - 입력 벡터가 행 단위로 저장된 입력 샘플 행렬
        #           numpy.ndarray. shape=(N, d), dtype=numpy.float32
        # k - 사용할 최근접 이웃개수
        # results - 각 입력 샘플에 대한 예측(분류 또는 회귀) 결과를 저장한 행렬.
        #           numpy.ndarray. shape=(N, 1), dtype=numpy.float32
        # neighborResponses - 예측에 사용된 k개의 최근접 이웃 클래스 정보 행렬.
        #                     numpy.ndarray. shape=(N, k), dtype=numpy.float32
        # dist - 입력 벡터와 예측에 사용된 k개의 최근접 이웃과의 거리를 저장한 행렬.
        #        numpy.ndarray. shape=(N, k), dtype=numpy.float32
        # retval - 입력 벡터가 하나인 경우에 대한 응답
        print(int(ret))

        img.fill(0)
        cv2.imshow('img', img)

cv2.destroyAllWindows()
