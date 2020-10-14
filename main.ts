input.onButtonPressed(Button.A, function () {
    pins.digitalWritePin(DigitalPin.P1, 1)
    basic.pause(100)
    pins.digitalWritePin(DigitalPin.P1, 0)
    basic.pause(100)
    music.playTone(523, music.beat(BeatFraction.Whole))
    counter += 1
    basic.showNumber(counter)
    basic.pause(100)
})
input.onButtonPressed(Button.AB, function () {
    pins.digitalWritePin(DigitalPin.P1, 1)
    basic.pause(100)
    pins.digitalWritePin(DigitalPin.P1, 0)
    basic.pause(100)
    basic.showNumber(0)
    counter = 0
    music.playMelody("G A B C5 B C5 - - ", 300)
    basic.pause(100)
})
input.onButtonPressed(Button.B, function () {
    pins.digitalWritePin(DigitalPin.P1, 1)
    basic.pause(100)
    pins.digitalWritePin(DigitalPin.P1, 0)
    basic.pause(100)
    music.playTone(523, music.beat(BeatFraction.Whole))
    basic.showNumber(input.temperature())
    basic.pause(100)
})
input.onGesture(Gesture.Shake, function () {
    basic.showNumber(counter)
    basic.pause(100)
})
let moisture = 0
let counter = 0
let lights = neopixel.create(DigitalPin.P2, 30, NeoPixelMode.RGB)
music.setVolume(100)
basic.forever(function () {
    moisture = pins.analogReadPin(AnalogPin.P1)
    if (moisture > 1200) {
        basic.showIcon(IconNames.Surprised)
    } else if (moisture > 1000) {
        basic.showIcon(IconNames.Happy)
        lights.showRainbow(1, 360)
    } else {
        basic.showIcon(IconNames.Sad)
        lights.showColor(neopixel.colors(NeoPixelColors.Red))
    }
})
