# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

# fastest at 42ms, *and* no extra memory (everything is 13.9Mb or 14Mb, randomly)
# very, very odd
class Solution:
    def mergeTwoListsArray(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result_as_array = []
        
        while list1 and list2:
            if list1.val < list2.val:
                result_as_array.append(list1.val)
                list1 = list1.next
            else:
                result_as_array.append(list2.val)
                list2 = list2.next
        
        while list1:
            result_as_array.append(list1.val)
            list1 = list1.next
        
        while list2:
            result_as_array.append(list2.val)
            list2 = list2.next
        
        result = None
        for n in result_as_array[::-1]:
            result = ListNode(n,result)
        
        return result


# gets 82ms, 62ms (8.16%, 38.59%) and 13.9Mb, 14Mb on two sequential runs
class Solution:
    def mergeTwoListsDeadhead(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        deadhead = ListNode()
        target = deadhead
        
        while list1 and list2:
            if list1.val < list2.val:
                target.next = list1
                target = target.next
                list1 = list1.next
            else:
                target.next = list2
                target = target.next
                list2 = list2.next
        
        # from the comments, obviously a better idea but slower on their system somehow!!
        #if list1 or list2:
        #    target.next = list1 if list1 else list2
        
        while list1:
            target.next = list1
            target = target.next
            list1 = list1.next
        
        while list2:
            target.next = list2
            target = target.next
            list2 = list2.next
        
        return deadhead.next


# 50ms
class Solution:
    def mergeTwoListsExtraIf(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 and list2:
            if list1.val < list2.val:
                root = list1
                target = list1
                list1 = list1.next
            else:
                root = list2
                target = list2
                list2 = list2.next
        elif list1:
            return list1
        else:
            return list2
        
        while list1 and list2:
            if list1.val < list2.val:
                target.next = list1
                target = list1 # or target.next
                list1 = list1.next
            else:
                target.next = list2
                target = list2
                list2 = list2.next
        
        while list1:
            target.next = list1
            target = list1
            list1 = list1.next
        
        while list2:
            target.next = list2
            target = list2
            list2 = list2.next
        
        return root