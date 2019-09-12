import time
import random 

l=['a','s','d','f','j','k','l',';']

i=1
while i<=10:
	print(random.sample(l,1)[0])
	time.sleep(2)
	i+=1

