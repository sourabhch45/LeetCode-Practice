>[Problem on leetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)
# Problem
## Remove Duplicates from Sorted List
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:
```
Input: head = [1,1,2]
Output: [1,2]
```
![image](https://user-images.githubusercontent.com/55706427/152152916-36ebd523-b84f-4a5e-b774-12596472d17a.png)

Example 2:
```
Input: head = [1,1,2,3,3]
Output: [1,2,3]
```
 ![image](https://user-images.githubusercontent.com/55706427/152152870-472ca08f-46c3-4927-b383-1e30a0e483ae.png)


Constraints:

    The number of nodes in the list is in the range [0, 300].
    -100 <= Node.val <= 100
    The list is guaranteed to be sorted in ascending order.
# Notes
- Learnt LinkedListImplementation 
- can  access the 2nd next element by node.next.next
- can traverse 1 (more than 1?) node backwards by using prev [like in this example](https://www.geeksforgeeks.org/linked-list-set-3-deleting-node/)  
