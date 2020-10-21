"""
Given an array arr[] of size N, the task is to add the minimum number(should be
greater than 0) to the array so that the sum of the array becomes even

Example 1:
Input: N = 8
arr[] = {1, 2, 3, 4, 5, 6, 7, 8}
Output:  2
Explanation:  Sum of array is 36, so
we add minimum number 2 to make the
sum even.

Example 2:
Input: N = 9
arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9}
Output:  1

Your Task:
This is a function problem. You don't need to take any input, as it is already
accomplished by the driver code. You just need to complete the function minNum()
that takes array A and integer N as parameters and returns the minimum number
required to the array so that the sum becomes even.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ N ≤ 106
"""
class Solution:
     def minNum(self, arr, n):
        sum = 0
        a = 0
        for i in range(0,n):
            if arr[i] % 2 == 1:
                a += 1
        if a % 2 == 0:
            return 2
        elif a % 2 == 1:
            return 1

if __name__ == '__main__':
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        a=list(map(int,input().split()))
        ob = Solution()
        ans=ob.minNum(a,n)
        print(ans)
