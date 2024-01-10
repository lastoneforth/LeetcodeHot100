# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def getIntersectionNode(self, headA: ListNode, headB: ListNode):

        # 双指针的办法
        # 其实基本原理一样，都是要想办法两个链表尾部对齐，然后从到尾部相同距离开始遍历
        # 对齐的方法相当于把A链表后面接一个B链表，B链表后面接一个A链表，这样得到两个长度相同的链表
        ptrA = headA
        ptrB = headB
        if not ptrA or not ptrB:
            return None

        while ptrA is not ptrB:
            ptrA = ptrA.next if ptrA else headB
            ptrB = ptrB.next if ptrB else headA

        return ptrA


if __name__ == '__main__':
    # 测试数据
    a = ListNode(4)
    b = ListNode(1)
    c = ListNode(8)
    d = ListNode(4)
    e = ListNode(5)

    a.next = b
    b.next = c
    c.next = d
    d.next = e

    A = ListNode(5)
    B = ListNode(6)
    A.next = B
    B.next = b

    print(Solution().getIntersectionNode(a, A).val)



