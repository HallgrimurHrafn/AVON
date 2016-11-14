import numpy as np

#fScrollMapY er function map fyrir scroll y

#fScrollMapX er function map fyrir scroll x

navx=0
navy=0
oldnavx=0  # navx fyrir
oldnavx2=0


es=0                #edit skali, es=1 fyrir custom skala 1, es=2 fyrir customskala 2....
note=60
currentscale=0      #0= dur, 1=moll, 2=penta, 3,4,5.... =customs 1,2,3....
# ef currentscale >2 ma gera adgerd i custom.
skalar=np.array([
"Main.skali=np.array([note+12, note+11, note+9, note+7, note+5, note+4, note+2,note])",
"Main.skali=np.array([note+12, note+10, note+8, note+7, note+5, note+3, note+2,note])",
"Main.skali=np.array([note+17, note+15, note+12, note+10, note+7, note+5, note+3, note])",
"pass" # custom skali
])
custom=np.array([60, 60, 60, 60, 60, 60, 60, 60])
cs=np.array([])


p="pass"
# 5x8: 8 dalkar, 5 linur.

fClickMap=np.array([[
"""
functionMaps.oldnavx=functionMaps.navx
functionMaps.navx=0
functionMaps.navy=1
Render.Render()""", p,
"""
functionMaps.oldnavx=functionMaps.navx
functionMaps.navx=0
functionMaps.navy=2
Render.Render()""", p,
"""
functionMaps.oldnavx=functionMaps.navx
functionMaps.navx=0
functionMaps.navy=4
Render.Render()""", p, p, p],
[p, p, p, p, p, p, p, p],
[p, "customsetup()", p, p, p, p, p, p],
[p, p, p, p, p, p, p, p],
[p, p, p, p, p, p, p, p]
])


fScrollMapY=np.array([
#0
["tempchange(val, 1)",
"channelchange(val)",
p,
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
    functionMaps.navx+=val
    Render.Render()"""
high="""
if val==-1:
    functionMaps.navx+=val
    Render.Render()"""
default="""
functionMaps.navx+=val
Render.Render()"""
fScrollMapX=np.array([
[low, default, default, default, default, default, high, p],
[low, default, high, p, p, p, p, p],
[low, high, p, p, p, p, p, p],
[low, default, default, default, default, default, default, high],
[low, default, high, p, p, p, p, p],

])
