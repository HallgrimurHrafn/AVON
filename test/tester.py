



def test(x):
    glo.trellis.setLED(x)
    glo.trellis.writeDisplay()
    time.sleep(2)
    glo.trellis.clrLED(x)
    glo.trellis.writeDisplay()
