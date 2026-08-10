class Solution:
    def isValid(self, s: str) -> bool:
        inserts = ['(', '{', '[']
        pops = [')', '}', ']']
        
        pops_mapping = dict(zip(pops, inserts))

        stack = list()
        for x in s:
            if x in inserts:
                stack.append(x)
            elif x in pops:
                if len(stack) > 0 and pops_mapping[x] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
