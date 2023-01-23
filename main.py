def on_forever():
    basic.show_leds("""
        # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
basic.forever(on_forever)

def on_forever2():
    datalogger.log(datalogger.create_cv("x", input.acceleration(Dimension.X)))
    basic.pause(100)
basic.forever(on_forever2)

def on_forever3():
    datalogger.log(datalogger.create_cv("y", input.acceleration(Dimension.Y)))
    basic.pause(100)
basic.forever(on_forever3)

def on_forever4():
    datalogger.log(datalogger.create_cv("z", input.acceleration(Dimension.Z)))
    basic.pause(100)
basic.forever(on_forever4)
