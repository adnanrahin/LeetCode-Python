class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        result = ListNode(0)
        head = result
        sum = 0
        while l1 is not None and l2 is not None:
            sum += l1.val + l2.val
            mod = sum % 10
            sum //= 10
            head.next = ListNode(mod, head.next)
            head = head.next
            l1 = l1.next
            l2 = l2.next

        remain = l2 if (l2 is not None) else l1

        while remain is not None:
            sum += remain.val
            mod = sum % 10
            sum //= 10
            head.next = ListNode(mod, head.next)
            remain = remain.next
            head = head.next

        if sum is not 0:
            head.next = ListNode(sum, head.next)

        return result.next


hand = 110
while hand != 0:
    temp = hand % 10
    hand = hand // 10
    print(temp)
