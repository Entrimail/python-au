#Design

+ [Implement Stack using Queues](#implement-stack-using-queues)

## Implement Stack using Queues
https://leetcode.com/problems/implement-stack-using-queues/

<details><summary>Test cases</summary><blockquote>

```python
import unittest
import Implement_Stack_using_Queues as ISQ

class TestImplementStack(unittest.TestCase):
    def setUp(self):
        self.solution = ISQ.Solution()

    def test_push(self):
        self.assertEqual(self.solution.push(5), [1, 2, 3, 4, 5])

    def test_top(self):
        self.assertEqual(self.solution.top(), 4)

    def test_empty(self):
        self.assertEqual(self.solution.empty(), False)

    def test_pop(self):
        self.assertEqual(self.solution.pop(), [1, 2, 3, 4].pop())


if __name__ == '__main__':
    unittest.main()
```

</blockquote></details>



```python
def __init__(self):
    self.stack = []
def push(self, val: int) -> None:
    self.stack += [val]
def pop(self) -> None:
    self.stack = self.stack[:-1]
def top(self) -> int:
    return self.stack[-1]
    
def getMin(self) -> int:
    return min(self.stack)
```