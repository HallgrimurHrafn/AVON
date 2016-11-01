# playcolumn begins --- spilar notur i dalk og takt maelinn lika.

import time
import threading
import numpy as np
import RPi.GPIO as GPIO

import Adafruit_Trellis         # trellis config
matrix0 = Adafruit_Trellis.Adafruit_Trellis()
matrix1 = Adafruit_Trellis.Adafruit_Trellis()
matrix2 = Adafruit_Trellis.Adafruit_Trellis()
matrix3 = Adafruit_Trellis.Adafruit_Trellis()
trellis = Adafruit_Trellis.Adafruit_TrellisSet(
    matrix0, matrix1, matrix2, matrix3
    )
I2C_BUS = 1
trellis.begin(
    (0x70,  I2C_BUS),
    (0x71, I2C_BUS),
    (0x72, I2C_BUS),
    (0x73, I2C_BUS)
    )

# nonmenu config
tkt=False                       # hvort ljosin fra taktmaelinum seu i gangi.
dlk=0                           # hvada dalkur er i spilun.
voice = 0                       # hvada voice er i notkun
mwGO = 0                        # hvort vid erum i modwatch eda ekki
tGO = 0                         # hvort breyta megi status eda ekki
mcGo = 0                        # hvort modda megi med myndavel eda ekki
status = np.zeros((8, 8, 16))   # status notna fylkid okkar
tStatus = np.zeros((8, 8, 16))  # tStatus, temporarystatus. notad thegar
                                # tgo=0 svo vid missum ekki af notum
#

# menu
v=0                             # styring fyrir hvada voice vid aetlum a fara i.
clA = 0                         # ef clA=1 tha gerum vid clearAll
lGO = 0                         # ef lgo=1 tha erum vid i life mode.
pause = 1                       # eigum vid ad pause-a
stop = 0                        # eigum vid ad stoppa
skali = np.array([72, 71, 69, 67, 65, 64, 62, 60])  # skali, segir sig sjalfur,
# save og loada skala :S                        tharf ad vera i minnkandi rod!.
tempo = 0.5  # 0.05 er min.     #tempo
FLASH = 0.9 * tempo             # hlutfallsleg lengd af tempo fyrir taktmaeli
lengd = 0.1                     # hlutfall tempo, bil milli enda og byrjunar
# save einhvern veginn              notna i samliggjandi dalkum.
# load einhvern veginn


def playColumn(dalkur):
    global tempo, FLASH, lengd                              # global breytur, utskyrdar efst.
    t1 = threading.Thread(target=NOTEON, args=(dalkur,))    # buum til thrad til ad og keyrum NOTEON
    t1.start()                                              # thannig er taktmaelirinn nakvaemari

    time.sleep(tempo - tempo * lengd)                       #tempo*lengd er hve mikill timi er eftir thegar notan klarast

    t3 = threading.Thread(target=NOTEOFF, args=(dalkur,))   # thad sama fyrir NOTEOFF
    t3.start()

    time.sleep(tempo * lengd)                               # timinn milli lok notu og upphaf naestu.
# playColumn ends		--- finna ut hvernig a ad deala vid mismunandi takta notna.


# NOTEON begins
def NOTEON(dalkur):
    global tGO, skali, status, mcGo                         # global breytur, utskyrdar efst.
    tGO = 0                                                 # tGO=0, trelliswatch ma ekki breyta status.
    for x in range(0, 8):
        for v in range(0, 16):                              # fyrir allar notur dalksins spilum..
            if status[dalkur][x][v] == 1:
                # midiout.send_message(mido.Message('note_on', channel=voice,
                # note=skali(x), velocity=100).bytes())  #velocity=mod(dalkur,
                # x, v, 0)
                print('on', 'channel er', v,
                'notan er', skali[x], 'velocity er', 100)
    tGO = 1                                                 # tGO=1, trelliswatch ma breyta status
    mcGO = 1                                                # mcGO=1, her ma modda notur
    taktmaelir(dalkur)                                      # forum i taktmaelinn.
# NOTEON ends


