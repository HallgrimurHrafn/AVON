import os
# os.getcwd()
# os.path.exists('/test2')

x=[False,3,2,1]
z=0

f = open(os.path.join('../vision/build', "XYZ.txt"), 'r')
for line in f:
    if z==0:
        if line == "True\n":
            x[z]=True
        else:
            x[z]=True
    else:
        x[z]=int(line)
    z+=1
if x[0]:
    print x, x[1]+x[2]+x[3]
