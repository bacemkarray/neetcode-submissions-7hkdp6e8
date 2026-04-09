class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            signature = [0] * 26            
            for char in s:
                signature[ord(char)-ord('a')] += 1
            groups[tuple(signature)].append(s)


        return list(groups.values())