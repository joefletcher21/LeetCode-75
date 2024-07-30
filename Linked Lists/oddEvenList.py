# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if(head == None or head.next == None):
            return head
        even = ListNode(0)
        odd = ListNode(0)
        odd_ptr = odd
        even_ptr = even
        count = 1

        while(head != None):
            if(count%2 != 0):
                odd_ptr.next = head
                odd_ptr = odd_ptr.next
            else:
                even_ptr.next = head
                even_ptr = even_ptr.next
            head = head.next
            count+=1
        even_ptr.next = None
        odd_ptr.next = even.next

        return odd.next

        return odd
