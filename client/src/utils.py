from tester import TesterException
from termcolor import colored


def left_pad(string: str, char: str, length: int):
    if len(string) >= length:
        return string
    return char * (length - len(string)) + string


def line_seperator(color: str, split_color: str, max_len_element: int, countLeftElements: int, countRightElements: int) -> str:
    leftLine = [colored("-", color) * (max_len_element + 2)
                for _ in range(countLeftElements)]
    rightLine = [colored("-", color) * (max_len_element + 2)
                 for _ in range(countLeftElements)]
    return f"{colored("+", color)}{colored("+", color).join(leftLine)}{colored("+", split_color)}" \
        f"{colored("+", color).join(rightLine)}{colored("+", color)}"


def line(color: str, split_color: str, max_len_element: int, leftElements: list[str], rightElements: list[str]):
    return f"{colored("|", color)} {colored(" | ", color).join(map(lambda element: left_pad(element, " ", max_len_element), leftElements))} " \
        f"{colored("|", split_color)} {colored(" | ", color).join(map(lambda element: left_pad(
            element, " ", max_len_element), rightElements))} {colored("|", color)}"


def print_truth_table(
    input_headers: list[str],
    ouput_headers: list[str],
    expected_outputs: list[list[int]],
    measured_outputs: list[list[int]],
):

    max_len = max(len(max(input_headers, key=len)),
                  len(max(ouput_headers, key=len)))

    header = line("magenta", "blue", max_len, input_headers, ouput_headers)
    header_line_seperator = line_seperator(
        "magenta", "blue", max_len, len(input_headers), len(ouput_headers))
    print(header_line_seperator)
    print(header)
    print(header_line_seperator)

    input = 0
    for expected_output, measured_output in zip(expected_outputs, measured_outputs):
        lineString = line("white", "blue", max_len, list(
            left_pad(f"{input:b}", "0", len(input_headers))), map(str, expected_output))
        if list(expected_output) != list(measured_output):
            for expected_output_for_header, measured_output_for_header in zip(expected_output, measured_output):
                if expected_output_for_header != measured_output_for_header:
                    lineString += "   " + \
                        colored(str(measured_output_for_header), "red")
                else:
                    lineString += "   " + str(measured_output_for_header)
        print(lineString)
        print(line_seperator("white", "blue", max_len,
              len(input_headers), len(ouput_headers)))
        input += 1


def validate_measured_output(measured_output: list[str]) -> list[int]:
    try:
        new_measured_output = list(map(int, measured_output))
    except ValueError:
        raise TesterException(
            f"Measured output is not an integer: {measured_output}.")
    for measured_output_for_header in new_measured_output:
        if measured_output_for_header != 0 and measured_output_for_header != 1:
            raise TesterException(
                f"Measured output is not 1 or 0: {measured_output}.")
    return new_measured_output
