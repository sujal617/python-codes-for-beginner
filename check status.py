def checkstatus(a,b ,flag):
    if flag == False:
        if((a>0)or (b>0)):
            return True
        else:
            if((a<0)or(b<0)):
                return True
            else:
                return False
            
checkstatus(1 , -1, False)           