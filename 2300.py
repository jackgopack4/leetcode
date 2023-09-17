import math
class Solution:
    def valid_pos(self, potions: List[int], success: int, spell: int) -> int:
        potion_needed = math.ceil(success/spell)
        l = 0 
        r = len(potions)
        while l < r:
            mid = (l + r) // 2
            if potions[mid] >= potion_needed:
                r = mid
            else:
                l = mid + 1
        return l

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions = sorted(potions)
        res = []
        for spell in spells:
            res.append(len(potions) - self.valid_pos(potions, success, spell))
        return res
