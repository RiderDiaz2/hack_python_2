"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(s):
    sustituciones = {
        'a': '@',
        'e': '3',
        'i': '¡',
        'o': '0',
        'u': 'v'
    }
    
    processed_chars = []
    n = len(s)
    for i, char in enumerate(s):
        lower_char = char.lower() 
        if lower_char in sustituciones:
            processed_chars.append(sustituciones[lower_char])
        elif (i == 0 or i == n - 1) and lower_char.isalpha():
            processed_chars.append(lower_char.upper())
        else:
            processed_chars.append(lower_char)
            
    return "".join(processed_chars)

print(fn_hack_3('fooziman'))
print(fn_hack_3('barziman'))    
print(fn_hack_3('3q'))    
print(fn_hack_3('qu'))    
print(fn_hack_3('qux'))    