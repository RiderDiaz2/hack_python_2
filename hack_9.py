"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result_dict = {}
    if "foo" in s:
        original_value = s["foo"]
        if original_value:
            capitalized_value = original_value[0].upper() + original_value[1:]
        else:
            capitalized_value = "" 
        transformed_value = capitalized_value.replace('k', '').replace('K', '')
        result_dict["Foo"] = transformed_value

    return result_dict

print(fn_hack_9({"foo":"fookziman","bar":"barziman"}))