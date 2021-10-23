from gag_functions.check_if_comment import check_if_comment
from gag_functions.check_multi_line_comment import check_multi_line_comment
from gag_functions.less_than_2_data_types import less_than_2_data_types
from gag_functions.more_than_2_data_types import more_than_2_data_types
from gag_functions.get_multi_line_comment import get_multi_line_comment
from gag_functions.get_comment import get_comment


# file declares and function that takes 3 args and passes them to other functions for processing
def check_print_gag(data_types, operands, operators_in_string):
    for item in operands:
        if item.isdigit():
            data_types.append('integer literal')

        elif '"' in item or "'" in item:
            data_types.append('string')

        else:
            data_types.append('identifier')

    if check_if_comment(operators_in_string, data_types):  # returns true if comment is found and false if not
        return get_comment(operands, data_types, operators_in_string)  # gets the comment we want to print and passes up

    elif check_multi_line_comment(operators_in_string, data_types):  # returns true multiline comment found
        return get_multi_line_comment(operators_in_string, operands, data_types)

    if len(data_types) >= 2:  # if condition is true calls the correct function to process the gag
        return more_than_2_data_types(data_types, operands, operators_in_string)

    elif len(data_types) < 2:  # if condition is true calls the correct functions to process the gag
        return less_than_2_data_types(data_types, operands, operators_in_string)
