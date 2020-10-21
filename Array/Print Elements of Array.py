"""
Given an array Arr of size N, print all its elements.

Example 1:
Input:
N = 5
Arr[] = {1, 2, 3, 4, 5}
Output: 1 2 3 4 5

Example 2:
Input:
N = 4
Arr[] = {2, 3, 5, 5}
Output: 2 3 5 5
Your Task:
Complete the function printArray() which takes an array arr, single integer n,
as input parameters and prints the value of the array space separated.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= N <= 105
1 <= Arr[i] <= 105
"""

class Solution:
	def printArray(self,arr, n):
	    for i in range(0,n):
	       print(arr[i],end = " ")

if __name__ == "__main__":
    tc=int(input())
    while tc > 0:
        n=int(input().strip())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ob.printArray(arr, n)
        print()
        tc=tc-1
