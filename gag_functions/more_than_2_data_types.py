from gag_functions.clear_lists import clear_lists


def more_than_2_data_types(data_types, operands, operators_in_string):
    operand_1_data_type, operand_2_data_type, *rest_of_data_types = data_types
    operand_1, operand_2, *rest_of_operands = operands

    if not operators_in_string:
        gag_to_return = f"{operand_1} : {operand_1_data_type}, " \
                        f"{operand_2} : {operand_2_data_type}"

        clear_lists(data_types, operators_in_string, operands)

        return gag_to_return

    for data_type in data_types:
        for operand in operands:
            gag_to_return = f"{operand_1} : {operand_1_data_type}, " \
                    f"{operand_2} : {operand_2_data_type}, " \
                    f"{operand}: {data_type}, "\
                    f"Operator: {operators_in_string}," \
                    # f"{rest_of_operands} : {rest_of_data_types}, " \


    clear_lists(data_types, operators_in_string, operands)

    return gag_to_return
