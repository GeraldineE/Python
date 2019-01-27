# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self,head):
        
        """
        :type head: ListNode
        :rtype: ListNode
        """
        aux = head
        nuevo = aux

            
        while(aux != None and aux.next != None):
            nuevo = aux.next.val
            aux.next.val = aux.val
            aux.val = nuevo
            aux = aux.next.next
            
        return head
         