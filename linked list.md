
# Linked List

+ [Intersection of Two Linked Lists](intersection-of-two-linked-lists)


## Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/

<details><summary>Test cases</summary><blockquote>

```python
import unittest
import Intersection_of_Two_Linked_Lists as ITLL


class TestIntersectionofTwolinkedlists(unittest.TestCase):
    def setUp(self):
        self.solution = ITLL.Solution()

    def test_intersection_of_two_linkedl_ists(self):
        expected = None
        actual = self.solution.getIntersectionNode(self.build_linked_list([4, 1, 8, 4, 5]),
                                                   self.build_linked_list([5, 6, 1, 8, 4, 5]))
        self.assertEqual(expected, actual)

    def build_linked_list(self, source):
        prev_link = None
        for i in source[::-1]:
            elem = ITLL.ListNode(i, prev_link)
            prev_link = elem
        return elem

    def get_linked_list_values(self, head):
        result = []
        curr = head
        while curr is not None:
            result.append(curr.val)
            curr = curr.next
        return result


if __name__ == '__main__':
    unittest.main()

```

</blockquote></details>

```python
def getIntersectionNode(self, headA, headB):
    heads = set()
    head = headA
    while head:
        heads.add(head)
        head = head.next

    head = headB
    while head:
        if head in heads:
            return head
        head = head.next
```
