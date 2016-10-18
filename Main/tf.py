#Her verda tvö föll. Varpa úr trellis formati og varpa í trellis format.
#allt prufad i matlab svo thad mun virka.



#tfIn begins 		--- varpar ur trellis i okkar format.
def tfIn (a):
	f=a//16
	d=(a%16)%4
	l=(a%16)//4
	#if f%2==0:
	#	b=16*f+8*l+d
	#else:
	#	#b=16*(f+1)-1-(3-l)*8-3+d
	#	b=16*(f+1)-(3-l)*8+d-4

	b=16*(f+f%2)+8*l+d -28*(f%2)
	return b
#tfIn ends	



#tfOut begins 		--- varpar ur okkar formati i trellis.
def tfOut (a):
	f=a//16
	d=(a%16)%8
	l=(a%16)//8
	#if d<4:
		#if f<2:
		#	b=8*f+4*l+d
		#else:
		#	b=16*f+4*l+d
	#	b=4*l+d+(1+f//2)*8*f
	#else
		#if f%2==1:
		#	b=16*(f+1)+d-4*(3-l)
		#else:
		#	b=16*(f+1)+d-4*(3-l)+8
	#	b=16*(f+1)+d-4*(3-l)+(1-f%2)*8

	b=d+4*l+(d//4)*(16*(f+1)+(1-f%2)*8-12)+(1-d//4)1+f//2)*8*f 		#gaeti verid betra ad nota if heldur en svona stora jofnu.
#tfOut ends