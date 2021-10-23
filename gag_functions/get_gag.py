from gag_functions.check_print_gag import check_print_gag


def get_gag(line_in_file, operators, operators_in_string, operands):
    split_line = line_in_file.split()  # splits the line by each space and assigns it to split_line variablw
    data_types = []

    for character in split_line:  # iterates through split_line and gets character
        if character in operators:  # if character is an operator append it to operators_in_string
            operators_in_string.append(character)

        # checks if anything is an instance of any data type tested
        elif isinstance(character, str) or isinstance(character, int) or isinstance(character, float):
            operands.append(character)

    return check_print_gag(data_types, operands, operators_in_string)
