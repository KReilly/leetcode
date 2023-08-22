class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        ss = s.split(" ")
        sr = ""
        for i in range(k):
            sr += ss[i] + " "
        return sr[0:len(sr)-1]



s = "Hello how are you Contestant"
k = 4
print(Solution.truncateSentence(Solution, s, k))