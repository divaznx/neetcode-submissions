class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqs = []
        res = []

        for word in strs:
            freq = {}

            for char in word:
                if char in freq:
                    freq[char] += 1
                else:
                    freq[char] = 1

            freqs.append(freq)

        used = []

        for i in range(len(strs)):
            if i in used:
                continue

            group = [strs[i]]
            used.append(i)

            for j in range(i + 1, len(strs)):
                if freqs[i] == freqs[j]:
                    group.append(strs[j])
                    used.append(j)

            res.append(group)

        return res