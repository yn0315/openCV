import sys
import numpy as np
import cv2


src = cv2.imread('keyboard.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

_, src_bin = cv2.threshold(src, 0, 255, cv2.THRESH_OTSU) # 이진화

cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(src_bin)

dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

for i in range(1, cnt): # 1부터 시작하는 것은 배경은 제외하겠다는 뜻
    (x, y, w, h, area) = stats[i]

    if area < 20: # 노이즈를 제거하기 위함/작은 것은 무시해라
        continue

    cv2.rectangle(dst, (x, y, w, h), (0, 255, 255))

cv2.imshow('src', src)
cv2.imshow('src_bin', src_bin)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
