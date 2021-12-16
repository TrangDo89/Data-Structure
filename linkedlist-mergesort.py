from node import Node

def read():
    file = open("hw5-2.txt", "r")
    line = file.readline()
    values = []
    for value in line.split(' '):
        values.append(int(value))
    return values

def insert(newItem, head):
    newNode = Node(newItem)
    if head == None:
        head = newNode
        return head
    else:
            cur_node = head
            while cur_node.next is not None:
                cur_node = cur_node.next
            cur_node.next = newNode
            return head

def printStructure(head):
    """Prints the items in the structure referred to by head."""
    # ADD CODE HERE
    cur_node = head
    while cur_node is not None:
        print(cur_node.data, end=" ")
        cur_node = cur_node.next

def mergesort(head, size):
    if head is None or head.next is None:
        return head
    # print(head.data, end =" ") #debug
    goal = size//2
    # print("goal: ", goal) #debug
    count = 1   #count can't be 0, bc there is always at least one element left in a list
    cur_node = head     #keep head pointed to first node
    while count < goal:
        cur_node = cur_node.next    #iterate with current
        count += 1
    middle = cur_node
    head_right_half = middle.next
    middle.next = None

    if size % 2 == 0: #if even
        left = mergesort(head, goal)
        right = mergesort(head_right_half, goal)
    else:
        #if list is odd, the right will be one greater than left (5 = 2 + 3)
        left = mergesort(head, goal)
        right = mergesort(head_right_half, goal + 1)
    result = merge(left,right)
    return result

def merge(left, right):
    # create the temporary linked list
    new_item = Node(None)
    new_head = new_item

    # when left and right is not null compare data
    while left is not None and right is not None:
        if left.data >= right.data:
            new_head.next = right
            right = right.next

        else:
            new_head.next = left
            left = left.next
        new_head = new_head.next

    if left is not None:
        new_head.next = left
        left = left.next

    else:
        new_head.next = right
        right = right.next

    return new_item.next


def main():
    list = read()
    print("before sort:\n", list)

    head = None

    for i in range(len(list)):
        head = insert(list[i],head)

    # print("\n\ncount: ", len(list))
    # printStructure(head)
    newList = mergesort(head, len(list))
    print("\nafter sort:")
    printStructure(newList)



if __name__ == "__main__": main()
