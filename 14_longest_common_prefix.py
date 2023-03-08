def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    lcp=""
    for i in range(0,len(strs[0])):
        lcp += strs[0][i]
        for w in range(1, len(strs)):
            if(len(strs[w]) <= i):
                lcp = lcp[:-1]
                return lcp
            if(strs[w][i] != strs[0][i]):
                lcp = lcp[:-1]
                return lcp
            #if(w == len(strs)-1):
            #    lcp += strs[0][i]
            
    return lcp

strs = ["flower","flow","flight"]
answer = longestCommonPrefix(strs)
print(answer)