class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = set()
        
        j = 0
        lengths = []

        for i in range(len(s)):
            char = s[i]
            if char not in cnt:
                cnt.add(char)
            else:
                lengths.append(i - j)
                while char in cnt:
                    cnt.remove(s[j])
                    j += 1
                cnt.add(char)

            if i == len(s) - 1:
                lengths.append(i - j + 1)

        if not lengths:
            return len(s)
        
        return max(lengths)


            


            