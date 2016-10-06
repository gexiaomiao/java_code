class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map_s, map_t ={}, {}
        for i in s:
            map_s[i] = map_s.get(i,0)+1  # here 0 means the default value, if there is no such pair
        
        for i in t:
            map_t[i] = map_t.get(i,0)+1
        
        return map_s==map_t