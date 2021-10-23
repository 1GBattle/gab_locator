# declares and function that takes in two args operators and data types
# function iterates through operators until the /* or */ operator is found
# once operators is found the correct data type is appended to the array

def check_multi_line_comment(operators, data_types_to_pass):
    for operator in operators:
        if operator == '/*':
            data_types_to_pass.append('multi-line comment')

            return True

        return False
