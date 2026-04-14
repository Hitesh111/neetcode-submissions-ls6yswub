class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = sorted(set(nums))
        result = []
        if len(num) == 0:
            return 0
        if len(num) == 1:
            return 1
        max_len = 1
        for i in range(len(num)):
            # Optimization: only start sequence if previous number isn't consecutive
            if i > 0 and num[i] == num[i-1] + 1:
                continue
            temp = [num[i]]
            prev = num[i]
            for j in range(i+1, len(num)):
                print(num[i],"-------",num[j] , "--", prev)
                if num[j]== prev+1:
                    temp.append(num[j])
                    prev = num[j]
                else:
                    break
            max_len = max(max_len, len(temp))
        return max_len