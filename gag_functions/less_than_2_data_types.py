from gag_functions.clear_lists import clear_lists


def less_than_2_data_types(data_types, operands, operators_in_string):
    operand_1_data_type = data_types  # unpacks the array to the variable
    operand_1 = operands  # also unpacks the array to a variable

    if not operand_1 and not operand_1_data_type:  # if we dont have a first operand and a data type for it
        operator_1 = operators_in_string
        gag_to_return = f"Operator: {operator_1[0]}"

        clear_lists(data_types, operators_in_string, operands)

        return gag_to_return

    if not operators_in_string:  # if line we are on is devoid of an operator
        gag_to_return = f"{operand_1[0]} : {operand_1_data_type[0]}"

        clear_lists(data_types, operators_in_string, operands)

        return gag_to_return

    gag_to_return = f"{operand_1[0]} : {operand_1_data_type[0]}, " \
                    f"Operator: {operators_in_string[0]}"

    clear_lists(data_types, operators_in_string, operands)

    return gag_to_return
