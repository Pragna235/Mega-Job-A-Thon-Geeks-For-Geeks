"""Geek love strings having atmost one character whose frequency is odd and rest all (if exists) characters have even frequencies,
he calls such strings as beautiful strings. Geek has a box containing n strings. You have to help him in counting number of pairs (i,j) 
(0<i<j<n-1) such that a string formed by concatenating string at index i with string at index j is a beautiful string. 

Note: Strings consist of only lowercase English letters.
Example 1 :
Input:
n = 3
box = {bbcb, abccc, abc}
Output:
3
Explanation:
Pairs which form beautiful string are (1,2), (1,3) and (2,3).
"""


from typing import List

class Solution:
    
    def noOfPairs(self, box: List[str]) -> int:
        # Write your code here
        
        def isBeautifulString(string):
            freq=[0]*26
            odd_count=0
            
            for char in string:
                freq[ord(char)-ord('a')]+=1
            
            for count in freq:
                if count%2!=0:
                    odd_count+=1
            return odd_count<=1
            
        count=0
        n=len(box)
        
        for i in range(n):
            for j in range(i+1,n):
                if isBeautifulString(box[i]+box[j]):
                    count+=1
        return count
                
        


#{ 
 # Driver Code Starts

for _ in range(int(input())):
    
    n = int(input())
    box = [input() for _ in range(n)]
    ob = Solution()
    res = ob.noOfPairs(box)
    print(res)
    
# } Driver Code Ends

