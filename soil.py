import time
import board
import neopixel
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction, Pull

# how frequently to take readings
DELAY = 600

# Update this to match the number of NeoPixel LEDs connected to your board.
num_pixels = 16

# setup the moisture sensor power pin and turn it off by default
sensor_power = DigitalInOut(board.GP7)
sensor_power.direction = Direction.OUTPUT
sensor_power.value = False

# set the analog read pin for the moisture sensor
sensor_signal = AnalogIn(board.GP27)

# set up the noepixels
pixels = neopixel.NeoPixel(board.GP2, num_pixels, auto_write=False)
pixels.brightness = 0.2

# some variables for internal use, you shouldn't have to worry about them
calibrate_count = 0
auto_calibrate = True
SENSOR_MAX = 0
SENSOR_MIN = 9999

# set the neopixels to blue
for i in range(num_pixels):
    pixels[i] = (0,0,255)
pixels.show()

print("=============")
print("calibrating sensor")
print("=============\n\n")

while True:

    if auto_calibrate == True:

        # enable the sensor power
        sensor_power.value = True

        # take a reading from the sensor and make it a little easier to read
        value = round(sensor_signal.value / 100)

        # disable the sensor power
        sensor_power.value = False

        print("reading:", value)

        if value > SENSOR_MAX:
            SENSOR_MAX = value

        if value < SENSOR_MIN:
            SENSOR_MIN = value

        calibrate_count += 1

        if(calibrate_count > 100):
            print("\n-------------------")
            print("MIN:", SENSOR_MIN)
            print("MAX:", SENSOR_MAX)
            print("-------------------\n")
            time.sleep(5)

            # wipe pixels
            for i in range(num_pixels):
                pixels[i] = (0,0,0)
            pixels.show()

            auto_calibrate = False

        time.sleep(0.2)

    else:

        # take a reading from the sensor and make it a little easier to read
        value = round(sensor_signal.value / 100)
        print("reading:", value)

        # disable the sensor power
        sensor_power.value = True

        # crazy math to turn value into percentage
        percent = round(((value - SENSOR_MIN) / (SENSOR_MAX - SENSOR_MIN)) * 100)
        print("Percent:", percent)

        # more crazy math to convert percentage to number of pixels
        show_leds = round(100 / (100 / num_pixels) * percent / 100)
        print("leds to show:", show_leds)

        # print values for the plotter
        print((value, percent, show_leds))

        # change colour depending on quantity
        if(show_leds < 8):
            color = (255,0,0)
        else:
            color = (0,255,0)

        # make sure we don't ever try to show more leds than we have
        # because that will crash the script
        if(show_leds > num_pixels):
            show_leds = num_pixels

        # if water levels are critically low, show them all
        if(show_leds <= 3):
            show_leds = num_pixels

        # wipe pixels
        for i in range(num_pixels):
            pixels[i] = (0,0,0)

        # turn on neopixels
        for i in range(show_leds):
            pixels[i] = color

        pixels.show()

        # wait for required delay
        time.sleep(DELAY)

        print("\n-------------------\n")
