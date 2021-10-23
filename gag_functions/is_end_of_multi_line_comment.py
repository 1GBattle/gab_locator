def is_end_of_multiline_comment(operators_in_string):  # checks if we reached the end of the comment and returns true
    for operator in operators_in_string:
        if operator == '*/':
            return True

        return False
