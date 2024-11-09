from tester import TesterException
from termcolor import colored


def left_pad(string: str, char: str, length: int):
    if len(string) >= length:
        return string
    return char * (length - len(string)) + string


def print_truth_table(
    input_headers: list[str],
    ouput_headers: list[str],
    expected_outputs: list[list[int]],
    measured_outputs: list[list[int]],
):
    header = f"| {" | ".join(input_headers)} {colored("|", "blue")} {" | ".join(ouput_headers)}"
    print("-" * len(header))
    print(header)


def validate_measured_output(measured_output: list[int]) -> list[int]:
    try:
        measured_output = map(int, measured_output)
    except ValueError:
        raise TesterException(f"Measured output is not an integer: {measured_output}.")
    for measured_output_for_header in measured_output:
        if measured_output_for_header != 0 and measured_output_for_header != 1:
            raise TesterException(f"Measured output is not 1 or 0: {measured_output}.")
    return measured_output
