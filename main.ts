// Enable one light (one pin)
// Disable all other pins
function redLight () {
    pins.digitalWritePin(DigitalPin.P0, 1)
    pins.digitalWritePin(DigitalPin.P1, 0)
    pins.digitalWritePin(DigitalPin.P2, 0)
}
function greenLight () {
    pins.digitalWritePin(DigitalPin.P0, 0)
    pins.digitalWritePin(DigitalPin.P1, 0)
    pins.digitalWritePin(DigitalPin.P2, 1)
}
input.onButtonPressed(Button.A, function () {
    basic.showString("R")
    AutoMode = 0
    redLight()
})
input.onButtonPressed(Button.AB, function () {
    AutoMode = 1
})
input.onButtonPressed(Button.B, function () {
    basic.showString("P")
    AutoMode = 0
    basic.pause(1000)
    yellowLight()
    basic.pause(1000)
    greenLight()
    basic.pause(5000)
    yellowLight()
    basic.pause(1000)
    redLight()
})
function yellowLight () {
    pins.digitalWritePin(DigitalPin.P0, 0)
    pins.digitalWritePin(DigitalPin.P1, 1)
    pins.digitalWritePin(DigitalPin.P2, 0)
}
let AutoMode = 0
redLight()
// When we start Microbit - automatically switch lights
AutoMode = 1
basic.forever(function () {
    if (AutoMode == 1) {
        basic.showString("A")
        redLight()
        basic.pause(5000 * AutoMode)
        yellowLight()
        basic.pause(1000 * AutoMode)
        greenLight()
        basic.pause(5000 * AutoMode)
        yellowLight()
        basic.pause(1000 * AutoMode)
        redLight()
    }
})