# NOTEON begins
def NOTEOFF(dalkur):
    global tGO, skali, status, mcGO
    tGO = 0                                                 # tGO=0, trelliswatch ma ekki breyta status.
    mcGO = 0                                                # slekkur a modColumn, bannad ad modda notur
    for x in range(0, 8):
        for v in range(0, 16):                              # slokkvum a notunum sem vid kveiktum a adan.
            if status[dalkur][x][v] == 1:
                #midiout.send_message(mido.Message('note_off', channel=voice, note=skali(x), velocity=0).bytes())
                print('off', 'channel er', v,
                      'notan er', skali[x], 'velocity er', 0)
                pass
                                                            # eini munurinn a thessu og sidasta er ad message-id er note_off og velocity er 0.
                                                            # velocity er valid 0 vegna thess ad sum midi hljodfaeri nota
                                                            # ekki message-id note off heldur bara velocity 0.
    tGO = 1                                                 # kveikir a trellisWatch.
# NOTEON ends


# taktmaelir begins
def taktmaelir(dalkur):
    global FLASH, status, voice, tkt                        # global breytur, utskyrdar efst.
    tkt = True
    for x in range(0, 8):                                   # fyrir oll LED i 'dalkur'
        trellis.setLED(tfOut(x * 8 + dalkur))               # kveikja a LED!,tfout varpar i trellisformat.
        #print(x*8+dalkur,tfOut(x*8+dalkur), 'on')
    trellis.writeDisplay()                                  # uppfaera led a bordi.. VERDI LJOS!
    time.sleep(FLASH)                                       # bidtimi eftir taktmaelis flash.
    for x in range(0, 8):                                   # fyrir oll LED i 'dalkur'
        if status[dalkur][x][voice] == 0:                   # slokkvum a theim ljosum sem eru ekki a bordinu fyrir.
            trellis.clrLED(tfOut(x * 8 + dalkur))
    trellis.writeDisplay()                                  # uppfaera led a bordi.. VERDI MYRKUR!
    tkt=False
# taktmaelir end


# tfIn begins 		--- varpar ur trellis i okkar format.
def tfIn(a):
    f = a // 16                                             # thetta er bara sma formula sem varpar
    d = (a % 16) % 4                                        # fylki ur trellis formati i status format.
    l = (a % 16) // 4
    if f % 2 == 0:
        b = 16 * f + 8 * l + d
    else:
        b = 16 * (f + 1) - (3 - l) * 8 + d - 4
    return b
# tfIn ends


# tfOut begins 		--- varpar ur okkar formati i trellis.
def tfOut(a):
    f = a // 16
    d = (a % 16) % 8                                        # thetta er bara sma formula sem varpar
    l = (a % 16) // 8                                       # fylki ur status formati i trellis format.
    if d < 4:
        if f < 2:
            b = 8 * f + 4 * l + d
        else:
            if f == 2:
                b = 32 + 4 * l + d
            else:
                b = 40 + d + 4 * l
    else:
        if f % 2 == 1:
            b = 16 * (f + 1) + d - 4 * (3 - l)
        else:
            b = 16 * (f + 1) + d - 4 * (3 - l) + 8
    return b
# tfOut ends


# SEQUENCER LOOP, THIS IS IT YO GUYS:
def Sequencer():
    global dlk, pause, stop                                 # til ad halda utanum hvar vid erum.
    while True:
        if stop == 0:                                       # ef ytt var a pause tha leyfum vid sequencer-inum ekki ad spila.
            for dalkur in range(0, 8):                      # fyrir alla dalka i sequencer.
                dlk=dalkur                                  #uppfaerum dlk
                While pause == 1:
                    time.sleep(0.1)
                playColumn(dalkur)                          # spila notur dalks auk bid og taktmaelis.
                if stop == 1:
                    break
        while pause == 1:
            time.sleep(0.1)
# SEQUENCER END, BOOOOOOOOOIIII                           --- her tharf


