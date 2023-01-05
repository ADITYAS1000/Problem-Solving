class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict = {}
        for each in s:
            if each not in my_dict:
                my_dict[each] = 1
            else:
                my_dict[each] += 1
                
        for each in t:
            if each in my_dict:
                my_dict[each] -= 1
                if my_dict[each] == 0:
                    del my_dict[each]
            else:
                return False
        if(len(my_dict.keys()) == 0):
            return True            
        else:
            return False