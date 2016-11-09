    #!/usr/bin/env python
import time
import serial
import pygame
import mido   # info fyrir mido. https://mido.readthedocs.io/en/latest/ports.html
import struct

ser = serial.Serial(
    port='/dev/serial1', # thetta er serialportid a raspberry.
    baudrate = 115200,
    parity=serial.PARITY_NONE,       # latum RS3232 sja um thetta.
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    xonxoff=False,
    rtscts=False,
    dsrdtr=False
    # timeout=0
    )
#counter =0

if ser.isOpen():                            #sjaum hvort portid se opid
    print "Port already open"
else:                                       #annars opnar thetta thad
    print "Opening Port:"

while 1:
    # thurfum ekki ad senda output relentlessly
    time.sleep(1)
    # til oryggist taemum inputtid
    ser.flushInput()
    # ser.write skilar fjolda bytes svo x er ad sja hvort thad se ekki verid ad senda
    # rettan fjolda bita. endar a .hex til ad koda thetta i formati fyrir serial.
    # lika haegt ad prufa .bin(), prufa ad sleppa, og mogulega bytearray. oll foll sem skila
    # a byte formati.
    # docs segir til um thetta og margt tengt thessu, maeli med thvi ad lesa hann til hlidsjonar.
    # docs fyrir serial https://pythonhosted.org/pyserial/pyserial_api.html?highlight=serial.write#serial.Serial.write
    x=ser.write(mido.Message('note_on', channel=0, note=60, velocity=100).hex())
    ser.flush()  # hreinsum aftur
    # debug, hvert var message-id adur en thad for i ser.write
    # prentar lika x fyrir debug
    print(mido.Message('note_on', channel=0, note=60, velocity=100).hex())
    print(x)
    # in case ad thetta virkadi endurtokum nema vid slokkvum a notunni. hun lifir i sekundu
    time.sleep(1)
    ser.flushInput()
    x=ser.write(mido.Message('note_off', channel=0, note=60, velocity=0).hex())
    ser.flush()
    print(mido.Message('note_off', channel=0, note=60, velocity=0).hex())
    print(x)



    # Man ekki hvernig en thad er lika haegt ad reyna ad senda serial merkid beint
    # an thess ad nota mido.message.  thad er vesen samt. en ef thid reynid thad
    # tha er mikilvaegt ad senda rett skilabod.

    # https://www.midi.org/specifications/item/table-1-summary-of-midi-message
    # ^ midi message info.

    # eg reyndi lika ad nota mido.get_output_names() en thad sagdi mer ad output
    # portid a raspberry vaeri [u'Midi Through Port-0'] sem meikar 0 sense.

    # annad en thetta tha veit eg ekki hvad gaeti verid malid :S.


    # lika haegt ad reyna ad leita ad odrum leidum til ad senda outputtid ut. hef hinsvegar ekkert fundid.
