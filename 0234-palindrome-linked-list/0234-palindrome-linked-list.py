class Solution(object):
    def isPalindrome(self, head):
      arr = [] 
      temp = head 
      
      while temp:
        arr.append(temp.val) 
        temp = temp.next 

      return arr == arr[::-1] 
        
        