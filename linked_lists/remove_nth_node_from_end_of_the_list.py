class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        length_of_list = 0
        curr = head
        head_ref = head
        while curr:
            length_of_list += 1
            curr = curr.next

        if length_of_list == n: return head.next

        count = 0
        while head_ref is not None:
            if count == length_of_list - n - 1:
                head_ref.next = head_ref.next.next
            count += 1
            head_ref = head_ref.next

        return head