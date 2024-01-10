# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):

        nextA = headA
        nextB = headB
        lengthA = 0
        lengthB = 0

        # 计算链表A和链表B的长度
        while True:
            if not nextA and not nextB:
                break
            if nextA:
                lengthA += 1
                nextA = nextA.next
            if nextB:
                lengthB += 1
                nextB = nextB.next

        # 有一个为空都不可能相交，返回None
        if lengthA == 0 or lengthB == 0:
            return None

        nextA = headA
        nextB = headB

        while True:
            if lengthA == lengthB:
                break
            elif lengthA < lengthB:
                nextB = nextB.next
                lengthB -= 1
            else:
                nextA = nextA.next
                lengthA -= 1

        while nextA:
            if nextA is nextB:
                return nextA
            else:
                nextA = nextA.next
                nextB = nextB.next

        return None


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



