"""Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Note:

The number of nodes in the given list will be between 1 and 100."""




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
    
        """Function to find happy number
        Param:
        head : singly linked list 
        Return :
        return type will be singly linked list
        """
        
        # Here we are using 2 pointer method
        # In each loop step the ptr2 will inremented twice which eventual end ptr1 as middle or 2nd middle
        ptr1=ptr2=head
        
        #Explanation
        #Traverse linked list using two pointers. Move one pointer by one and other pointer by two. 
        #When the fast pointer reaches end slow pointer will reach middle of the linked list.
        
        while ptr2!=None and ptr2.next!=None:
            # lopping till whole singly list
            
            ptr1=ptr1.next
            ptr2=ptr2.next.next
            
        return ptr1
        
        