# multithread starts		--- partur af main.
def multithread():
    t1 = threading.Thread(target=tw)                        # her buum vid til alla non main thraedina og
    t2 = threading.Thread(target=pp)
    t3 = threading.Thread(target=st)
    t1.start()
    t2.start()
    t3.start()
# multithread ends    --- breyta i function med if skilyrdum hvort thradur se daudur eda ekki.



# styring fyrir playpause
def pp():
    global pause
    GPIO.wait_for_edge(21, GPIO.FALLING)
    pause = 0
    GPIO.add_event_detect(21, GPIO.FALLING, callback=playpause, bouncetime=200)
def playpause(channel):
    global pause
    if pause == 0:
        pause = 1
    else:
        pause = 0
# lokid


# styring fyrir stop
def st():
    GPIO.add_event_detect(20, GPIO.FALLING, callback=stopper, bouncetime=200)
def stopper(channel):
    global stop, pause, tempo
    if stop == 0:
        stop = 1
        pause = 1
        time.sleep(tempo)
        stop = 0  
# lokid

# tw begins           --- byr til event fyrir trelliswatch.
def tw():
    GPIO.add_event_detect(37, GPIO.FALLING, callback=trellisWatch)
# tw ends.



# trellisWatch begins     --- fylgist med tokkum a trellis. fyrir allt
# nema live mode, eins og er.
def trellisWatch(channel):                              # ignore channel...
    global tGO, status, voice, a, b, tStatus, clA, lGO, mwGO
    time.sleep(0.015)
    # print(GPIO.input(37))                             #sma debug daemi
    if trellis.readSwitches():                          #ef ytt var a takka/uppfaerum database.
        for x in range(0, 64):                          #fyrir alla takka
            if trellis.justPressed(x):                  #var ytt a thennan takka?
                y = tfIn(x)                             #vorpum i status format.
                if tStatus[y % 8][y // 8][voice] == 0:  #ef thad var slokkt a notu
                    tStatus[y % 8][y // 8][voice] = 1   #tha er nuna kveikt a notu
                    trellis.setLED(x)                   #somuleidis med LED.
                    # print(GPIO.input(37),'on')        #debug dot
                else:                                   #ef ekki slokkt a notu
                    tStatus[y % 8][y // 8][voice] = 0   #slokkvum a notu
                    trellis.clrLED(x)                   #led lika
                    # print(GPIO.input(37),'off')
                    trellis.readSwitches()              #tilraun til ad laga response time-id. ma prufa ad fjarlaegja
        trellis.writeDisplay()                          #uppfaerum led
        if tGO == 1:                                    #meigum vid breyta status
            status = tStatus                            #ef ja, vistum tstatus i status.
        time.sleep(0.015)                               #tilraun til ad laga response time-id. ma prufa ad fjarlaegja
        trellis.readSwitches()                          #tilraun til ad laga response time-id. ma prufa ad fjarlaegja
    if mwGO == 1:                                       #ef mwGO=1
        modWatch()                                      #forum i modwatch :)
    if lGO == 1:                                        #ef lGO=1
        livePlay()                                      #forum i liveplay :D
    if clA == 1:                                        #ef clA=1
        clearAll()                                      #skemmum allt :'(
# trellisWatch ends --------------------------------------




# Notkun : fylkid er 8x8, ef taka a status sem er 8x8x16 tharf ad velja eitt voice og gera
# ledshow(status[:,:,voice])svipad fyrir mod fylkid ur modwatch.
# ledshow begins     --- tekur inn fylki af gerdinni 8x8 og flassar fra midju ut en skilur eftir ljos fylkisins.
def ledshow(fylki):
    for x in range(0, 7):
        if x == 1:
            trellis.setLED(15)
            trellis.setLED(35)
            trellis.setLED(48)
            trellis.setLED(28)
            trellis.writeDisplay()
            time.sleep(0.1)
        if x == 2:
            for v in range(0, 2):
                trellis.setLED(v + 24)
                trellis.setLED(v + 52)
                trellis.setLED(v + 38)
                trellis.setLED(v + 10)
            trellis.setLED(29)
            trellis.setLED(49)
            trellis.setLED(34)
            trellis.setLED(14)
            trellis.writeDisplay()
            time.sleep(0.1)
        if x == 3:
            ledhelp(15, fylki)
            ledhelp(35, fylki)
            ledhelp(28, fylki)
            ledhelp(48, fylki)
            for v in range(0, 3):
                trellis.setLED(v + 20)
                trellis.setLED(v + 56)
                trellis.setLED(v + 41)
                trellis.setLED(v + 5)
            for v in range(0, 2):
                y = 4 * v
                trellis.setLED(26 + y)
                trellis.setLED(50 + y)
                trellis.setLED(9 + y)
                trellis.setLED(33 + y)
            trellis.writeDisplay()
            time.sleep(0.1)
        if x == 4:
            for v in range(0, 2):
                y=v*20
                ledhelp(v+24, fylki)
                ledhelp(v+52, fylki)
                ledhelp(v+38, fylki)
                ledhelp(v+10, fylki)
                ledhelp(29+y, fylki)
                ledhelp(14+y, fylki)
            for v in range(0, 4):
                trellis.setLED(v + 16)
                trellis.setLED(v + 60)
                trellis.setLED(v + 44)
                trellis.setLED(v + 0)
            for v in range(0, 3):
                y = 4 * v
                trellis.setLED(23 + y)
                trellis.setLED(51 + y)
                trellis.setLED(4 + y)
                trellis.setLED(32 + y)
            trellis.writeDisplay()
            time.sleep(0.1)
        if x == 5:
            for v in range(0, 3):
                ledhelp(v+20, fylki)
                ledhelp(v+56, fylki)
                ledhelp(v+41, fylki)
                ledhelp(v+5, fylki)
            for v in range(0, 2):
                y = 4 * v
                ledhelp(26+y, fylki)
                ledhelp(50+y, fylki)
                ledhelp(9+y, fylki)
                ledhelp(33+y, fylki)
            trellis.writeDisplay()
            time.sleep(0.1)

        if x == 6:
            for v in range(0, 4):
                ledhelp(v+16, fylki)
                ledhelp(v+60, fylki)
                ledhelp(v+44, fylki)
                ledhelp(v, fylki)
            for v in range(0, 3):
                y = 4 * v
                ledhelp(23+y, fylki)
                ledhelp(51+y, fylki)
                ledhelp(4+y, fylki)
                ledhelp(32+y, fylki)
            trellis.writeDisplay()
            time.sleep(0.1)
#ledshow ends

# ledhelp begins    --- tekur gildi og fylki. ef gildi fylkisins er 0 i x
def ledhelp(x, fylki):      #tha slokkvum vid a thvi. annars ekki
    y=tfIn(x)
    if fylki[y % 8][y // 8] ==0:
        trellis.clrLED(x)
#lehelp ends



#clearleds starts       ---hreinsar ut oll ljos.
def clearleds():
    for x in range(0, 64):
        trellis.clrLED(x)
    trellis.writeDisplay()
#clearleds ends


# ChannelChange starts          --- slekkur a þáverandi led m.v. voice og kveikir a núverandi.
def ChannelChange():
    global tkt, v, voice
    if v != voice:
        clearleds()
        if tkt:
            for x in range(0, 8):                                   # fyrir oll LED i 'dlk'
                trellis.setLED(tfOut(x * 8 + dlk))                  # kveikja a LED!,tfout varpar i trellisformat.
        voice=v
        for x in range (0, 64):
            y = tfIn(x)
            if status[y % 8][y // 8][voice] == 1:
                trellis.setLED(x)
        trellis.writeDisplay()
# ChannelChange ends.



print('starting up')
trellis.readSwitches()
for x in range(0, 64):
    trellis.clrLED(x)
trellis.writeDisplay()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set up for trellis
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set up STOP button
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set up START button

fylki=np.zeros((8, 8))
for x in range(0, 1):
    ledshow(fylki)

for x in range(0, 64):
    trellis.clrLED(x)
trellis.writeDisplay()


t = threading.Thread(target=multithread)
t.start()
print('its running, boooooiiiiii!')

Sequencer()
