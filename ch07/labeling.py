import sys
import numpy as np
import cv2


mat = np.array([
    [0, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 1, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]], np.uint8)

# cnt, labels = cv2.connectedComponents(mat)
cnt, labels, stats,centroids = cv2.connectedComponentsWithStats(mat)
# 레이블링 함수
# cv2.connectedComponents(image, labels=None, connectivity=None,ltype=None) -> retval, labels
# image - 8비트 1채널영상
# labels - 레이블 맵 행렬 . 입력 영상과 같은 크기. numpy.ndarray
# connectivity - 4 또는 8 기본값은 8
# ltype - labels 타입 cv2.CV_32S 또는 cv2.CV_16S. 기본값은 cv2.CV_32S
# retval - 객체 개수. N을 반환하면 [0, N-1]의 레이블이 존재 하며,0은 배경을 의미. (실제 흰색 객체 개수는 N-1개)
 
# 객체정보를 함께 반환하는 레이블링 함수 - 더 많이 사용
# cv2.connectedComponentsWithStats(image, labels=None, stats=None,
#                                  centroids=None, connectivity=None, ltype=None)
#                                  -> retval, labels, stats, centroids
# image - 8비트 1채널영상
# labels - 레이블 맵 행렬 . 입력 영상과 같은 크기. numpy.ndarray
# stats - 각 객체의 바운딩 박스, 픽셀 개수 정보를 담은 행렬.
#         numpy.ndarray. shape=(N, 5), dtype=numpy.int32
# centroids - 각 객체의 무게 중심 위치 정보를 담은 행렬
#             numpy.ndarray. shape=(N, 2), dtype=numpy.float64
# ltype - labels 행렬 타입. cv2.CV_32S 또는 cv2.CV_16S. 기본값은 cv2.CV_32S
print('sep:', mat, sep='\n')
# print('cnt:', cnt)
# print('labels:', labels, sep='\n')


print("lables: ", labels, sep='\n')
print("stats: ", stats, sep='\n')
print("centroids: ", centroids, sep='\n')
print("retval: ", cnt)
