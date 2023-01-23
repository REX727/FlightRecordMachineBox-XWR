basic.forever(function on_forever() {
    basic.showLeds(`
        # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
    `)
    basic.showLeds(`
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    `)
})
basic.forever(function on_forever2() {
    datalogger.log(datalogger.createCV("x", input.acceleration(Dimension.X)))
    basic.pause(100)
})
basic.forever(function on_forever3() {
    datalogger.log(datalogger.createCV("y", input.acceleration(Dimension.Y)))
    basic.pause(100)
})
basic.forever(function on_forever4() {
    datalogger.log(datalogger.createCV("z", input.acceleration(Dimension.Z)))
    basic.pause(100)
})
