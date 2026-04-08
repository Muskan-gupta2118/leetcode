# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def deleteDuplicates(head):
    current = head

    # Traverse the list
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next  # remove duplicate
        else:
            current = current.next  # move forward

    return head


# Helper function to print linked list
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# Creating example linked list: 1 -> 1 -> 2 -> 3 -> 3
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)

print("Original List:")
printList(head)

# Remove duplicates
head = deleteDuplicates(head)

print("After Removing Duplicates:")
printList(head)