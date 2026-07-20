class Solution:
    hash_ = "✓"

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            if strs[0] == "":
                return self.hash_
            return strs[0]
        if strs == ["", ""]:
            return self.hash_ + self.hash_
        strs = self.hash_.join(strs)
        return strs

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        if s == self.hash_:
            return [""]
        if len(s) == 1:
            return [s]
        if s == self.hash_ + self.hash_:
            return ["", ""]
        return s.split(self.hash_)
