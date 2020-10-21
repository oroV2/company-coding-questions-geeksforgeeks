"""
Given an array Arr of N elements which is first increasing and then may be
decreasing, find the maximum element in the array.
Note: If the array is increasing then just print then last element will be the
maximum value.

Example 1:
Input:
N = 9
Arr[] = {1,15,25,45,42,21,17,12,11}
Output: 45
Explanation: Maximum element is 45.

Example 2:
Input:
N = 5
Arr[] = {1, 45, 47, 50, 5}
Output: 50

Explanation: Maximum element is 50.
Your Task:
You don't need to read input or print anything. Your task is to complete the
function findMaximum() which takes the array arr[], and n as parameters and
returns an integer denoting the answer.

Expected Time Complexity: O(logN)
Expected Auxiliary Space: O(1)

Constraints:
3 ≤ N ≤ 106
1 ≤ Arri ≤ 106
"""

class Solution:
	def findMaximum(self,arr, n):
		ans = 0
		for i in range(0,n):
		    if ans < arr[i]:
		        ans = arr[i]
		return ans

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaximum(arr, n)
        print(ans)
        tc -= 1
