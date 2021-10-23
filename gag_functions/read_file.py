from gag_functions.get_gag import get_gag
from operators_operands_definitions import operators


def read_file(file_to_read):
    operands = []
    operators_in_string = []

    file = open(file_to_read, 'r')

    while True:
        line = file.readline()

        if not line:
            break

        else:
            print(get_gag(line, operators, operators_in_string, operands))

    file.close()
