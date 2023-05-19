class Solution:
    def defangIPaddr(self, address: str) -> str:
        defang = ""
        sp = address.split(".")
        defang = sp[0] + "[.]" + sp[1] + "[.]" + sp[2] + "[.]" + sp[3] + "[.]"
        return defang

address = "255.100.50.0"
print(Solution.defangIPaddr(Solution, address))