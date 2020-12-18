# Enable one light (one pin)
# Disable all other pins
def redLight():
    pins.digital_write_pin(DigitalPin.P0, 1)
    pins.digital_write_pin(DigitalPin.P1, 0)
    pins.digital_write_pin(DigitalPin.P2, 0)
def greenLight():
    pins.digital_write_pin(DigitalPin.P0, 0)
    pins.digital_write_pin(DigitalPin.P1, 0)
    pins.digital_write_pin(DigitalPin.P2, 1)

def on_button_pressed_a():
    global AutoMode
    basic.show_string("R")
    AutoMode = 0
    redLight()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global AutoMode
    AutoMode = 1
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global AutoMode
    basic.show_string("P")
    AutoMode = 0
    basic.pause(1000)
    yellowLight()
    basic.pause(1000)
    greenLight()
    basic.pause(5000)
    yellowLight()
    basic.pause(1000)
    redLight()
input.on_button_pressed(Button.B, on_button_pressed_b)

def yellowLight():
    pins.digital_write_pin(DigitalPin.P0, 0)
    pins.digital_write_pin(DigitalPin.P1, 1)
    pins.digital_write_pin(DigitalPin.P2, 0)
AutoMode = 0
redLight()
# When we start Microbit - automatically switch lights
AutoMode = 1

def on_forever():
    if AutoMode == 1:
        basic.show_string("A")
        redLight()
        basic.pause(5000)
        yellowLight()
        basic.pause(1000)
        greenLight()
        basic.pause(5000)
        yellowLight()
        basic.pause(1000)
        redLight()
basic.forever(on_forever)
