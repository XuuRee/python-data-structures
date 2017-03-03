#!/usr/bin/python3

# IB002 Extra homework 1.
#
# Linked list:
#        ___   ___   ___   ___   ___
#       /   \ /   \ /   \ /   \ /   \
#     a <-- b <-- c <-- d <-- e <-- f
#
# Strange list:
#       _________   _________
#      /         \ /         \
#     a <-- b <-- c <-- d <-- e <-- f
#            \_________/ \_________/
#

class Node:
    def __init__(self):
        self.value = None
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None


class StrangeList:
    def __init__(self):
        self.first = None
        self.last = None


def list_to_strange_list(linkedList):
    node = linkedList.first
    
    while((node != None) and (node.next != None)):
        nextnode = node.next
        node.next = nextnode.next
        node = nextnode
    
    return linkedList
 

def check_strange_list(strangeList):
    firstNode = strangeList.first
    lastNode = strangeList.last

    if(firstNode.prev != None):
        return False

    if(lastNode.next != None):
        return False

    if(lastNode.prev != None):
        if(lastNode.prev.next != None):
            return False

    return True

