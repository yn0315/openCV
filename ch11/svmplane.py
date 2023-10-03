import sys
import numpy as np
import cv2


trains = np.array([[150, 200], [200, 250],
                   [100, 250], [150, 300],
                   [350, 100], [400, 200],
                   [400, 300], [350, 400]], dtype=np.float32)
labels = np.array([0, 0, 0, 0, 1, 1, 1, 1])

svm = cv2.ml.SVM_create()
svm.setType(cv2.ml.SVM_C_SVC)
svm.setKernel(cv2.ml.SVM_LINEAR)
#svm.setKernel(cv2.ml.SVM_RBF)

svm.trainAuto(trains, cv2.ml.ROW_SAMPLE, labels)
# svm 자동학습(k- 폴드교차검증)
# cv.ml_SVM.trainAuto(samples, layout, responses, kFold=None, ...) -> retval
# samples - 학습 데이터 행렬. numpy.ndarray. shape=(N, d), dtype=numpy.float32
# layout - 학습 데이터 배치 방법. cv2.ROW_SAMPLE 또는 cv2.COL_SAMPLE
# responses - 각 학습 데이터에 대응되는 응답(레이블) 벡터. numpy.ndarray
#             shape=(N, ) 또는 (N, 1).dtype=numpy.int32 또는 numpy.float32
# kFold - 교차 검증을 위한 부분 집합 개수
# retval - 학습이 정상적으로 완료되면 True

print('C:', svm.getC())
print('Gamma:', svm.getGamma())

w, h = 500, 500
img = np.zeros((h, w, 3), dtype=np.uint8)

for y in range(h):
    for x in range(w):
        test = np.array([[x, y]], dtype=np.float32)
        _, res = svm.predict(test)
        ret = int(res[0, 0])

        if ret == 0:
            img[y, x] = (128, 128, 255)  # Red
        else:
            img[y, x] = (128, 255, 128)  # Green

color = [(0, 0, 128), (0, 128, 0)]

for i in range(trains.shape[0]):
    x = int(trains[i, 0])
    y = int(trains[i, 1])
    l = labels[i]

    cv2.circle(img, (x, y), 5, color[l], -1, cv2.LINE_AA)

cv2.imshow('svm', img)
cv2.waitKey()
cv2.destroyAllWindows()
