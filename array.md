# Array

+ [Squares of a Sorted Array](#squares-of-a-sorted-array)

## Square of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/

<details><summary>Test cases</summary><blockquote>

```python
import unittest
from squares_of_a_sorted_array import sortedSquares


class MyTestCase(unittest.TestCase):
    def test_squares_of_a_sorted_array(self):
        self.assertEqual(sortedSquares([-2, -5, 184, 24, 4]), [4, 16, 25, 24 * 24, 184 * 184])


if __name__ == '__main__':
    unittest.main()

```

</blockquote></details>



```python
def sortedSquares(self, nums: List[int]) -> List[int]:
    return sorted([i ** 2 for i in nums])
    
```
