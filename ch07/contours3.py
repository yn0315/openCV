# 외곽선함수

# 외곽선길이구하기
# cv2.arcLength(curve, closed) -> retval
# curve - 외곽선 좌표. numpy.ndarray. shape=(K, 1, 2)
# closed - True이면 폐곡선으로 간주
# retval - 외곽선길이

# 면적구하기
# cv2.contourArea(contour, oriented=None) -> retval
# countour - 외곽선 좌표. numpy.ndarray. shape=(K, 1, 2)
# oriented - True이면 외곽선 진행 방향에 따라 부호 있는 면적을 반환 기본값 false
# retval - 외곽선으로 구성된 영역의 면적

# 바운딩박스(외곽선을 외접하여 둘러싸는 가장 작은 사각형) 구하기
# cv2.boundingRect(array) -> retval
# array - 외곽선 좌표. numpy.ndarray. shape=(K, 1, 2)
# retval - 사각형정보(x,y,w,,h)튜플

# 바운딩서클클(외곽선을 외접하여 둘러싸는 가장 작은 원) 구하기
# cv2.minEnclosingCircle(points) -> center, radius
# points - 외곽선좌표 numpy.ndarray. shape=(K, 1, 2)
# center - 바운딩 서클 중심 좌표. (x, y) 튜플
# radius - 바운딩 서클 반지름. 실수.

# 외곽선 근사화
# cv2.approxPolyDP(curve, epsilon, closed, approxCurve=None) -> approxCurve
# curve - 입력 곡선 좌표. numpy.ndarray. shape=(K, 1, 2)
# epsilon - 근사화 정밀도 조절. 입력 곡선과 근사화 곡선 간의 최대 거리.e.g) cv2.arcLength(curve) * 0.02
# closed - True를 전달하면 폐곡선으로 인식
# approxCurve - 근사화된 곡선 좌표. numpy.ndarray. shape=(K', 1, 2)

# convex 검사
# cv2.isContourConvex(contour) -> retval
# contour - 입력 곡선 좌표. numpy.ndarray. shape=(K, 1, 2)
# retcal - 컨벡스이면 True, 아니면 False.
