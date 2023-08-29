class Solution:
    def minTimeToType(self, word: str) -> int:
        time = 0
        prev = 'a'
        for w in word:
            if(w == prev):
                time+=1
            else:
                time+=min(abs(ord(w)-ord(prev)), abs(ord(prev)-ord(w)))
            prev = w
        return time
    
word = "abc"
word = "bza"
print(Solution.minTimeToType(Solution, word))