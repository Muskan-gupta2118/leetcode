#You are given the heads of two sorted linked lists list1 and list2.

#Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.  write a program in pyhton

# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    # Create a dummy node to simplify logic
    dummy = ListNode()
    current = dummy

    # Traverse both lists
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        
        current = current.next

    # Attach remaining elements
    if list1:
        current.next = list1
    else:
        current.next = list2

    return dummy.next


# Helper function to print linked list
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# Example usage
# list1: 1 -> 2 -> 4
list1 = ListNode(1, ListNode(2, ListNode(4)))

# list2: 1 -> 3 -> 4
list2 = ListNode(1, ListNode(3, ListNode(4)))

result = mergeTwoLists(list1, list2)
printList(result)