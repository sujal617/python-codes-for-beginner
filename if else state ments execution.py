Age = int(input("enter your age: "))
# conditional operators are
# < , > , <= , >= , == , !=\
print(Age>18)
print(Age<18)
print(Age>=18)
print(Age<=18)
print(Age==18)
print(Age!=18)
if(Age>18):
   print("you can smoke")
elif(Age==19):
    print("you are now adult you can smoke")
    if( 20 <= Age <= 26):
        print("yor are in your prime age")   
else:
    print("you can't smoke") 
 
   