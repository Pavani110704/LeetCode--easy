    dummy = ListNode()  # dummy node to build result list
    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    # Attach the remaining nodes
    tail.next = list1 if list1 else list2

    return dummy.next