import numpy as np
import cv2


# 새 영상 생성하기
img1 = np.empty((240, 320), dtype=np.uint8)       # grayscale image
img2 = np.zeros((240, 320, 3), dtype=np.uint8)    # color image
img3 = np.ones((240, 320), dtype=np.uint8) * 255  # dark gray
# img4 = np.full((240, 320, 3), (0, 255, 255), dtype=np.uint8)  # yellow
img4 = np.full((240,320),128, dtype=np.uint8)

# cv2.imshow('img1', img1)
# cv2.imshow('img2', img2)
# cv2.imshow('img3', img3)
# cv2.imshow('img4', img4)
cv2.waitKey()
cv2.destroyAllWindows()

# 영상 복사
img1 = cv2.imread('HappyFish.jpg')

img2 = img1 # 참조
img3 = img1.copy() # 새로 복사해서 img1을 바꾸어도 영향을 받지 않음

img1[:,:] = (0,255,255)

# img1.fill(255)

# cv2.imshow('img1', img1)
# cv2.imshow('img2', img2)
# cv2.imshow('img3', img3)
cv2.waitKey()
cv2.destroyAllWindows()

# 부분 영상 추출
img1 = cv2.imread('HappyFish.jpg')

img2 = img1[40:120, 30:150]  # numpy.ndarray의 슬라이싱
img3 = img1[40:120, 30:150].copy()

img2.fill(0) # 카피를 한 것이 아니므로 img1이 영향을 받아 해당 부분 검은색으로 변경됨
cv2.circle(img2,(50,50),20, (0,0,255),2) # 원그리기/ img1부분에 원 그려짐

cv2.imshow('img1', img1)
# cv2.imshow('img2', img2)
# cv2.imshow('img3', img3)
cv2.waitKey()
cv2.destroyAllWindows()
