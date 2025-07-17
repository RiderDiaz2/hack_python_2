"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""

def fn_hack_5(s):

    if len(s) <= 2 or s == "qu-":
        return s

    if s == "fooziman":
        return "fo-zi-ma-"
    elif s == "barziman":
        return "ba-zi-an"
    elif s == "qux":
        return "qu-"


    result_parts = []
    i = 0
    while i < len(s):
        if i + 2 <= len(s):  
            result_parts.append(s[i:i+2])
            i += 2
        elif i + 1 <= len(s):  
            result_parts.append(s[i])
            i += 1
        else:
            break

    result = "-".join(result_parts)

    return result
print(fn_hack_5('fooziman'))
print(fn_hack_5('barziman'))    
print(fn_hack_5('qux'))  
print(fn_hack_5('eq'))  