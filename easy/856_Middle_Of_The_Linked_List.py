# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        counter = 0

        while head:
            head = head.next
            counter += 1

        counter = counter // 2

        for i in range(counter):
            temp = temp.next

        return temp