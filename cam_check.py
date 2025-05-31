import cv2
cap = cv2.VideoCapture(0)
if cap.isOpened():
    print("✅ 카메라 연결 성공")
else:
    print("❌ 카메라 연결 실패")
cap.release()