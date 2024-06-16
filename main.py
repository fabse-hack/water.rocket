from machine import Pin, I2C, PWM
from time import sleep
import ADXL345
import machine
import time
import neopixel
import uasyncio as asyncio

# Datei vom Microcontroller kopieren mit mpremote:
# python.exe -m mpremote connect com7 cp :sensor.txt C:\Austausch\

# ADXL345
i2cadx = I2C(scl=Pin(5),sda=Pin(4), freq=400000)
adx = ADXL345.ADXL345(i2cadx)

#neopixel
np = neopixel.NeoPixel(machine.Pin(13), 1)

# Servo
servo = PWM(Pin(14), freq=50, duty=77)

async def sensordata():
    while True:
        x_adx = adx.xValue
        y_adx = adx.yValue
        z_adx = adx.zValue

        #Schreiben der Werte in die Datei sensor.txt
        with open('sensor.txt', 'a') as file:
            ticks_millis = time.ticks_ms()
            milliseconds = ticks_millis % 1000
            seconds_total = ticks_millis // 1000
            seconds = seconds_total % 60
            minutes_total = seconds_total // 60
            minutes = minutes_total % 60
            hours = minutes_total // 60
            file.write(f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d} ,")
            file.write("X_adx: {:.2f}, Y_adx: {:.2f}, Z_adx: {:.2f}\n".format(x_adx, y_adx, z_adx))

def buzzer():
    while True:
        zz_adx = adx.zValue
        if abs(zz_adx) < 10: 
            buzzer = PWM(Pin(12), freq=240, duty=300)
            sleep(0.5)
            buzzer.deinit()

def servo():
    while True:
        zzz_adx = adx.zValue
        if 0 <= zzz_adx <= 170:
            servo.duty(122)

async def main():
    task1 = asyncio.create_task(sensordata())
    task2 = asyncio.create_task(buzzer())
    task3 = asyncio.create_task(servo())
    await asyncio.gather(task1, task2, task3)

if __name__ == "__main__":
    np[0] = (255, 0, 0)
    np.write()
    servo.duty(122)
    sleep(2)
    servo.duty(30)
    asyncio.run(main())
