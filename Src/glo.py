import numpy as np

#fScrollMapY er function map fyrir scroll y

#fScrollMapX er function map fyrir scroll x

navx=0
navy=0
oldnavx=0  # navx fyrir
oldnavx2=0


# mod=np.array(["pass", "notes(Main.x)"])
xmod=np.array(["pass", "notes(Main.x)", "bPitch(Main.x)", "modwheel(Main.x)"])
ymod=np.array(["pass", "notes(Main.y)", "bPitch(Main.y)", "modwheel(Main.y)"])
zmod=np.array(["pass", "notes(Main.z)", "bPitch(Main.z)", "modwheel(Main.z)"])
xcursor=0
ycursor=0
zcursor=0
stat=1

es=0                #edit skali, es=1 fyrir custom skala 1, es=2 fyrir customskala 2....
note=60
currentscale=0      #0= dur, 1=moll, 2=penta, 3,4,5.... =customs 1,2,3....
# ef currentscale >2 ma gera adgerd i custom.
skalar=np.array([
"Main.newskali=np.array([glo.note+12, glo.note+11, glo.note+9, glo.note+7, glo.note+5, glo.note+4, glo.note+2,glo.note])",
"Main.newskali=np.array([glo.note+12, glo.note+10, glo.note+8, glo.note+7, glo.note+5, glo.note+3, glo.note+2,glo.note])",
"Main.newskali=np.array([glo.note+17, glo.note+15, glo.note+12, glo.note+10, glo.note+7, glo.note+5, glo.note+3, glo.note])",
"pass" # custom skali
])
custom=np.array([60, 60, 60, 60, 60, 60, 60, 60])
cs=np.array([])


# 5x8: 8 dalkar, 5 linur. functionmaps og cursormap.
p="pass"

cursor=np.array([
[p, p, p, p, p, p, p, p],
[p, p, p, p, p, p, p, p],
[p, p, p, p, p, p, p, p],
[p, p, p, p, p, p, p, p],
[p, p, p, p, p, p, p, p]
])

fClickMap=np.array([[
"""
glo.oldnavx=glo.navx
glo.navx=0
glo.navy=1""", p,
"""
glo.oldnavx=glo.navx
glo.navx=0
glo.navy=2""", p,
"""
glo.oldnavx=glo.navx
glo.navx=0
glo.navy=4""", p, p, p],
[p, p, p, p, p, p, p, p],
[p, "customsetup()", p, p, p, p, p, p],
[p, p, p, p, p, p, p, p],
[p, p, p, p, p, p, p, p]
])


fScrollMapY=np.array([
#0
["tempchange(val, 1)",
"channelchange(val)",
p, # kannki hvort hann noti global skala eda channel customly her?
"livechange()",
"camerachange()",
"notelengdChange(val)",
"barChange(val)",
p],
#1
["tempchange(val, 100)", "tempchange(val, 10)",
"tempchange(val, 1)", p, p, p, p, p],
#2
["skalarChange(val,1)", "skalarChange(val,0)", p, p, p, p, p, p],
#3
["customskali(val,7)",
"customskali(val,6)",
"customskali(val,5)",
"customskali(val,4)",
"customskali(val,3)",
"customskali(val,2)",
"customskali(val,1)",
"customskali(val,0)"],
#4
["cameraMode(val,0)", "cameraMode(val,1)", "cameraMode(val,2)", p, p, p, p, p]
])

low="""
if val==1:
    glo.navx+=val"""
high="""
if val==-1:
    glo.navx+=val"""
default="""
glo.navx+=val"""

fScrollMapX=np.array([
[low, default, default, default, default, default, high, p],
[low, default, high, p, p, p, p, p],
[low, high, p, p, p, p, p, p],
[low, default, default, default, default, default, default, high],
[low, default, high, p, p, p, p, p]
])


# background color for menu
textbgr = (100,100,100)
