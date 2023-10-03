import sys
import cv2


# 영상 불러오기
img1 = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('cat.bmp', cv2.IMREAD_COLOR)

if img1 is None or img2 is None:
    print('Image load failed!')
    sys.exit()

print(type(img1))
print(img1.shape) # 각 차원의 크기(h,w) 또는 (h,w,3) // 2는 그레이스케일, 3은 컬러, 4는 투명이미지png
print(img2.shape)
print(img1.dtype) # 원소의 데이터타입 일반적인 영상이면 numpy.uint8
print(img2.dtype)

h,w = img1.shape[:2]
print('w X h = {} x {}'.format(w,h))

h,w = img2.shape[:2] # 컬러일 때 두자리로 안 자르면 에러남 뒤의 숫자를 받을 변수가 없기 때문
print('w X h = {} x {}'.format(w,h))


if img1.ndim == 2:
    print('img1 is a grayscale image')

if img1.shape == 2:
    print('img1 is a grayscale image')

# for y in range(h):
#     for x in range(w):
#         img1[y,x] = 0
#         img2[y,x] = (0,255,255) 이런 코드는 쓰면 안됨

img1[:,:] = 0
img2[:,:] = (0,255,255) # 위에처럼 말고 이렇게 작성

x = 20
y = 10
# p1 = img1[y,x]
# p2 = img2[y,x]

p1 = img1[y,x] = 0 # 검은색 대입
p2 = img2[y,x] = (0,0,255) # 빨간색 대입


print(p1,"p1")
print(p2,"p2")

# 영상의 속성 참조
print('type(img1):', type(img1))
print('img1.shape:', img1.shape)
print('img2.shape:', img2.shape)
print('img1.dtype:', img1.dtype)

# 영상의 크기 참조
h, w = img2.shape[:2]
print('img2 size: {} x {}'.format(w, h))

if len(img1.shape) == 2:
    print('img1 is a grayscale image')
elif len(img1.shape) == 3:
    print('img1 is a truecolor image')

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey()

# 영상의 픽셀 값 참조
for y in range(h):
    for x in range(w):
        img1[y, x] = 255
        img2[y, x] = (0, 0, 255)        

# img1[:,:] = 255
# img2[:,:] = (0, 0, 255)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey()

cv2.destroyAllWindows()
