def average(*numbers):
    #print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i 
    #print("average is:",sum / len(numbers))
    return  sum / len(numbers)
c = average(5,6,7,8,9)
print(c) 

def name(**name):
    #print(type((name))
    print("hello" ,name["fname"], name["mname"], name["lname"])

name(fname="sujal", mname="sandeep", lname = "khopade")    

