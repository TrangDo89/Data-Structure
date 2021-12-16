#Group 31: Trang Do - U26667617, Arianna Loucks - U69700489
"""
File: a5.py
Assignment 5

Define a length function.
Define a printStructure function.
Define an insert function.
Test the above functions and the Node class.
"""

from node import Node


def length(head):
    """Returns the number of items in the linked structure
    referred to by head."""
    probe = head
    count = 0

    # ADD CODE HERE: Count the number of nodes in the structure
    while probe is not None:
        count += 1
        probe = probe.next
    return count


def insert(newItem, head):
    """Inserts newItem at the correct position (ascending order) in
    the linked structure referred to by head.
    Returns a reference to the new structure."""

# create the new node object
    node = Node(newItem)
    if head == None:
        head = node
        return head

# if the head is not empty
    else:
        # if the head value less than the new node value
        if head.data.upper() < node.data.upper():
            current_node = head
            while current_node.next is not None and current_node.next.data.upper() < node.data.upper():
                nextNode = current_node.next
                current_node = nextNode
            node.next = current_node.next
            current_node.next = node
            return head
        # if the head value more than the new node value
        else:
            node.next = head
            head = node
            return head


def printStructure(head):
    """Prints the items in the structure referred to by head."""
    # ADD CODE HERE
    cur_node = head
    while cur_node is not None:
        print(cur_node.data, end=' ')
        cur_node = cur_node.next


def main():
    """Gets words from the user and inserts in the
    structure referred to by head."""

    head = None
    while True:
        userInput = input('Please enter a word (or just hit enter to end): ')
        if userInput == '':
            break
        head = insert(userInput, head)

    print('The structure contains', length(head), 'items:')
    printStructure(head)


if __name__ == "__main__": main()
