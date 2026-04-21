class Solution(object):
    def lengthOfLongestSubstring(self, s): 
     unique_characters = set()   
     left = 0  
     max_length = 0
     for i in range(len(s)):   
        while s[i] in unique_characters: 
            unique_characters.remove(s[left])   
            left += 1      
        unique_characters.add(s[i]) 
        length = i -left + 1  
        max_length = max(max_length,length)  

     return max_length  
