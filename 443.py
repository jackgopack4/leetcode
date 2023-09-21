class Solution:
    def compress(self, chars: List[str]) -> int:
        last = chars[0]
        count = 1
        lp = 0
        rp = 1
        while rp < len(chars):
            if chars[rp] == last:
                count += 1
            else:
                chars[lp] = last
                if count > 1:
                    for c in str(count):
                        lp += 1
                        chars[lp] = c
                    count = 1
                last = chars[rp]
                lp += 1
            rp += 1
        chars[lp] = last
        if count > 1:
            for c in str(count):
                lp += 1
                chars[lp] = c
        return lp + 1
