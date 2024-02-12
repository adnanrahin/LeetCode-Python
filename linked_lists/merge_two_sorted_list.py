class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        
        result = ListNode(0)
        head = result

        while list1 != None and list2 != None:
            if list1.val < list2.val:
                head.next = ListNode(list1.val)
                head = head.next
                list1 = list1.next
            elif list2.val < list1.val:
                head.next = ListNode(list2.val)
                head = head.next
                list2 = list2.next
            else:
                head.next = ListNode(list1.val)
                head = head.next
                list1 = list1.next
                head.next = ListNode(list2.val)
                head = head.next
                list2 = list2.next

        while list1 != None:
            head.next = ListNode(list1.val)
            head = head.next
            list1 = list1.next

        while list2 != None:
            head.next = ListNode(list2.val)
            head = head.next
            list2 = list2.next

        return result.next


list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)

list2 = ListNode(4)
list2.next = ListNode(5)
list2.next.next = ListNode(6)

list3 = Solution().mergeTwoLists(list1, list2)
