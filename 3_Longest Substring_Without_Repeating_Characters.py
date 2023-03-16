class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        output = 0
        for r in range(len(s)):
            if s[r] not in seen:
                output = max(output,r-l+1)
            else:
                if seen[s[r]] < l:
                    output = max(output,r-l+1)
                else:
                    l = seen[s[r]] + 1
            seen[s[r]] = r
        return output
        
        # maxSubstring = 0
        # if(len(s) < 2):
        #      return len(s)
        # for i in range(0, len(s)-1):
        #     valid = True
        #     for j in range(i, len(s)):
        #         if(valid):
        #             a = s[i:j]
        #             last = a[-1]
        #             a2 = a[:-1]
        #             print(a, a2, last)




        # return maxSubstring
        # maxSubstring = 0
        # if(len(s) < 2):
        #     return len(s)
        # if(len(s) == 2):
        #     if(s[0] == s[1]):
        #         return 1
        #     else:
        #         return 2
        
        # for i in range(0, len(s)-1):
        #     found = False
        #     for j in range (i, len(s)):
        #         if(found != True):
        #             a = s[i:j]
        #             last = a[-1]
        #             a = a[:-1]
        #             print(a, last)

        #             for n in a:
        #                 if(n == last):
        #              #       print(a, n, last)
        #                     found = True
                    
        #             if( found == False):
        #                 flength = (len(a))+1
        #                 if(maxSubstring < flength):
        #                     #print(a)
        #                     maxSubstring = flength


                   


                # a = s[i:j]
                # #print(a, maxSubstring)
                # if (a.find(s[j]) != 1):
                #     break
                # else:
                #     if(j-i+1 > maxSubstring):
                #         maxSubstring = j-i+1
                #         print(a)


        
        return maxSubstring
    
#s = "bbbbb"
#s = "pwwkew"
s = "abcabcbb"
#s= "aab"
#s= "aa"
#x`s = " "
#s = ""
print(Solution.lengthOfLongestSubstring(Solution, s))
