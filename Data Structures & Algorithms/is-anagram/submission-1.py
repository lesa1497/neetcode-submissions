class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        count1 = {}

        for x in s :
            count[x] = count.get(x, 0) + 1

        for y in t : 
            count1[y] = count1.get(y, 0) + 1

        return count == count1

      
        



     
            
             