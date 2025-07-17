"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""

def fn_hack_8(s):
    n = len(s)
    
    result_elements = []
    for i, item in enumerate(s):
    
        if n % 2 != 0: 
            result_elements.append(f"{item}-{i + 1}")
        else: 
            result_elements.append(str(i + 1))
            
    result_elements.reverse()
    
    return result_elements

print(fn_hack_8(["a","b","c","d","e"]))
print(fn_hack_8(["a","b","c"]))
print(fn_hack_8(["a","b","c","d"]))
print(fn_hack_8(["a","b"]))