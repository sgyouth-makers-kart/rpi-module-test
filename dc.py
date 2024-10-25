from gpiozero import Motor
from time import sleep

forward=17
backward=27
# GPIO 핀 설정 (L298N의 IN1과 IN2를 GPIO 핀에 연결)
motor = Motor(forward=forward, backward=backward)

try:
    while True:
        speed = float(input("motor speed (0.0 ~ 1.0): "))
        direction = input("direction (f: forward, b: backward): ")

        if direction == 'f':
            print(f"forward with {speed*100}%")
            motor.forward(speed)
        elif direction == 'b':
            print(f"backward {speed*100}%")
            motor.backward(speed)
        else:
            print("'f' or  'b'")

        sleep_time = int(input("duration time (sec): "))
        sleep(sleep_time)

        motor.stop() 
        print("Motor stopped")

except KeyboardInterrupt:
    print("Exit!")
    motor.stop()

