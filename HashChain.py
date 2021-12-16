import hashlib

# this code is reference on zybook and last assignment
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head == None:
            self.head = new_node

class Node():

    def __init__(self, data, next = None):
        """Instantiates a Node with default next of None"""
        self.data = data
        self.next = next

def H(k):
    kb = str.encode(k)
    return hashlib.sha256(kb).hexdigest()

def hashchain(seed_value, hash_length):
    #create a list
    num_list = LinkedList()
    hash_seed = H(seed_value)
    num_list.head = Node(hash_seed)

    cur_node = num_list.head

    #keep hashing the data in linked list base on seed value
    for i in range(hash_length-1):
       hash_value = H(cur_node.data)
       cur_node.next = Node(hash_value)
       cur_node = cur_node.next

    # print the linked list
    cur_node = num_list.head
    while cur_node is not None:
        print(cur_node.data)
        cur_node = cur_node.next

def main():

    #get the seed value and hash chain input
    seed= input("Please enter the seed value: ")
    length = int(input("Please enter the length of the hashchain: "))
    hashchain(seed, length)


if __name__ == "__main__": main()

