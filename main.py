def on_button_pressed_a():
    global counter
    pins.digital_write_pin(DigitalPin.P1, 1)
    basic.pause(100)
    pins.digital_write_pin(DigitalPin.P1, 0)
    basic.pause(100)
    music.play_tone(523, music.beat(BeatFraction.DOUBLE))
    counter += 1
    basic.show_number(counter)
    basic.pause(100)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global counter
    for index in range(3):
        pins.digital_write_pin(DigitalPin.P1, 1)
        basic.pause(100)
        pins.digital_write_pin(DigitalPin.P1, 0)
        basic.pause(100)
    basic.show_number(0)
    counter = 0
    music.play_melody("G A B C5 B C5 - - ", 300)
    basic.pause(100)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    pins.digital_write_pin(DigitalPin.P1, 1)
    basic.pause(100)
    pins.digital_write_pin(DigitalPin.P1, 0)
    basic.pause(100)
    music.play_tone(523, music.beat(BeatFraction.DOUBLE))
    basic.show_number(input.temperature())
    basic.pause(100)
input.on_button_pressed(Button.B, on_button_pressed_b)

moisture = 0
counter = 0
lights = neopixel.create(DigitalPin.P2, 30, NeoPixelMode.RGB)

def on_forever():
    global moisture
    music.set_volume(30)
    led.set_brightness(255)
    moisture = pins.analog_read_pin(AnalogPin.P1)
    if moisture > 1200:
        basic.show_icon(IconNames.SURPRISED)
    elif moisture > 1000:
        basic.show_icon(IconNames.HAPPY)
        lights.show_rainbow(1, 360)
    else:
        basic.show_icon(IconNames.SAD)
        music.play_tone(523, music.beat(BeatFraction.DOUBLE))
        music.play_tone(494, music.beat(BeatFraction.DOUBLE))
        music.play_tone(523, music.beat(BeatFraction.DOUBLE))
        music.play_tone(494, music.beat(BeatFraction.DOUBLE))
        basic.pause(1000)
        lights.show_color(neopixel.colors(NeoPixelColors.RED))
basic.forever(on_forever)
