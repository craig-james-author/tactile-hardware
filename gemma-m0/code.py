"""CircuitPython Essentials Capacitive Touch example"""
import time
import board
import digitalio
import touchio
from analogio import AnalogOut

touch_pad = board.A1  # Will not work for Circuit Playground Express!

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led_cycle = 0;

touch = touchio.TouchIn(touch_pad)
analog_out = AnalogOut(board.A0)
analog_factor = 60

offset = 0.0;
for i in range(100):
    offset += touch.raw_value
offset /= 100.0
offset = int(offset + 0.5)

print("Initial offset: ", offset)

filtered_value = offset;
n = 0;
while True:
    filtered_value = touch.raw_value; # /100.0 + filtered_value*0.99
    output = (int(filtered_value) - offset) * analog_factor
    if output < 0:
        output = 0
    elif output > 65535:
        output = 65535
    analog_out.value = output;
#    if n % 25 == 0:
#        print ("filtered: ", filtered_value, ", output: ", output);
#    time.sleep(0.01)
    led_percent = int(output * 100.0 / 65536.0)
    if led_cycle < led_percent:
        led.value = True
    else:
        led.value = False
    led_cycle += 1;
    if led_cycle > 99:
        led_cycle = 0
    n += 1
