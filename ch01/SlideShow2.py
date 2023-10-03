import os
import glob # 목록 읽어오는 거 특정 패턴의 문자열형태로 돼있는 파일들을 다 불러올 수 있음
import cv2

# 와일드카드 (부호)
# * - 모든 파일
# sql의 % - a%는 a로 시작하는 모든 문자열과 일치하는 것


img_files = glob.glob('.\\images\\*.jpg')

for f in img_files:
    print(f)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

cnt = len(img_files)
idx = 0
while True:
    img = cv2.imread(img_files[idx])

    cv2.imshow('image',img)

    if cv2.waitKey(1000) == 27:
        break

    idx += 1
    if idx >= cnt:
        idx = 0

    cv2.destroyAllWindows()
