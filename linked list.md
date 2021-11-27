# Linked List

+ [Palindrome Linked List](#palindrome-linked-list)

## Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/

<details><summary>Test cases</summary><blockquote>

```python
import unittest
import Palindrome_linked_list as PLL


class TestisPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = PLL.Solution()

    def test_is_linked_list_palindrome(self):
        expected = True
        actual = self.solution.isPalindrome(self.build_linked_list([1, 3, 3, 1]))
        self.assertEqual(expected, actual)

    def build_linked_list(self, source):
        prev_link = None
        for i in source[::-1]:
            elem = PLL.ListNode(i, prev_link)
            prev_link = elem
        return elem


if __name__ == '__main__':
    unittest.main()

```

</blockquote></details>



```python
def isPalindrome(self, head: Optional[ListNode]) -> bool:
    s = ''
    h = head
    while h:
        s += str(h.val)
        h = h.next            
    return True if s[::-1] == s else False
```
