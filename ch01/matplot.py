import matplotlib.pyplot as plt
import cv2


# 컬러 영상 출력
imgBGR = cv2.imread('cat.bmp') # numpy.ndarray는 bgr순서
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB) # matplotlib은 rgb순서라서 cvtColor로 형태를 바꿔줘야함

plt.axis('off')
plt.imshow(imgRGB)
plt.show()

# 그레이스케일 영상 출력
imgGray = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

plt.axis('off') # 눈금제거
plt.imshow(imgGray, cmap='gray') # cmap - 컬러맵
plt.show()

# 두 개의 영상을 함께 출력
plt.subplot(121), plt.axis('off'), plt.imshow(imgRGB)
plt.subplot(122), plt.axis('off'), plt.imshow(imgGray, cmap='gray')
plt.show()

# plt.subplot(행의 수, 열의 수, 몇 번째 열에 그릴거냐)
