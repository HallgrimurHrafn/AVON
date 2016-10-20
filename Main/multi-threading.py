import threading
import time
#multithread starts		--- partur af main.
def multithread ():
	t1=threading.Thread(target=trellisWatch)
	#t2=threading.Thread(target=myndavel)
	#t3=threading.Thread(target=menuWatch)
	print('test1')
	t1.start()
	#t2.start()
	#t3.start()
	print('test2')
	t1.join()
	#t2.join()
	#t3.join()
	multithread()
#multithread ends    --- breyta i function med if skilyrdum hvort thradur se daudur eda ekki.

def trellisWatch ():
	print('aftur')
	time.sleep(2)

t=threading.Thread(target=multithread)
t.start()
print('still running buddy')