class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0
        cFlag = True
        stext = text.split(" ")

        for w in stext:
            for l in w:
                if(l in brokenLetters):
                    cFlag = False
            if(cFlag):
                count += 1
            cFlag = True
        return count

    

text = "hello world"
brokenLetters = "ad"
text = "leet code"
brokenLetters = "lt"

print(Solution.canBeTypedWords(Solution, text, brokenLetters))