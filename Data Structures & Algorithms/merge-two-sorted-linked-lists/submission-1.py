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
# (C) Time: O(n + m)
# (C) Space: O(1)

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


# Helper to convert [1, 2, 3] -> 1 -> 2 -> 3 -> None
def build_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

# Helper to convert 1 -> 2 -> 3 -> None -> [1, 2, 3]
def to_list(head: Optional[ListNode]) -> List[int]:
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res


# if __name__ == "__main__":
#     solver = Solution()

#     # 1. Edge Case: Both lists empty
#     res = solver.mergeTwoLists(build_list([]), build_list([]))
#     assert to_list(res) == [], "Failed on both empty lists"

#     # 2. Edge Case: One list empty, one populated
#     res = solver.mergeTwoLists(build_list([]), build_list([0]))
#     assert to_list(res) == [0], "Failed on one empty list"

#     # 3. Standard Case: Interleaved values
#     l1 = build_list([1, 2, 4])
#     l2 = build_list([1, 3, 4])
#     res = solver.mergeTwoLists(l1, l2)
#     assert to_list(res) == [1, 1, 2, 3, 4, 4], "Failed on interleaved values"

#     # 4. Asymmetric Lengths (One list much longer than the other)
#     l1 = build_list([1, 5])
#     l2 = build_list([2, 3, 4, 6, 7, 8])
#     res = solver.mergeTwoLists(l1, l2)
#     assert to_list(res) == [1, 2, 3, 4, 5, 6, 7, 8], "Failed on unequal lengths"

#     # 5. Non-overlapping Ranges (All elements in list1 < all elements in list2)
#     l1 = build_list([1, 2, 3])
#     l2 = build_list([10, 20, 30])
#     res = solver.mergeTwoLists(l1, l2)
#     assert to_list(res) == [1, 2, 3, 10, 20, 30], "Failed on non-overlapping ranges"

#     # 6. Negative Numbers and Zeroes
#     l1 = build_list([-10, -5, 0])
#     l2 = build_list([-7, 2, 3])
#     res = solver.mergeTwoLists(l1, l2)
#     assert to_list(res) == [-10, -7, -5, 0, 2, 3], "Failed on negative numbers"

        