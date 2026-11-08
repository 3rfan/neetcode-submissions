# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        tempHead = head
        tempArr = []
        
        while (tempHead):
            tempArr.append(tempHead)
            tempHead = tempHead.next

        left = 0
        right = len(tempArr) - 1

        while (left < right):
            tempArr[left].next = tempArr[right]
            left += 1

            if left >= right:
                break

            tempArr[right].next = tempArr[left]
            right -= 1
        # prevent cycles, since this node will now be the new tail of the list
        tempArr[left].next = None