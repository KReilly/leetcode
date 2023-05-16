class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        l = word.lower()
        u = word.upper()
        c = ""
        for i in range(len(word)):
            if(i == 0):
                c+=word[i].upper()
            else:
                c+=word[i].lower()
        return (word == l or word == u or word == c)



word = "FlaG"
word = "Flag"

#word = "USA"

print(Solution.detectCapitalUse(Solution, word))