# Design

+ [Min Stack](#min-stack)

## Min Stack
https://leetcode.com/problems/min-stack/

<details><summary>Test cases</summary><blockquote>

```python
import unittest
import Min_Stack as MS


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = MS.Solution()

    def test_push(self):
        self.assertEqual(self.solution.push(4), [1, 2, 3, 4])

    def test_top(self):
        self.assertEqual(self.solution.top(), 3)

    def test_get_Min(self):
        self.assertEqual(self.solution.getMin(), 1)
        
    def test_pop(self):
        self.assertEqual(self.solution.pop(), [1, 2])


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
