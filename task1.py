class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return ' -> '.join(map(str, values))


def reverse_linked_list(linked_list):
    prev = None
    current = linked_list.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    linked_list.head = prev


def merge_sort(linked_list):
    if not linked_list.head or not linked_list.head.next:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(linked_list):
    if not linked_list.head or not linked_list.head.next:
        left_half = linked_list
        right_half = LinkedList()
        return left_half, right_half

    slow = linked_list.head
    fast = linked_list.head
    prev = linked_list.head

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    left_half = LinkedList()
    right_half = LinkedList()

    left_half.head = linked_list.head
    right_half.head = slow
    prev.next = None

    return left_half, right_half


def merge(left, right):
    merged = LinkedList()
    merged.head = Node()

    current = merged.head
    left_head = left.head
    right_head = right.head

    while left_head and right_head:
        if left_head.value < right_head.value:
            current.next = left_head
            left_head = left_head.next
        else:
            current.next = right_head
            right_head = right_head.next
        current = current.next

    current.next = left_head if left_head else right_head
    merged.head = merged.head.next

    return merged


