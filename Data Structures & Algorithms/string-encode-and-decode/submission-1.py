class Solution:

    def encode(self, strs: List[str]) -> str:
        strs = [str(len(x)) + "#" + x for x in strs]
        strs = "".join(strs)
        return strs

    def decode(self, s: str) -> List[str]:
        substrs = list()

        i = 0
        while(i < len(s)):
            size, n = self._find_num(s[i:])
            size = int(size)
            substrs.append(s[i + n + 1:i + size + n + 1])
            i += size + n + 1

        return substrs

    def _find_num(self, sub_s: str):
        i = 0
        num = list()
        while sub_s[i] != "#":
            num.append(sub_s[i])
            i += 1
        return str("".join(num)), len(num)

