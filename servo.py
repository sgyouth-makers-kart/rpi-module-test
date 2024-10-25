from gpiozero import Servo
from time import sleep

# 각도 변환을 위한 상수
MIN_ANGLE = 0    # 최소 각도
MAX_ANGLE = 180  # 최대 각도
MIN_SERVO = -1   # 서보의 최소 위치 (-1)
MAX_SERVO = 1    # 서보의 최대 위치 (1)

# GPIO 14번 핀에 서보 모터 연결
servo = Servo(14)

def angle_to_value(angle):
    # 각도를 -1 ~ 1 범위로 변환
    return (angle - MIN_ANGLE) * (MAX_SERVO - MIN_SERVO) / (MAX_ANGLE - MIN_ANGLE) + MIN_SERVO

try:
    while True:
        # 원하는 각도를 입력받음
        angle = float(input("원하는 각도를 입력하세요 (0 ~ 180): "))
        if 0 <= angle <= 180:
            # 각도를 서보 모터의 위치 값으로 변환
            value = angle_to_value(angle)
            servo.value = value
            print(f"서보를 {angle}도로 회전")
        else:
            print("각도는 0에서 180 사이로 입력하세요.")

except KeyboardInterrupt:
    print("프로그램 종료")

