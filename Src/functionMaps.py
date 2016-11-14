

fClickMap=np.chararray((5,8), itemsize=68)         # max 25 stafir.. haegt ad auka.
fClickMap[:][:]="pass"


#fScrollMapY er function map fyrir scroll y
fScrollMapY=np.chararray((5,8), itemsize=25)
fScrollMapY[:][:]="pass"
#fScrollMapX er function map fyrir scroll x
fScrollMapX=np.chararray((5,8), itemsize=70)
fScrollMapX[:][:]="pass"

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
])
