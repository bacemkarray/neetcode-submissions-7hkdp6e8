class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}

        for s in strs:
            signature = [0] * 26

            for char in s:
                signature[ord(char)-ord('a')] += 1
            
            if tuple(signature) not in results:
                results[tuple(signature)] = []
            results[tuple(signature)].append(s)
        
        return list(results.values())
