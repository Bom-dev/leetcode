class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        final = []
        for i in range(len(heights)):
            max_num = max(heights)
            n = heights.index(max_num)
            final.append(names[n])
            heights.pop(n)
            names.pop(n)
        return final
