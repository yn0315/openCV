import sys
import numpy as np
import cv2


# 영상 불러오기
src1 = cv2.imread('graf1.png', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('graf3.png', cv2.IMREAD_GRAYSCALE)

if src1 is None or src2 is None:
    print('Image load failed!')
    sys.exit()

# 특징점 알고리즘 객체 생성 (KAZE, AKAZE, ORB 등)
feature = cv2.KAZE_create()
#feature = cv2.AKAZE_create()
#feature = cv2.ORB_create()

# 특징점 검출 및 기술자 계산
kp1, desc1 = feature.detectAndCompute(src1, None)
kp2, desc2 = feature.detectAndCompute(src2, None)

# 특징점 매칭
matcher = cv2.BFMatcher_create()
# 특징점 매칭 알고리즘 객체 생성
# cv2.BFMatcher_create(, normType=None, crossCheck=None) -> retval
# normType - 특징점 기술자 거리 계산 방식 지정. 기본값은 cv2.NORM_L2
# crossCheck -  값이 True이면 양방향 매칭 결과가 같은 경우만 반환함 기본값은 false

# 특징점 검출 알고리즘 객체생성
# cv2.DescriptorMatcher.match(queryDescriptors, trainDescriptors, mask=None-> matches
# queryDescriptors - (기준 영상 특징점) 질의 기술자 행렬
# trainDescriptors - (대상 영상 특징점) 학습 기술자 행렬
# mask - 매칭 진행 여부를 지정하는 행렬 마스크
# matches - 매칭 결과. cv2.DMatch 객체의 리스트

# 특징점 검출 알고리즘 객체생성
# cv2.DescriptorMatcher.knnmatch(queryDescriptors, trainDescriptors, k,
#                                mask=None, compactResult=None) -> matches
# queryDescriptors - (기준 영상 특징점) 질의 기술자 행렬
# trainDescriptors - (대상 영상 특징점) 학습 기술자 행렬
# k - 질의 기술자에 대해 검출할 매칭 개수
# mask - 매칭 진행 여부를 지정하는 행렬 마스크
# compactResult - mask가 None이 아닐 때 사용되는 파라미터. 기본값은 False이며,
#                  경우 결과 matches는 기준 영상 특징점과 같은 크기를 가짐.
# matches - 매칭 결과. cv2.DMatch 객체의 리스트

# 특징점 매칭 결과 영상생성
# cv2.drawMatches(img1, keypoints1, img2, keypoints2, matches1to2, outImg,
#                 matchColor=None, singlePointColor=None, matchesMask=None, 
#                 flags=None) -> outImg
# img1, keypoints1 - 기준 영상과 기준 영상에서 추출한 특징점 정보
# img2, keypoints2 - 대상 영상과 대상 영상에서 추출한 특징점 정보
# matches1to2 - 매칭 정보. cv2.DMatch의 리스트
# outImg - 출력영상
# matchColor - 매칭된 특징점과 직선색상
# singlePointColor - 매칭되지 않은 특징점 색상
# matchesMask - 매칭정보를 선택하여 그릴 때 사용할 마스크
# flags - 매칭 정보 그리기 방법.기본값은 cv2.DRAW_MATCHES_FLAGS_DEFAULT.



#matcher = cv2.BFMatcher_create(cv2.NORM_HAMMING)
matches = matcher.match(desc1, desc2)

# 좋은 매칭 결과 선별
matches = sorted(matches, key=lambda x: x.distance)
good_matches = matches[:80] # 앞에 상위 80개

print('# of kp1:', len(kp1))
print('# of kp2:', len(kp2))
print('# of matches:', len(matches))
print('# of good_matches:', len(good_matches))

# 특징점 매칭 결과 영상 생성
dst = cv2.drawMatches(src1, kp1, src2, kp2, good_matches, None)

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
