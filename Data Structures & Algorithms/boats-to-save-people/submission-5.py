class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i,j = 0,len(people)-1
        sum = 0
        print(people)
        while i <= j:
            if i == j and people[i] <= limit:
                sum += 1
                break
            if people[i] + people[j] <= limit:
                sum += 1
                i += 1
                j -= 1
            else:
                if people[i] == limit:
                    sum += 1
                    i += 1
                if people[j] <= limit:
                    sum += 1
                j -= 1
        return sum