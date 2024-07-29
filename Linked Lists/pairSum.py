# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        maxSum = 0
        middlePtr = head
        fast = head
        node = None

        while(fast != None and fast.next != None):
            middlePtr = middlePtr.next
            fast = fast.next.next
        prev = node
        while(middlePtr != None):
            temp = middlePtr.next
            middlePtr.next = prev
            prev = middlePtr
            middlePtr = temp
        while(prev != None):
            currSum = head.val + prev.val
            maxSum = max(maxSum,currSum)
            head = head.next
            prev = prev.next
        return maxSum

