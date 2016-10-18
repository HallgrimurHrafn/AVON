
#multithread starts		--- partur af main.
def multithread ():
	t1=thread(target=trellisWatch)
	t2=thread(target=myndavel)
	t3=thread(target=menuWatch)
	t1.start()
	t2.start()
	t3.start()
#multithread ends    --- breyta i function með if skilyrðum hvort þráður sé dauður eða ekki.
