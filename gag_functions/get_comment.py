from gag_functions.clear_lists import clear_lists


def get_comment(operands, data_types, operators_in_string):
    comment = operands  # comment variable set to equal operands; operands holds the entire comment
    comment_to_string = ''

    for word in comment:  # iterates through each word in comment
        comment_to_string += word + ' '  # appends word to the end of the comment string

    gag_to_return = f"Comment: {comment_to_string}"
    clear_lists(data_types, operators_in_string, operands)

    return gag_to_return
