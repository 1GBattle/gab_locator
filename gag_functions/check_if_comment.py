# declares a function to take in operators and the data types
# function iterates through operators until it sees the comment operator and appends comment to data and returns true
def check_if_comment(operators, data_types_to_pass):
    for operator in operators:
        if operator == '//':
            data_types_to_pass.append('comment')

            return True

        return False
