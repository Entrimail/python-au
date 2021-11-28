# Design

+ [Implement Queue using Stacks](#implement-queue-using-stacks)

## Implement Queue using Stacks
https://leetcode.com/problems/implement-queue-using-stacks/

<details><summary>Test cases</summary><blockquote>

```python
import unittest
import Implement_Queue_using_Stacks as IQS

class TestImplementQueueUsingStacks(unittest.TestCase):
    def setUp(self):
        self.solution = IQS.Solution()

    def test_push(self):
        self.assertEqual(self.solution.push(6), [3, 4, 5, 6])

    def test_peek(self):
        self.assertEqual(self.solution.peek(), 3)

    def test_empty(self):
        self.assertEqual(self.solution.empty(), False)

    def test_pop(self):
        self.assertEqual(self.solution.pop(), [3, 4, 5].pop(0))


if __name__ == '__main__':
    unittest.main()
```

</blockquote></details>



```python
def __init__(self):
    self.queue = []
    
def push(self, x: int) -> None:
    self.queue += [x]
def pop(self) -> int:
    x = self.queue[0]
    del self.queue[0]
    return x
def peek(self) -> int:
    return self.queue[0]
    
def empty(self) -> bool:
    return not self.queue
```
