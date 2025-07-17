"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""

def fn_hack_6(s):
    if not s: 
        return ["0"]

    result_list = [] 
    
    for i, item in enumerate(s):
        if i % 2 == 0:
            result_list.append(str(i + 1)) 
        else:
            result_list.append("-")
            
    return result_list

print(fn_hack_6(["a","b","c","d","e"]))
print(fn_hack_6([]))  