# Linked-list

+ [Middle of the Linked List](#middle-of-the-linked-list)

## Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list/

<details><summary>Test cases</summary><blockquote>

```python
import unittest
import Middle_of_linked_list as MLL

class TestMiddleofLinkedList(unittest.TestCase):
    def setUp(self):
        self.solution = MLL.Solution()

    def test_middle_of_linked_list(self):
        expected = self.get_linked_list_values(self.build_linked_list([3, 4, 5]))
        actual = self.get_linked_list_values(self.solution.middleNode(self.create_linked_list(5)))
        self.assertEqual(expected, actual)


    def create_linked_list(self, n):
        prev_link = None
        for i in range(n, 0, -1):
            elem = MLL.ListNode(i, prev_link)
            prev_link = elem
        return elem

    def build_linked_list(self, source):
        prev_link = None
        for i in source[::-1]:
            elem = MLL.ListNode(i, prev_link)
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
def middleNode(self, head):
    l = 0
    new_head = head
    if new_head.next is None:
        return new_head
    while new_head:
        new_head = new_head.next
        l += 1
    new_head = head
    m = l // 2
    while m > 0:
        new_head = new_head.next
        m -= 1
    return new_head
```
