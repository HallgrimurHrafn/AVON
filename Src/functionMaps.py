import numpy as np

#fScrollMapY er function map fyrir scroll y

#fScrollMapX er function map fyrir scroll x


p="pass"
# 5x8: 8 dalkar, 5 linur.

fClickMap=np.array([[
"""
oldnavx=navx
navx=0
navy=1
Render.Render()""", p,
"""
oldnavx=navx
navx=0
navy=2
Render.Render()""", p,
"""
oldnavx=navx
navx=0
navy=4
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
    navx+=val
    Render.Render()"""
high="""
if val==-1:
    navx+=val
    Render.Render()"""
default="""
navx+=val
Render.Render()"""
fScrollMapX=np.array([
[low, default, default, default, default, default, high, p],
[low, default, high, p, p, p, p, p],
[low, high, p, p, p, p, p, p],
[low, default, default, default, default, default, default, high],
[low, default, high, p, p, p, p, p],

])
