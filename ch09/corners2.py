# 해리스코너 응답함수계산
# cv2.cornerHarris(src, blockSize, ksize, k, dst=None, borderType=None) -> dst
# src - 입력 단일채널 8비트 또는 실수형 영상
# blockSize - 코너 응답 함수 계산에서 고려할 이웃 픽셀 크기. 보통 2~5
# ksize - (미분을 위한) 소벨 연산자를 위한 커널 크기. 보통 3
# k - 해리스 코너 검출 상수 (보통 0.04~0.06)
# dst - 해리스 코너 응답 계수. src와 같은 크기의 행렬(numpy.ndarray) dtype=numpy.float32
# borderType - 가장자리 픽셀 확장 방식. 기본값은 cv2.BORDER_DEFAULT

# 추적하기 좋은 특징 코너 검출
# cv2.goodFeaturesToTrack(image, maxCorners, qualityLevel, minDistance,
#                         corners=None, mask=None, blockSize=None,
#                         useHarrisDetector=None, k=None) -> corners
# image - 8비트 또는 32비트 실수, 단일채널 영상
# maxCorners - 최대 코너 개수. maxCorners <=0 이면 무제한.
# qualityLevel - 코너점 결정을 위한 값. 보통 0.01 ~ 0.1
# minDistance - 코너점 사이의 최소 거리
# corners - 검출된 코너점 좌표. numpy.ndarray. shape=(N, 1, 2). dtype=numpy.float32
# mask - 마스크 영상
# blockSize - 코너 검출을 위한 블록 크기. 기본값은 3.
# useHarrisDetector - 해리스 코너 방법 사용 여부. 기본값은 False.
# k - 해리스 코너 검출 시 사용할 k 값