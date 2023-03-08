def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        if(s.find("IV")!=-1):
            total+=4
            s=s.replace("IV", "")
            print(s)
        if(s.find("IX")!=-1):
            total+=9
            s.replace("IX", "")
        if(s.find("XL")!=-1):
            total+=40
            s.replace("XL", "")
        if(s.find("XC")!=-1):
            total+=90
            s.replace("XC", "")
        if(s.find("CD")!=-1):
            total+=400
            s.replace("CD", "")
        if(s.find("CM")!=-1):
            total+=900
            s.replace("CM", "")
        
        c = s.count('I')
        if(c!=-1):
            total+=c
            
        c = s.count('V')
        if(c!=-1):
            total+=c*5

        c = s.count('X')
        if(c!=-1):
            total+=c*10

        c = s.count('L')
        if(c!=-1):
            total+=c*50

        c = s.count('C')
        if(c!=-1):
            total+=c*100

        c = s.count('D')
        if(c!=-1):
            total+=c*500
        c = s.count('M')
        if(c!=-1):
            total+=c*1000
            
        return total

s = "III"
print("Input = " + s)
print("Output = " + str(romanToInt(s)))
s = "IV"

print("Input = " + s)
print("Output = " + str(romanToInt(s)))
s= "MCMXCIV"

print("Input = " + s)
print("Output = " + str(romanToInt(s)))
