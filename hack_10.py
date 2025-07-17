"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result_list = []
    num_counter = 1  
    for element in s:
        if isinstance(element, dict):
            new_dict = {str(num_counter): str(num_counter + 1)}
            result_list.append(new_dict)
            num_counter += 2 
        elif isinstance(element, set):
            new_set = {str(num_counter), str(num_counter + 1)}
            result_list.append(new_set)
            num_counter += 2  
        else:
            result_list.append(element)

    return result_list

print(fn_hack_10([{"a":"b"},{"c","d"},{"e":"f"}]))