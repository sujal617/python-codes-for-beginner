import time 
t = (time.strftime("%H:%M:%S"))
h = int(time.strftime("%H"))
h = (int(input("enter the time:")))
print (h)

if(h > 0 and h < 12 ):
    print("good morning")
elif(h >= 12 and h < 18 ):
    print("good afternoon")
if(h >= 18 and h < 20  ):
    print("good evening")    
else:
    print("good night") 
