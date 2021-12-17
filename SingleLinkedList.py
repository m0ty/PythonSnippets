# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def buildSingleLinkedList(array):
    if len(array) == 0:
        return
    head = ListNode(array[0])
    if len(array) == 1:
        return head
    
    prevNode = head
    
    for i in range(1, len(array)):
        currNode = ListNode(array[i])
        prevNode.next = currNode
        prevNode = currNode
                                    
    return head
    
def singleLinkedToPythonList(singleLinkedList):
    out_list = []
    currentLink = singleLinkedList

    while currentLink:
        out_list.append(currentLink.val)
        currentLink = currentLink.next
    
    return out_list
