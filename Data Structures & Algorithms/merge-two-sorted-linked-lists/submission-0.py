# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Inputs: list1: Optional[ListNode], list2: Optional[ListNode]
# Goal: to return ONE merged sorted list
#
# Constraints:
# - length of each list is between 0 and 100
# - node values are between -100 and 100
#
# Questions:
# - input lists could they be the same? -> no
# - in case one is empty, what should happen? -> return non empty list
# - does the order of same values matter in output? -> no
# - can the input lists be modified or should they remain as they are? -> can be modified
#
# Scenarios:
# - inp: [1,1,5] [2,5,6]
# - out: [1,1,2,5,5,6]
#
# - inp: [] [2,4,5]
# - out: [2,4,5]
# 
# - inp: [1,1,2,9] [3,4,5,20]
# - out: [1,1,2,3,4,5,9,20]
#
# Initial plan (3 pointers):
# - left, curr, right
# - left for list1, right for list2 and curr for new list
# - compare values of the lists where the pointers point to, in the new list, we should insert the smaller of the 2, at index curr
# - add result list
# (C) Time: O(n)
# (C) Space: O(n + m) (resultList)

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        left = list1
        curr = res
        right = list2
        
        while (left != None and right != None):
            if (left.val < right.val):
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next

        if (left != None):
            curr.next = left
        if (right != None):
            curr.next = right

        return res.next

# if __name__ == "__main__":
#     solver = Solution()

#     assert solver.mergeTwoLists([],[]) == [], "Failed empty lists test"

        