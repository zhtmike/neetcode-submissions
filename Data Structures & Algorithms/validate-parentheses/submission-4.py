class Solution:
    def isValid(self, s: str) -> bool:
        inserts = ['(', '{', '[']
        inserts = dict(zip(inserts, range(len(inserts))))

        pops = [')', '}', ']']
        pops = dict(zip(pops, range(len(pops))))

        stack = list()
        for x in s:
            if x in inserts:
                stack.append(x)
            elif x in pops:
                if len(stack) > 0 and pops[x] == inserts[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
