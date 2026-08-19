class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        print(people)
        i,j = 0,len(people)-1
        sum = 0
        while i <= j:
            if i == j and people[i] <= limit:
                sum += 1
                i += 1
                j -= 1
            elif people[i] == limit:
                sum += 1
                i += 1
            elif people[j] == limit:
                sum += 1
                j -= 1
            elif people[i] + people[j] > limit:
                if people[j] <= limit:
                    sum += 1
                j -= 1
            else:
                sum += 1
                i += 1
                j -= 1
            
        return sum