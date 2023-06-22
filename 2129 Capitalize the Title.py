class Solution:
    def capitalizeTitle(self, title: str) -> str:
        cap = ""
        title = title.lower()
        words = title.split(" ")
        for w in words:
            if(len(w) > 2):
                cap += " " + w[0].upper() + w[1:]
            else:
                cap += " "
                cap += w
        
        if(len(cap)>1):
            return cap[1:]
        return cap





title = "First leTTeR of EACH Word"
print(Solution.capitalizeTitle(Solution, title))