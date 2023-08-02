class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime+delayedTime)%24

arrivalTime = 10
delayedTime = 15
print(Solution.findDelayedArrivalTime(Solution, arrivalTime, delayedTime))
