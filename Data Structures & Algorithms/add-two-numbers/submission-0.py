# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Goal: return the sum of 2 values that are represented as individual numbers in reversed order in a list
#
# Input: l1 and l2 (list heads)
#
# Questions:
# - can the list be empty -> no
# - can the list be null -> no
# - can 0 appear as a value inside the list? -> yes
# - does the output order have to be the same? so the output number reversed? -> yes
# - can list lengths be different? -> yes
# 
# Initial plan:
# - iterate through l1 and l2 with a pointer
# - create an array, with as its values, the powers of 10 (through 10^index of pointer) * list-value at pointer
# - then we loop through the arrays and sum all the values
# - we split the sum into individual values and make the result list
# Time: O(n + m) or more precisely: O(max(n,m))
# Space: O(n + m + max(n, m))
#
# Optimised plan:
# - traverse both lists at the same time using single pointer loop
# - add digits from matching positions along with a carry (either 0 or 1 like in real addition)
# - create and append new list in same iteration
# Time: O(max(n, m))
# Space: O(1)

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # we use a dummy node to handle edge cases like checking if we are adding to an existing chain or wether we are creating a new chain
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        p1 = l1
        p2 = l2
        
        # we keep going as long as we have SOMETHING to process, either items in a list or a carry
        while p1 or p2 or carry:
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0
            
            # we perform basic arithmetic addition with carries
            # since the list is in reverse order, the proper digits will land on the proper positions according to their value
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            # because of the dummy node we can simply do:
            current.next = ListNode(digit)
            current = current.next

            # if there are digits left in the list, advance corresponding pointer
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next

        return dummy_head.next