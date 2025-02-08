from microbit import *
import neopixel

# Define the pins connected to the shift register
serial_out = pin0
parallel_load = pin1
clock = pin2

# Number of buttons (8 for an 8-bit shift register)
NUM_BUTTONS = 8

# Number of NeoPixels (if 5 pixels, set to 4)
NUM_PIXELS = 5

# Define custom images for directions
DOWN_DPAD = Image("00000:"
                  "00000:"
                  "99999:"
                  "09990:"
                  "00900")
UP_DPAD = Image("00900:"
                "09990:"
                "99999:"
                "00000:"
                "00000")
LEFT_DPAD = Image("00900:"
                  "09900:"
                  "99900:"
                  "09900:"
                  "00900")
RIGHT_DPAD = Image("00900:"
                   "00990:"
                   "00999:"
                   "00990:"
                   "00900")

# Button to character mapping
button_chars = ['R', 'L', RIGHT_DPAD, UP_DPAD, LEFT_DPAD, DOWN_DPAD, 'Y', 'X']

# Maps each button index to a (x, y) coordinate on the micro:bit display (for the pixel array display mode)
button_to_led_mapping = [
    (0, 0),  # Button 0 maps to row 0, column 0
    (1, 0),  # Button 1 maps to row 1, column 0
    (2, 0),  # Button 2 maps to row 2, column 0
    (3, 0),  # Button 3 maps to row 3, column 0
    (4, 0),  # Button 4 maps to row 4, column 0
    (0, 1),  # Button 5 maps to row 0, column 1
    (1, 1),  # Button 6 maps to row 1, column 1
    (2, 1)   # Button 7 maps to row 2, column 1
]

# Initialize the NeoPixel strip on pin 1
np = neopixel.NeoPixel(pin1, NUM_PIXELS)

# Function to get RGB values from the color wheel
def wheel(pos):
    pos = pos % 255  # Ensure pos is always within 0-254
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    else:
        pos -= 170
        return (pos * 3, 0, 255 - pos * 3)

# Function to set the color of the pixels
def set_color(pixel_index, r, g, b):
    np[pixel_index] = (r, g, b)
    np.write()
    
    # Function to read button states from the shift register
def read_shift_register():
    # Pulse the parallel load to load the button states into the shift register
    parallel_load.write_digital(0)
    parallel_load.write_digital(1)
    
    # Read the serial output from the shift register
    button_states = 0
    for i in range(NUM_BUTTONS):
        clock.write_digital(0)
        button_states |= (serial_out.read_digital() << (NUM_BUTTONS - 1 - i))
        clock.write_digital(1)
    
    # Debounce delay (might not be necessary)
    # sleep(5)
    
    return button_states

# Check the state of the buttons and display the corresponding image, with display priority to the LEFT_DPAD
def check_buttons_with_large_display():
    button_states = read_shift_register()
    left_dpad_index = button_chars.index(LEFT_DPAD)  # Get the index for LEFT_DPAD in button_chars

    # First, check if the LEFT_DPAD button is pressed
    if button_states & (1 << left_dpad_index):
        display.show(LEFT_DPAD)
    else:
        # If LEFT_DPAD is not pressed, check other buttons
        for i in range(NUM_BUTTONS):
            if button_states & (1 << i):
                display.show(button_chars[i])
                break
        else:
            display.clear()

    # Check for button A and B presses on the micro:bit
    if button_a.is_pressed():
        display.show('A')
    elif button_b.is_pressed():
        display.show('B')


def check_buttons_with_pixel_array():
    button_states = read_shift_register()
    display.clear()  # Clear the display at the start of each check
    for i in range(NUM_BUTTONS):
        # Determine if each button is pressed (bit is high)
        if button_states & (1 << i):
            # Find the LED position for this button
            x, y = button_to_led_mapping[i]
            display.set_pixel(x, y, 9)  # Set brightness to maximum (9)

    # Additional checks for micro:bit's built-in buttons
    if button_a.is_pressed():
        display.set_pixel(0, 4, 9)  # Indicate button A is pressed
    if button_b.is_pressed():
        display.set_pixel(4, 4, 9)  # Indicate button B is pressed
    
# Function to fade through the rainbow with adjustable brightness
def rainbow_pixels(steps=255, delay=15, brightness=0.25):
    for step in range(steps):
        r, g, b = wheel(step)
        # Scale the RGB values by the brightness factor
        r = int(r * brightness)
        g = int(g * brightness)
        b = int(b * brightness)
        for i in range(NUM_PIXELS):
            set_color(i, r, g, b)

        check_buttons_with_large_display()
        sleep(delay)

while True:
    rainbow_pixels()