> [Problem on leetCode](https://leetcode.com/problems/climbing-stairs/)
# Problem
## Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:
```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```
Example 2:
```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```
 

Constraints:

    1 <= n <= 45

# Notes
![image](https://user-images.githubusercontent.com/55706427/152100892-0e6c7e1e-ee5c-4ff6-9a34-0a546f252ab6.png)
- solution 1
  - Noticed that the number of twos and ones were increasing and decreasing respectively
  - did permutations
  - implemented it
- solution 2
  - The results are in fibonacci series 
