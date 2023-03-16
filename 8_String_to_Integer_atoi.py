import math

class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        s = s.lstrip() #remove leading space
        total = 0
        
        modes = ["begin", "sign", "digits", "ignore"]
        m = "begin"
        for n in s:
            #print(n)
            if(m == "begin"):
                #print("begin")
                if(n == "-" ):
                    sign = -1
                    m = "digits"
                    continue
                elif(n == "+"):
                    m = "digits"
                    continue
                else:
                    m = "digits"
            if(m == "digits"):
                if(n.isdigit()):
                    total*=10
                    total+= int(n)
                else:
                    m = "ignore"
            
        total = total * sign
        high = math.pow(2,31) -1
        high = int(high)
        low = math.pow(2,31)*-1
        low = int(low)
        if(total > high):
            total = high
        elif(total < low):
            total = low

        return total 
    
s = ""
#s = "   -42"
#s = "4193 with words"

print(Solution.myAtoi(Solution, s))
