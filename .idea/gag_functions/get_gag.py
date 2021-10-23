def get_gag(line_in_file, operators, operators_in_string, operands):
    split_line = line_in_file.split()
    data_types = []

    for character in split_line:
        if character in operators:
            operators_in_string.append(character)
        elif isinstance(character, str) or isinstance(character, int) or isinstance(character, float):
            operands.append(character)

    for item in operands:
        if item.isdigit():
            data_types.append('number')
        else:
            data_types.append('string')

    operand_1_data_type, operand_2_data_type = data_types
    operand_1, operand_2 = operands
    gag_to_return = f"Operand 1 data type:{operand_1_data_type}, " \
                    f"Operand 2 data type:{operand_2_data_type}, " \
                    f"Operator: {operators_in_string}, " \
                    f"Operand 1: {operand_1} Operand 2: {operand_2}"


    data_types.clear()
    operators_in_string.clear()
    operands.clear()

    return gag_to_return
