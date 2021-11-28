# Linked List

+ [Sort List](#sort-list)

## Sort List
https://leetcode.com/problems/sort-list/

<details><summary>Test cases</summary><blockquote>

```python
import unittest
import Sort_list as Sl

class TestMiddleofLinkedList(unittest.TestCase):
    def setUp(self):
        self.solution = Sl.Solution()

    def test_middle_of_linked_list(self):
        expected = self.get_linked_list_values(self.build_linked_list([3, 4, 5]))
        actual = self.get_linked_list_values(self.solution.split_list(self.create_linked_list(5)))
        self.assertEqual(expected, actual)


    def test_merge_two_sorted_lists(self):
        expected = self.get_linked_list_values(self.build_linked_list([1, 2, 3, 4, 5, 6]))
        actual = self.get_linked_list_values(
            self.solution.merge(self.build_linked_list([4, 5, 6]), self.build_linked_list([1, 2, 3])))
        self.assertEqual(expected, actual)

    def test_sort(self):
        expected = self.get_linked_list_values(self.build_linked_list([1, 2, 3]))
        actual = self.get_linked_list_values(self.solution.sortList(self.build_linked_list([3, 1, 2])))
        self.assertEqual(expected, actual)


    def create_linked_list(self, n):
        prev_link = None
        for i in range(n, 0, -1):
            elem = Sl.ListNode(i, prev_link)
            prev_link = elem
        return elem

    def build_linked_list(self, source):
        prev_link = None
        for i in source[::-1]:
            elem = Sl.ListNode(i, prev_link)
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
def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head == None or head.next == None:
        return head
    return self.mergeSort(head)
    
    
def split_list(self, head):
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow
    
    
def merge(self,left,right):
    head = None
     
    if not left:
        return right
    if not right:
        return left
         
    if left.val < right.val:
        head = left
        head.next = self.merge(left.next, right)
    else:
        head = right
        head.next = self.merge(left, right.next)
        
    return head


def mergeSort(self, head):
    if head == None or head.next == None:
        return head
    else:
        midNode = self.split_list(head)                
        nextMidNode = midNode.next                    
        midNode.next = None                          
        
        left = self.mergeSort(head)                   
        right = self.mergeSort(nextMidNode)          
        
        return self.merge(left, right)
```
