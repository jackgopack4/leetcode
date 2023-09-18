class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = 201
        for s in strs:
            if len(s) < min_length:
                min_length = len(s)
        test_prefix = strs[0][0:min_length]
        for s in strs:
            if s[0:min_length] == test_prefix:
                continue
            else:
                while min_length > 0 and s[0:min_length] != test_prefix[0:min_length]:
                    min_length -= 1
                if min_length == 0:
                    return ""
                else:
                    test_prefix = test_prefix[0:min_length]
        return test_prefix
