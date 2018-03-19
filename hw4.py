"""
Homework 4 - Linked Lists

To understand recursion, you must first understand recursion.
"""

class Node(object):
    """
    Class for linked list node.
    """
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


def list_length(head):
    """
    Given a linked list, returns the length ofthe linked list.
    Suppose the existing linked list looks like this: 3 -> 5 -> 9 -> 6
    Then the length is 4.
    
    Input:
        head - the head Node of a linked list
    
    Returns:
        (int) The length of the linked list
    """
    node = head
    len = 1
    while node.next_node != None:
        len = len + 1
        node.next_node
    return len


def add_head(head, data):
    """
    Prepends a new Node to a linked list. You are given the head
    of the linked list and the data for the new Node.

    Example:
    Suppose the existing linked list looks like this: 3 -> 5 -> 9 -> 6
    In this case, head is a Node with head.data = 3. If the data argument
    is 10, then the resulting linked list should look like this:
    10 -> 3 -> 5 -> 9 -> 6

    Input:
        head - the head Node of a linked list
        data - the data element you'll need to add to the list

    Returns:
        (Node) the head of the new linked list that includes 'data'
    """
    newHead = Node(data)
    newHead.next_node = head
    return newHead


def add_tail(head, data):
    """
    Appends a new Node to a linked list. You are given the head of
    the linked list and the data for the new Node.

    Example:
    Suppose the existing linked list looks like this: 7 -> 8 -> 2
    In this case, head is a Node with head.data = 7. If the data argument
    is 4, then the resulting linked list should look like this:
    7 -> 8 -> 2 -> 4

    Input:
        head - the head Node of a linked list
        data - the data element you'll need to add to the list

    Returns:
        (Node) the head of the new linked list that includes 'data'
    """
    if head == None:
        head = Node(data)
    else:
        current = head
        while (current.next_node != None):
            current = current.next_node
        current.next_node = Node(data)
    return head


def remove_position(head, position):
    """
    Given the head of a linked list, removes the element of the 
    specified position. If the position is greater than the length
    of the linked list, do not remove anything.

    Input:
        head - the head of the linked list.
        position - the position at which to remove an element.
    
    Output:
        the head of the linked list.
    """
    temp = head
    if position == 0:
        return temp.next_node

    while position - 1 > 0:
        head = head.next_node
        position -= 1
    head.next_node = head.next_node.next_node
    return temp


def find_cycle(head):
    """
    Given the head of a linked list, determines whether or not there
    is a cycle in the linked list.
    
    Ex. suppose we have a linked list 3 -> 4 -> 7, and the last node points
    back to the node labeled 4. Then this linked list has a cycle.
    
    Input:
        head - the head of the linked list.
    
    Output:
        (bool) whether or not there is a cycle in the linked list.
    """
    x = []
    while head:
        if head in x:
            return True
        else:
            x.append(head)
        head = head.next_node
    return False
