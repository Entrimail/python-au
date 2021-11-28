# Linked- list

+ [Merge Two Sorted Lists](#merge-two-sorted-lists)

## Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/

<details><summary>Test cases</summary><blockquote>

```python
import unittest
import Merge_two_sorted_lists as MTSL


class TestMergeTwoLists(unittest.TestCase):
    def setUp(self):
        self.solution = MTSL.Solution()

    def test_merge_two_sorted_lists(self):
        expected = self.get_linked_list_values(self.build_linked_list([1, 2, 3, 4, 5, 6]))
        actual = self.get_linked_list_values(
            self.solution.mergeTwoLists(self.build_linked_list([4, 5, 6]), self.build_linked_list([1, 2, 3])))
        self.assertEqual(expected, actual)

    def build_linked_list(self, source):
        prev_link = None
        for i in source[::-1]:
            elem = MTSL.ListNode(i, prev_link)
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
def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    ans = ListNode()
    a = ans
    while l1 is not None or l2 is not None:
        if l1 is None or l2 is None:
            a.next = l1 or l2
            break
        if l1.val <= l2.val:
            a.next = l1
            l1 = l1.next
        else:
            a.next = l2
            l2 = l2.next
        a = a.next
    return ans.next
```
