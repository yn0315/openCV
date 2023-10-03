# 기본적인 2D 필터링
# cv2.filter2D(src, ddepth, kernel, dst=None, anchor=None, delta=None,borderType=None) -> dst

# src - 입력영상
# ddepth - 출력 영상 데이터타입 /  (e.g) cv2.CV_8U, cv2.CV_32F, cv2.CV_64F
#          -1을 지정하면 src와 같은 타입의 dst 영상을 생성
# kernel - 필터마스크 행렬 실수형
# anchor - 고정점 위치(-1,-1)이면 필터 중앙을 고정점으로 사용
# delta - 추가적으로 더할 값
# borderType - 가장자리 픽셀 확장방식
# dst - 출력영상
