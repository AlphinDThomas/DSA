class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        players.sort()
        trainers.sort()

        i = 0
        j = 0
        count = 0
        while i<len(players) and j<len(trainers):
            if players[i]<=trainers[j]:
                i+=1
                j+=1
                count+=1
            elif players[i]>trainers[j] and j<len(trainers):
                j+=1
        return count