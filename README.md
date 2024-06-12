# Pi Pico Soil Moisture Indicator

## Introduction
Welcome to the `Pi Pico Soil Moisture Indicator` project! This guide will show you how to create a practical soil moisture indicator for your indoor plants using the Raspberry Pi Pico and CircuitPython. This project automates the calibration process and provides a visually intuitive moisture indicator using a Neopixel LED display.

## What You'll Need
- Raspberry Pi Pico
- Sparkfun Soil Moisture Sensor
- WS2812B (aka Neopixel) ring or strip (16 LEDs recommended)
- Solid core wire
- Micro USB cable

**Note:** While this project uses a Raspberry Pi Pico, you can use any microcontroller that supports CircuitPython. Alternatives like the Adafruit QTPy could also be used.

## Setup Instructions

### Hardware Setup
1. **Trim and solder wires:** Make sure to trim and solder the wires according to your setup needs. For beginners, YouTube has excellent tutorials on soldering and wire trimming.
2. **Connect the components:** Follow the circuit diagram below to connect your components. Use short wires to keep your setup tidy, although longer wires can be used depending on your placement needs.

### CircuitPython Setup
1. **Install CircuitPython on your Raspberry Pi Pico:** Follow Adafruit’s detailed guide to get CircuitPython running on your Pi Pico.
2. **Download required libraries:** Download the CircuitPython library bundle and transfer the `neopixel.mpy` file into the `lib` folder on your Pi Pico.

### Software Installation
```python
# Copy and paste the following code into the `code.py` file on your Raspberry Pi Pico
import time
import board
import neopixel
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction, Pull

# Configuration and variables setup
[Insert the complete code provided earlier in the detailed project description]

# Save the file and ensure it's running by checking the output on your Neopixel display.
