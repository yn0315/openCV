import sys
import numpy as np
import cv2


src1 = cv2.imread('frame1.jpg')
src2 = cv2.imread('frame2.jpg')

if src1 is None or src2 is None:
    print('Image load failed!')
    sys.exit()

gray1 = cv2.cvtColor(src1, cv2.COLOR_BGR2GRAY)

pt1 = cv2.goodFeaturesToTrack(gray1, 50, 0.01, 10)
pt2, status, err = cv2.calcOpticalFlowPyrLK(src1, src2, pt1, None)
# 루카스-카타데 옵티컬플로우계산함수
# cv2.calcOpticalFlowPyrLK(prevImg, nextImg, prevPts, nextPts, status=None,
#                          err=None, winSize=None, maxLevel=None, criteria=None, flags=None,
#                          minEigThreshold=None) -> nextPts, status, err
# prevImg, nextImg - 이전 프레임과 현재 프레임 8비트 입력영상
# prevPts - 이전프레임에서 추적할 점들  numpy.ndarray. shape=(N, 1, 2), dtype=np.float32.
# nextPts - (출력) prevPts점들이 이동한(현재프레임)좌표
# status - (출력) 점들의 매칭상태 . numpy.ndarray. shape=(N, 1), dtype=np.uint8.
#           i번째 원소가 1이면 prevPts의 i번째 점이 nextPts의 i번째 점으로 이동
# err - 결과 오차정보  numpy.ndarray. shape=(N, 1), dtype=np.float32
# winSize - 각피라미드 레벨에서 검색할 윈도우 크기 기본값(21,21)
# maxLevel - 최대 피라미드레벨 0이면 피라미드 사용안함 기본값 3
# criteria - (반복알고리즘의)종료기준
dst = cv2.addWeighted(src1, 0.5, src2, 0.5, 0)

# 출력코드
for i in range(pt2.shape[0]):
    if status[i, 0] == 0: # 잘못찾은 건 넘어가게
        continue

    cv2.circle(dst, tuple(pt1[i, 0].astype(int)), 4, (0, 255, 255), 2, cv2.LINE_AA)
    cv2.circle(dst, tuple(pt2[i, 0].astype(int)), 4, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.arrowedLine(dst, tuple(pt1[i, 0].astype(int)), tuple(pt2[i, 0].astype(int)), (0, 255, 0), 2)

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
