class Solution:

    def partitionString(self, s: str) -> int:
        count = 1
        hashmap = set()
        for el in s:
            if el in hashmap:
                count += 1
                hashmap = {el}
            else:
                hashmap.add(el)
        return count
