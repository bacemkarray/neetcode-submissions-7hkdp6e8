class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            length = len(s)
            res += str(length) + "*" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        while i < len(s):
            length = ""
            while (s[i] != "*"):
                length += s[i]
                i+=1
            res.append(s[i+1:i+1+int(length)])
            i += 1+int(length)
        return res
