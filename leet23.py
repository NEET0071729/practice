'''
23. Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list: 1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
 
Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        ans = ListNode()
        dummy = ans
        current = {}
        for k in range(len(lists)):
            while lists[k]:
                if lists[k].val in current:
                    current[lists[k].val] += 1
                else:
                    current[lists[k].val] = 1
                lists[k] = lists[k].next
        
        for keese in sorted(current.keys()):
            while current[keese]:
                dummy.next = ListNode(keese)
                dummy = dummy.next
                current[keese] -= 1
        return ans.next