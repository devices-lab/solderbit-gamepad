solderbit_gamepad.onButtonPressed(solderbit_gamepad.GamepadButton.North, function () {
    basic.showArrow(ArrowNames.North, 0)
})
solderbit_gamepad.onButtonReleased(solderbit_gamepad.GamepadButton.West, function () {
    basic.clearScreen()
})
solderbit_gamepad.onButtonReleased(solderbit_gamepad.GamepadButton.LeftBumper, function () {
    basic.clearScreen()
})
solderbit_gamepad.onButtonReleased(solderbit_gamepad.GamepadButton.X, function () {
    basic.clearScreen()
})
solderbit_gamepad.onButtonPressed(solderbit_gamepad.GamepadButton.East, function () {
    basic.showArrow(ArrowNames.East, 0)
})
solderbit_gamepad.onButtonPressed(solderbit_gamepad.GamepadButton.X, function () {
    basic.showString("X", 0)
})
solderbit_gamepad.onButtonReleased(solderbit_gamepad.GamepadButton.Y, function () {
    basic.clearScreen()
})
solderbit_gamepad.onButtonPressed(solderbit_gamepad.GamepadButton.West, function () {
    basic.showArrow(ArrowNames.West, 0)
})
solderbit_gamepad.onButtonReleased(solderbit_gamepad.GamepadButton.North, function () {
    basic.clearScreen()
})
solderbit_gamepad.onButtonPressed(solderbit_gamepad.GamepadButton.RightBumper, function () {
    basic.showString("R", 0)
})
solderbit_gamepad.onButtonReleased(solderbit_gamepad.GamepadButton.RightBumper, function () {
    basic.clearScreen()
})
solderbit_gamepad.onButtonReleased(solderbit_gamepad.GamepadButton.East, function () {
    basic.clearScreen()
})
solderbit_gamepad.onButtonPressed(solderbit_gamepad.GamepadButton.Y, function () {
    basic.showString("Y", 0)
})
solderbit_gamepad.onButtonPressed(solderbit_gamepad.GamepadButton.South, function () {
    basic.showArrow(ArrowNames.South, 0)
})
solderbit_gamepad.onButtonPressed(solderbit_gamepad.GamepadButton.LeftBumper, function () {
    basic.showString("L", 0)
})
solderbit_gamepad.onButtonReleased(solderbit_gamepad.GamepadButton.South, function () {
    basic.clearScreen()
})
let hue = 0
let pixelHue = 0
let SEPARATION = 90
let HUE_STEP = 1
let WAIT_MICROS = 20
let BRIGHTNESS = 32
solderbit_gamepad.solderbitPixels().setBrightness(BRIGHTNESS)
solderbit_gamepad.solderbitPixels().clear()
let numPixels = solderbit_gamepad.solderbitPixels().length()
basic.forever(function () {
    for (let i = 0; i <= numPixels - 1; i++) {
        pixelHue = (hue + Math.idiv(i * SEPARATION, numPixels)) % 360
        solderbit_gamepad.solderbitPixels().setPixelColor(i, neopixel.hsl(pixelHue, 99, 50))
    }
    solderbit_gamepad.solderbitPixels().show()
    hue = (hue + HUE_STEP) % 360
    control.waitMicros(WAIT_MICROS)
})
