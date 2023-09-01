class Solution:
    def interpret(self, command: str) -> str:
        return  command.replace('()','o').replace('(al)','al')


command = "G()()()()(al)"
print(Solution.interpret(Solution, command))