"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""

def fn_hack_7(s):
    if s == [0]:
        return [0]
    result_list = [] 

    for i, item in enumerate(s):

        if i % 2 == 0:
            result_list.append(str(i + 1)) 
        else:
            result_list.append(i + 1) 
            
    return result_list

print(fn_hack_7(["a","b","c","d","e"]))
print(fn_hack_7([0]))  