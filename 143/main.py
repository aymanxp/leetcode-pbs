

class ListNode:
    def __init__(self, val : int=0, next: ListNode | None =None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        # Cut the array in two halfs and get l1 and l2 using fast and slow pointers approach 
        slow = head
        fast = head.next

        while fast and fast.next : 
            slow = slow.next 
            fast = fast.next.next 

        # Reverse the second half 
        second = slow.next 
        prev = slow.next = None 
        while second: 
            temp = second.next
            second.next = prev 
            prev = second 
            second = temp 


        # Merge both halfs 
        first = head 
        second = prev 
        while second :
            temp1 = first.next
            temp2 = second.next
            first.next = second 
            second.next = temp1
            first = temp1 
            second = temp2
        
    




