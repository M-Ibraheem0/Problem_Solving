class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = [0] * (limit + 1)
        for p in people:
            count[p] += 1
        idx,i = 0,1
        while idx < len(people):
            while count[i] == 0:
                i += 1
            people[idx] = i
            count[i] -= 1
            idx += 1

        i,j,boats = 0,len(people) - 1,0
        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
            boats += 1
        return boats