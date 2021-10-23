from gag_functions.is_end_of_multi_line_comment import is_end_of_multiline_comment
from gag_functions.clear_lists import clear_lists


def get_multi_line_comment(operators_in_string, operands, data_types):
    multi_line_comment = operands
    multi_line_comment_to_string = ''

    if not is_end_of_multiline_comment(operators_in_string):  # if line comes back as part of a multi-line comment
                                                              # returns true
        for word in multi_line_comment:
            multi_line_comment_to_string += word + ' '

        gag_to_return = f"Multi-line comment: {multi_line_comment_to_string}"

        for operator in operators_in_string:
            if operator == '*/':

                clear_lists(data_types, operators_in_string, operands)
                
                return gag_to_return
