# Arrays

+ [String Compression](#string-compression)

## String Compression

https://leetcode.com/problems/string-compression/

```python
def compress(chars: List[str]) -> Union[str, int]:
    new_chars = []
    if len(a) == 0:
        return "list is empty"
    new_chars += chars[0]
    i = 1
    c = 1
    while i < len(chars):
        while i < len(chars) and chars[i] == chars[i - 1]:
            c += 1
            i += 1
        if c > 1:
            new_chars.append(str(c))
            c = 1
        else:
            new_chars.append(chars[i])
            i += 1
    chars.clear()
    chars.extend(new_chars)
    n = [x for x in new_chars if x.isdigit()]
    s = 0
    for i in n:
        s += int(i)
    return s

```
