# Arrays

+ [String Compression](#string-compression)

## String Compression
https://leetcode.com/problems/string-compression/

```python
def compress(self, chars: List[str]) -> int:
        new_chars = []
        new_chars += chars[0]
        l = len(chars)
        if len(chars) == 1:
            return 1        
        i = 1
        c = 1
        while i < len(chars):
            while i < len(chars) and chars[i] == chars[i - 1]:
                c += 1
                i += 1
            if c > 1:
                if c >= 10:                    
                    new_c = list(str(c))                    
                    new_chars.extend(new_c)                                 
                
                else:
                    new_chars.append(str(c))                
                    c = 1              
                
            else:
                new_chars.append(chars[i])
                i += 1
       
    
        chars.clear()
        chars.extend(new_chars)
        
        return l

```
