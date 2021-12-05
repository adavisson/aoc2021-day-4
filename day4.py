file_name = "day4-inputs.txt"


# Read lines
def get_formatted_inputs(file_name):
    with open(file_name) as f:
        lines = f.readlines()
    return [line.strip() for line in lines]


def get_called_numbers(values):
    return values[0].split(",")


def get_boards(values):
    boards = []

    i = 2
    while i < len(values):
        board = []
        for j in range(0, 4):
            board.append(values[i+j].split())

        boards.append(board)

        i += 6

    return boards


def main():
    file_lines = get_formatted_inputs(file_name)
    called_numbers = get_called_numbers(file_lines)
    boards = get_boards(file_lines)

    print("Called Numbers: " + str(called_numbers))
    print("Boards: " + str(boards[6]))


main()
