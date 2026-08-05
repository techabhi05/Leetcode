class Solution:
    def removeDuplicates(self, s , k):
        pocket = []
        answer = ""

        for ch in s:
            if len(pocket) == 0 or pocket[-1][0] != ch:
                pocket.append([ch,1])
            else:
                if pocket[-1][1] == k-1:
                    pocket.pop()
                else:
                    pocket[-1][1] += 1


        for num in pocket:
            for i in range(num[1]):
                answer += num[0]

        return answer

                    
