"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""


def fn_hack_1(s):
    result_parts = []
    for i in range(0, len(s), 3):
        chunk = s[i : i + 3]
        
        if len(chunk) == 3:
            modified_chunk = f"{chunk[0]}{chunk[1].upper()}{chunk[2]}"
            result_parts.append(modified_chunk)
        else:
            result_parts.append(chunk)
            
    return "".join(result_parts)

print(fn_hack_1("fooziman"))
print(fn_hack_1("qux"))
print(fn_hack_1("eq"))